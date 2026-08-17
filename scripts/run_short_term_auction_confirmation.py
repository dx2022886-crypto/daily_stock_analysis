#!/usr/bin/env python3
"""Stage 5: next-day auction confirmation for the short-term observation pool.

This layer is an observation filter, not an order generator.  Real auction
fields are kept separate from ordinary quote proxies; missing values remain
missing and are reflected in coverage and confidence.
"""

from __future__ import annotations

import argparse
import copy
import json
import logging
import math
import os
import re
import sys
import time
from datetime import date, datetime, time as dt_time, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import akshare as ak
import exchange_calendars as xcals
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "short_term"
STAGE3_PATH = REPORT_DIR / "theme_leader.json"
STAGE4_PATH = REPORT_DIR / "weak_to_strong.json"
STAGE4_POOL_PATH = REPORT_DIR / "candidate_pool_stage4.json"
OUTPUT_JSON_PATH = REPORT_DIR / "auction_confirmation.json"
OUTPUT_MD_PATH = REPORT_DIR / "auction_confirmation.md"
STAGE5_JSON_PATH = REPORT_DIR / "candidate_pool_stage5.json"
STAGE5_MD_PATH = REPORT_DIR / "candidate_pool_stage5.md"

MARKET_TIMEZONE = ZoneInfo("Asia/Shanghai")
FETCH_RETRIES = 3
AUCTION_INPUT_MAX = 15
AUCTION_OUTPUT_MAX = 5
SNAPSHOT_TARGETS = ((9, 20, 5), (9, 23, 0), (9, 24, 50))
GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}
GRADE_SCORE = {"A": 3, "B": 2, "C": 1, "D": 0}
DATA_MODE_CONFIDENCE = {"REAL_AUCTION": 1.0, "PARTIAL": 0.85, "QUOTE_PROXY": 0.70, "UNAVAILABLE": 0.0}
WEIGHTS = {
    "gap_quality": 15.0,
    "auction_volume_strength": 20.0,
    "late_auction_strength": 20.0,
    "theme_resonance": 15.0,
    "previous_setup": 10.0,
    "leader_status": 10.0,
    "risk_quality": 10.0,
}
THEME_SCORES = {"MAIN": 15.0, "DEGRADED_MAIN": 15.0, "SECONDARY": 11.0, "ROTATION": 5.0, "WEAK": 0.0}
SETUP_SCORES = {
    "BROKEN_BOARD_RECOVERY": 10.0,
    "BOARD_BREAK_RECOVERY": 9.0,
    "LEADER_DIVERGENCE": 9.0,
    "THEME_CORE_DIVERGENCE": 8.0,
    "FIRST_PULLBACK": 7.0,
    "TREND_CORE_PULLBACK": 6.0,
    "NONE": 0.0,
}
LEADER_SCORES = {"MARKET_LEADER": 10.0, "THEME_LEADER": 8.0, "FRONT_CORE": 6.0, "BROKEN_CORE": 5.0, "FOLLOWER": 1.0, "OBSERVE": 0.0}

logger = logging.getLogger("short_term_auction_confirmation")
_API_CACHE: dict[str, tuple[list[dict[str, Any]], dict[str, Any]]] = {}
_API_STATS = {"requests": 0, "cache_hits": 0}


def _xshg_calendar() -> Any:
    """Return the exchange-calendars XSHG calendar used for date guards."""
    return xcals.get_calendar("XSHG")


def _is_trading_day(value: date) -> bool:
    calendar = _xshg_calendar()
    sessions = calendar.sessions_in_range(pd.Timestamp(value), pd.Timestamp(value))
    return len(sessions) == 1


def _previous_trading_day(value: date) -> date:
    """Return the latest completed XSHG session strictly before ``value``."""
    calendar = _xshg_calendar()
    start = pd.Timestamp(value - timedelta(days=15))
    end = pd.Timestamp(value - timedelta(days=1))
    sessions = calendar.sessions_in_range(start, end)
    if len(sessions) == 0:
        raise ValueError(f"No previous XSHG session found before {value:%Y-%m-%d}")
    return sessions[-1].date()


def _live_date_guard(target: date, now: datetime, *, snapshot_file: bool = False) -> str | None:
    """Reject live requests that could accidentally score another trading date."""
    if snapshot_file:
        return None
    current_date = now.astimezone(MARKET_TIMEZONE).date()
    if target != current_date:
        return "LIVE_DATE_MISMATCH"
    if not _is_trading_day(current_date):
        return "NON_TRADING_DAY"
    return None


def _snapshot_mode_guard(mode: str, snapshot_file: bool) -> str | None:
    if mode == "snapshot" and not snapshot_file:
        return "SNAPSHOT_FILE_REQUIRED"
    return None


def _stage4_source_date(stage4: dict[str, Any], stage3: dict[str, Any]) -> date | None:
    values = (
        stage4.get("target_date"), stage4.get("date"),
        stage3.get("target_date"), stage3.get("date"),
    )
    for value in values:
        if not value:
            continue
        text = str(value).replace("-", "")[:8]
        try:
            return datetime.strptime(text, "%Y%m%d").date()
        except ValueError:
            continue
    return None


def _validate_stage4_date(stage4: dict[str, Any], stage3: dict[str, Any], expected: date) -> tuple[bool, date | None]:
    source_date = _stage4_source_date(stage4, stage3)
    component_dates = [_stage4_source_date(stage4, {}), _stage4_source_date(stage3, {})]
    # Both artifacts are expected to describe the same completed session;
    # one stale component must not be hidden by the other component's date.
    valid = all(item is not None and item == expected for item in component_dates)
    return valid, source_date


def _workflow_ready_time(now: datetime) -> str:
    configured = os.getenv("SHORT_TERM_WORKFLOW_READY_TIME", "").strip()
    if configured:
        return configured
    return now.astimezone(MARKET_TIMEZONE).isoformat()


def _configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item) for item in value]
    if isinstance(value, (pd.Timestamp, datetime, date)):
        return value.isoformat()
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def _display(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    return str(value).replace("\n", " ").replace("|", "\\|")


def _normalize_code(value: Any) -> str:
    text = str(value or "").strip().upper().replace(" ", "")
    match = re.fullmatch(r"(?:SH|SZ|BJ)?(\d{1,6})(?:\.(?:SH|SZ|BJ))?", text)
    return match.group(1).zfill(6) if match else ""


def _first(row: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = row.get(key)
        if value is not None and value != "":
            return value
    return None


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        number = float(str(value).replace("%", "").replace(",", ""))
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _records(frame: Any) -> list[dict[str, Any]]:
    if frame is None:
        return []
    if isinstance(frame, list):
        return [row for row in frame if isinstance(row, dict)]
    if isinstance(frame, dict):
        return [frame]
    try:
        rows = frame.to_dict(orient="records")
    except Exception:
        return []
    return [row for row in rows if isinstance(row, dict)]


def _source_ok(source: dict[str, Any] | None) -> bool:
    return bool(source and source.get("status") == "success")


def _fetch(function: str, *, source: str = "akshare", symbol: str | None = None, **kwargs: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    params = dict(kwargs)
    if symbol is not None:
        params["symbol"] = symbol
    cache_key = json.dumps([function, params], ensure_ascii=False, sort_keys=True, default=str)
    if cache_key in _API_CACHE:
        _API_STATS["cache_hits"] += 1
        rows, metadata = _API_CACHE[cache_key]
        cached = copy.deepcopy(metadata)
        cached["cache_hit"] = True
        return copy.deepcopy(rows), cached

    _API_STATS["requests"] += 1
    if not hasattr(ak, function):
        metadata = {
            "function": function, "source": source, "symbol": symbol, "status": "failed", "rows": 0,
            "attempts": 0, "params": _json_safe(params),
            "error": {"type": "AttributeError", "message": f"AKShare function {function} is unavailable"},
        }
        _API_CACHE[cache_key] = ([], copy.deepcopy(metadata))
        return [], metadata

    last_error: Exception | None = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            frame = getattr(ak, function)(**params)
            rows = _records(frame)
            metadata = {
                "function": function, "source": source, "symbol": symbol, "status": "success",
                "rows": len(rows), "attempts": attempt, "params": _json_safe(params),
            }
            _API_CACHE[cache_key] = (copy.deepcopy(rows), copy.deepcopy(metadata))
            return rows, metadata
        except Exception as exc:  # Each endpoint is isolated.
            last_error = exc
            if attempt < FETCH_RETRIES:
                time.sleep(2 ** (attempt - 1))
    metadata = {
        "function": function, "source": source, "symbol": symbol, "status": "failed", "rows": 0,
        "attempts": FETCH_RETRIES, "params": _json_safe(params),
        "error": {"type": type(last_error).__name__, "message": str(last_error)},
    }
    _API_CACHE[cache_key] = ([], copy.deepcopy(metadata))
    return [], metadata


def _parse_timestamp(value: Any, default_date: date | None = None) -> datetime | None:
    if isinstance(value, datetime):
        parsed = value
    else:
        text = str(value or "").strip()
        if not text:
            return None
        text = text.replace("Z", "+00:00")
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError:
            for fmt in ("%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%H:%M:%S"):
                try:
                    parsed = datetime.strptime(text, fmt)
                    if fmt == "%H:%M:%S":
                        parsed = datetime.combine(default_date or date.today(), parsed.time())
                    break
                except ValueError:
                    parsed = None
            if parsed is None:
                return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=MARKET_TIMEZONE)
    return parsed.astimezone(MARKET_TIMEZONE)


def _auction_status(now: datetime, *, snapshot_file: bool = False) -> str:
    if snapshot_file:
        return "SNAPSHOT_TEST"
    local = now.astimezone(MARKET_TIMEZONE).time()
    if local < dt_time(9, 15):
        return "BEFORE_AUCTION"
    if local <= dt_time(9, 25):
        return "AUCTION_WINDOW"
    if local <= dt_time(9, 30):
        return "FINAL_SNAPSHOT_ONLY"
    return "OUTSIDE_WINDOW"


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain an object")
    return payload


def _record_value(record: dict[str, Any], analysis: dict[str, Any], key: str) -> Any:
    value = record.get(key)
    return value if value is not None else analysis.get(key)


def _merge_record(records: dict[str, dict[str, Any]], item: dict[str, Any], *, stage4_member: bool = False) -> None:
    code = _normalize_code(item.get("code") or item.get("symbol") or item.get("股票代码"))
    if not code:
        return
    analysis = item.get("weak_to_strong_analysis") if isinstance(item.get("weak_to_strong_analysis"), dict) else {}
    current = records.setdefault(code, {"code": code, "stage4_watchlist_member": False})
    current["stage4_watchlist_member"] = bool(current.get("stage4_watchlist_member") or stage4_member)
    for key in (
        "name", "primary_theme", "primary_theme_rank", "primary_theme_score", "primary_theme_role", "stock_role",
        "leader_score", "market_leader_rank", "resonance_count", "setup_type", "setup_grade",
        "weak_to_strong_score", "final_weak_to_strong_score", "is_limit_up", "is_broken_board",
        "is_limit_down", "board_count", "break_count", "prev_close", "previous_close",
        "prev_volume", "volume_5d", "previous_volume", "prev_day_limit_down", "theme_collapsed",
        "risk_flags", "themes", "industry",
    ):
        value = _record_value(item, analysis, key)
        if value is not None and (current.get(key) is None or key in {"stage4_watchlist_member"}):
            current[key] = copy.deepcopy(value)
    if current.get("name") in (None, ""):
        current["name"] = item.get("name") or analysis.get("name") or ""
    if current.get("weak_to_strong_score") is None:
        current["weak_to_strong_score"] = current.get("final_weak_to_strong_score")


def _input_pool(stage4: dict[str, Any], stage4_pool: dict[str, Any], stage3: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    watchlist_codes: set[str] = set()
    for item in stage4.get("next_day_watchlist", []) or []:
        if isinstance(item, dict):
            _merge_record(records, item, stage4_member=True)
            code = _normalize_code(item.get("code"))
            if code:
                watchlist_codes.add(code)
    eligible_roles = {"MARKET_LEADER", "THEME_LEADER", "FRONT_CORE", "BROKEN_CORE"}
    for item in stage4.get("weak_to_strong_states", []) or []:
        if isinstance(item, dict) and item.get("stock_role") in eligible_roles:
            _merge_record(records, item)
    for item in stage3.get("market_leaders", []) or []:
        if isinstance(item, dict):
            _merge_record(records, item)
    for item in stage3.get("leaders", []) or []:
        if isinstance(item, dict) and item.get("stock_role") in eligible_roles:
            _merge_record(records, item)
    for item in stage4_pool.get("candidates", []) or []:
        if isinstance(item, dict):
            analysis = item.get("weak_to_strong_analysis") or {}
            if analysis.get("stock_role") in eligible_roles:
                _merge_record(records, item)

    def sort_key(item: dict[str, Any]) -> tuple[Any, ...]:
        grade = str(item.get("setup_grade") or "D")
        return (
            GRADE_ORDER.get(grade, 3),
            -(float(item.get("weak_to_strong_score")) if _number(item.get("weak_to_strong_score")) is not None else float("-inf")),
            -(float(item.get("leader_score")) if _number(item.get("leader_score")) is not None else float("-inf")),
            _number(item.get("primary_theme_rank")) if _number(item.get("primary_theme_rank")) is not None else 999,
            -(_number(item.get("resonance_count")) or 0),
            item.get("code", ""),
        )

    ordered = sorted(records.values(), key=sort_key)[:AUCTION_INPUT_MAX]
    for item in ordered:
        item["stage4_watchlist_member"] = item.get("code") in watchlist_codes
    return ordered, {"all_input_count": len(records), "stage4_watchlist_count": len(watchlist_codes), "eligible_roles": sorted(eligible_roles)}


def _snapshot_rows(snapshot: dict[str, Any], default_date: date | None = None) -> list[dict[str, Any]]:
    raw = snapshot.get("rows") or snapshot.get("stocks") or snapshot.get("quotes") or snapshot.get("data") or []
    if isinstance(raw, dict):
        rows = []
        for code, value in raw.items():
            row = dict(value) if isinstance(value, dict) else {"value": value}
            row.setdefault("code", code)
            rows.append(row)
        return rows
    return _records(raw)


def _load_snapshot_file(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        raw_snapshots = payload
    elif isinstance(payload, dict) and isinstance(payload.get("snapshots"), list):
        raw_snapshots = payload["snapshots"]
    elif isinstance(payload, dict):
        raw_snapshots = [payload]
    else:
        raise ValueError("snapshot file must contain an object, list, or snapshots list")
    result: list[dict[str, Any]] = []
    for index, snapshot in enumerate(raw_snapshots):
        if not isinstance(snapshot, dict):
            continue
        timestamp = _parse_timestamp(snapshot.get("timestamp") or snapshot.get("time"))
        rows = _snapshot_rows(snapshot)
        result.append({"timestamp": timestamp, "timestamp_text": snapshot.get("timestamp") or snapshot.get("time") or f"snapshot-{index + 1}", "rows": rows})
    return sorted(result, key=lambda item: item.get("timestamp") or datetime.min.replace(tzinfo=MARKET_TIMEZONE))


def _flatten_bid_ask(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if len(rows) == 1:
        return rows[0]
    result: dict[str, Any] = {}
    for row in rows:
        item = _first(row, "item", "项目", "名称", "key", "字段")
        value = _first(row, "value", "值", "data")
        if item is not None:
            result[str(item)] = value
        else:
            result.update(row)
    return result


def _live_snapshot_once(records: list[dict[str, Any]], current: datetime, sources: list[dict[str, Any]]) -> dict[str, Any]:
    spot_rows, spot_source = _fetch("stock_zh_a_spot_em", source="eastmoney")
    sources.append(spot_source)
    spot_map = {_normalize_code(_first(row, "代码", "股票代码", "code")): row for row in spot_rows}
    rows: list[dict[str, Any]] = []
    for record in records:
        code = record["code"]
        row = dict(spot_map.get(code) or {})
        row.setdefault("code", code)
        if hasattr(ak, "stock_bid_ask_em"):
            bid_rows, bid_source = _fetch("stock_bid_ask_em", source="eastmoney", symbol=code)
            sources.append(bid_source)
            row.update(_flatten_bid_ask(bid_rows))
        else:
            sources.append({"function": "stock_bid_ask_em", "source": "eastmoney", "symbol": code, "status": "failed", "rows": 0, "attempts": 0, "error": {"type": "AttributeError", "message": "AKShare function stock_bid_ask_em is unavailable"}})
        rows.append(row)
    return {"timestamp": current, "timestamp_text": current.isoformat(), "rows": rows}


def _snapshot_schedule(now: datetime) -> tuple[list[str], list[datetime]]:
    """Split auction targets into missed and still-waitable targets."""
    current = now.astimezone(MARKET_TIMEZONE)
    missed: list[str] = []
    pending: list[datetime] = []
    for hour, minute, second in SNAPSHOT_TARGETS:
        target = datetime.combine(current.date(), dt_time(hour, minute, second), tzinfo=MARKET_TIMEZONE)
        if current < target:
            pending.append(target)
        else:
            missed.append(target.isoformat())
    return missed, pending


def _live_snapshots(records: list[dict[str, Any]], now: datetime, sources: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    snapshots: list[dict[str, Any]] = []
    missed, pending = _snapshot_schedule(now)
    max_wait = int(os.getenv("SHORT_TERM_AUCTION_MAX_WAIT_SECONDS", "360"))
    for target in pending:
        current = datetime.now(MARKET_TIMEZONE)
        wait = max(0.0, (target - current).total_seconds())
        if wait > 0:
            if wait > max_wait:
                missed.append(target.isoformat())
                continue
            time.sleep(wait)
            current = datetime.now(MARKET_TIMEZONE)
        if current.astimezone(MARKET_TIMEZONE).time() > dt_time(9, 25):
            missed.append(target.isoformat())
            break
        snapshots.append(_live_snapshot_once(records, current, sources))
    return snapshots, missed


def _canonical_snapshot_row(row: dict[str, Any]) -> dict[str, Any]:
    result = dict(row)
    result["code"] = _normalize_code(_first(row, "code", "代码", "股票代码", "symbol"))
    result["name"] = _first(row, "name", "名称", "股票名称")
    result["prev_close"] = _number(_first(row, "prev_close", "previous_close", "昨收", "昨收价"))
    result["auction_reference_price"] = _number(_first(row, "auction_reference_price", "集合竞价参考价", "竞价参考价", "匹配价"))
    result["auction_matched_volume"] = _number(_first(row, "auction_matched_volume", "集合竞价匹配量", "竞价匹配量", "匹配量"))
    result["auction_unmatched_volume"] = _number(_first(row, "auction_unmatched_volume", "集合竞价未匹配量", "竞价未匹配量", "未匹配量"))
    result["auction_unmatched_side"] = _first(row, "auction_unmatched_side", "未匹配方向", "竞价未匹配方向")
    result["proxy_price"] = _number(_first(row, "proxy_price", "最新价", "现价", "price"))
    result["proxy_buy1"] = _number(_first(row, "proxy_buy1", "买一价", "买1价", "buy1"))
    result["proxy_buy1_volume"] = _number(_first(row, "proxy_buy1_volume", "买一量", "买1量", "buy1_volume"))
    result["proxy_sell1"] = _number(_first(row, "proxy_sell1", "卖一价", "卖1价", "sell1"))
    result["proxy_sell1_volume"] = _number(_first(row, "proxy_sell1_volume", "卖一量", "卖1量", "sell1_volume"))
    result["proxy_volume"] = _number(_first(row, "proxy_volume", "成交量", "volume"))
    result["proxy_amount"] = _number(_first(row, "proxy_amount", "成交额", "amount"))
    result["timestamp"] = _parse_timestamp(row.get("timestamp") or row.get("time")) or row.get("timestamp")
    return result


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _gap_score(gap: float | None) -> float | None:
    if gap is None:
        return None
    if gap < -1:
        return 0.0
    if gap < 0:
        return 4.0
    if gap < 1:
        return 8.0
    if gap < 3:
        return 15.0
    if gap < 5:
        return 12.0
    if gap < 7:
        return 7.0
    return 3.0


def _late_strength(rows: list[dict[str, Any]], *, real: bool) -> float | None:
    canonical = [_canonical_snapshot_row(row) for row in rows]
    canonical = [row for row in canonical if row.get("auction_reference_price" if real else "proxy_price") is not None]
    if len(canonical) < 2:
        return None
    first, last = canonical[-2], canonical[-1]
    price_key = "auction_reference_price" if real else "proxy_price"
    price_change = (last[price_key] / first[price_key] - 1) * 100 if first[price_key] else None
    volume_key = "auction_matched_volume" if real else "proxy_volume"
    volume_change = None
    if first.get(volume_key) is not None and last.get(volume_key) is not None and first[volume_key] > 0:
        volume_change = last[volume_key] / first[volume_key] - 1
    score = 10.0
    used = 1
    if price_change is not None:
        score += _clamp(price_change * 8, -8, 8)
    if volume_change is not None:
        score += _clamp(volume_change * 5, -5, 5)
        used += 1
    side = str(last.get("auction_unmatched_side") or "").lower()
    if side in {"买", "买方", "buy", "b"}:
        score += 4
    elif side in {"卖", "卖方", "sell", "s"}:
        score -= 4
    return round(_clamp(score, 0, 20) * (1.0 if real else 0.70), 4)


def _weighted_score(components: dict[str, float | None]) -> dict[str, Any]:
    available = {key: value for key, value in components.items() if value is not None}
    raw = round(sum(float(value) for value in available.values()), 4) if available else None
    available_weight = round(sum(WEIGHTS[key] for key in available), 4)
    coverage = round(available_weight / sum(WEIGHTS.values()), 4)
    normalized = round(raw / available_weight * 100, 4) if raw is not None and available_weight else None
    confidence_adjusted = round(normalized * math.sqrt(coverage), 4) if normalized is not None else None
    return {
        "score_raw": raw,
        "available_weight": available_weight,
        "coverage_ratio": coverage,
        "normalized_score": normalized,
        "confidence_adjusted_score": confidence_adjusted,
        "data_quality": "complete" if len(available) == len(WEIGHTS) else "partial" if available else "unavailable",
        "score_components": {key: (round(float(value), 4) if value is not None else None) for key, value in components.items()},
    }


def _hard_rejects(record: dict[str, Any], observation: dict[str, Any], late_strength: float | None) -> list[str]:
    reasons: list[str] = []
    gap = observation.get("gap_pct") if observation.get("gap_pct") is not None else observation.get("proxy_gap_pct")
    if record.get("is_limit_down") is True or (_number(gap) is not None and _number(gap) <= -9.5):
        reasons.append("LIMIT_DOWN_AUCTION")
    if _number(gap) is not None and _number(gap) < -3:
        reasons.append("EXTREME_LOW_OPEN")
    if record.get("theme_collapsed") is True or "THEME_COLLAPSE" in (record.get("risk_flags") or []):
        reasons.append("THEME_COLLAPSE")
    if record.get("stage4_watchlist_member") and record.get("stock_role") in {"FOLLOWER", "OBSERVE"}:
        reasons.append("LEADER_LOST_STATUS")
    if late_strength is not None and late_strength < 5:
        reasons.append("LATE_AUCTION_COLLAPSE")
    return list(dict.fromkeys(reasons))


def _risk_quality(record: dict[str, Any], observation: dict[str, Any], late_strength: float | None) -> float:
    score = 10.0
    flags = set(record.get("risk_flags") or [])
    score -= min(4.0, len(flags) * 2.0)
    if record.get("stock_role") in {"FOLLOWER", "OBSERVE"}:
        score -= 2.0
    gap = observation.get("gap_pct") if observation.get("gap_pct") is not None else observation.get("proxy_gap_pct")
    if gap is not None and gap > 7:
        score -= 4.0
    if gap is not None and gap < -3:
        score -= 4.0
    if observation.get("proxy_sell1_volume") is not None and observation.get("proxy_buy1_volume") is not None and observation["proxy_sell1_volume"] > observation["proxy_buy1_volume"] * 2:
        score -= 3.0
    if late_strength is not None and late_strength < 8:
        score -= 2.0
    return round(_clamp(score, 0, 10), 4)


def _grade(score: float | None, coverage: float, data_mode: str, hard_rejects: list[str]) -> str:
    if hard_rejects or score is None:
        return "D"
    grade = "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 60 else "D"
    if coverage < 0.50 and GRADE_ORDER[grade] < GRADE_ORDER["C"]:
        grade = "C"
    if data_mode == "QUOTE_PROXY" and GRADE_ORDER[grade] < GRADE_ORDER["B"]:
        grade = "B"
    return grade


def _human_reason(state: dict[str, Any]) -> str:
    theme = state.get("primary_theme") or "核心题材"
    role = state.get("primary_theme_role") or state.get("stock_role") or "观察对象"
    gap = state.get("gap_pct") if state.get("gap_pct") is not None else state.get("proxy_gap_pct")
    gap_text = f"{gap:.1f}%" if isinstance(gap, (float, int)) else "数据不足"
    late = state.get("late_auction_strength")
    if state.get("auction_qualified"):
        late_text = "9:20后价格和买盘同步增强" if late is not None and late >= 12 else "竞价后段保持稳定"
        return f"{theme}{role}，竞价参考涨幅{gap_text}，{late_text}，竞价确认通过，等待9:30开盘承接确认。"
    risk = "、".join(state.get("hard_reject_reasons") or []) or "数据覆盖不足"
    return f"{theme}{role}，竞价参考涨幅{gap_text}，竞价确认不通过，原因：{risk}。"


def _build_state(
    record: dict[str, Any],
    snapshots: list[dict[str, Any]],
    *,
    theme_source_mode: str = "",
    final_snapshot_only: bool = False,
) -> dict[str, Any]:
    latest_rows = {_normalize_code(row.get("code")): _canonical_snapshot_row(row) for row in _snapshot_rows(snapshots[-1])} if snapshots else {}
    latest = latest_rows.get(record["code"], {})
    prev_close = _number(record.get("prev_close") or record.get("previous_close") or latest.get("prev_close"))
    real_gap = None
    proxy_gap = None
    if latest.get("auction_reference_price") is not None and prev_close:
        real_gap = (latest["auction_reference_price"] / prev_close - 1) * 100
    if latest.get("proxy_price") is not None and prev_close:
        proxy_gap = (latest["proxy_price"] / prev_close - 1) * 100
    has_real = any(latest.get(key) is not None for key in ("auction_reference_price", "auction_matched_volume", "auction_unmatched_volume"))
    has_proxy = any(latest.get(key) is not None for key in ("proxy_price", "proxy_buy1", "proxy_volume"))
    if has_real and latest.get("auction_reference_price") is not None and latest.get("auction_matched_volume") is not None:
        data_mode = "REAL_AUCTION"
    elif has_real:
        data_mode = "PARTIAL"
    elif has_proxy:
        data_mode = "QUOTE_PROXY"
    else:
        data_mode = "UNAVAILABLE"

    real_volume = None
    if data_mode == "REAL_AUCTION" and latest.get("auction_matched_volume") is not None:
        previous_volume = _number(record.get("prev_volume") or record.get("previous_volume") or record.get("volume_5d"))
        if previous_volume and previous_volume > 0:
            real_volume = _clamp(latest["auction_matched_volume"] / previous_volume * 20, 0, 20)
    proxy_volume_strength = None
    if latest.get("proxy_volume") is not None:
        previous_volume = _number(record.get("prev_volume") or record.get("previous_volume") or record.get("volume_5d"))
        if previous_volume and previous_volume > 0:
            proxy_volume_strength = round(_clamp(latest["proxy_volume"] / previous_volume * 20, 0, 20), 4)
    snapshot_rows = []
    for snapshot in snapshots:
        for row in _snapshot_rows(snapshot):
            if _normalize_code(row.get("code") or row.get("代码")) == record["code"]:
                snapshot_rows.append(_canonical_snapshot_row(row))
    late_real = _late_strength(snapshot_rows, real=True) if any(row.get("auction_reference_price") is not None for row in snapshot_rows) else None
    late_proxy = _late_strength(snapshot_rows, real=False) if any(row.get("proxy_price") is not None for row in snapshot_rows) else None
    # A 09:25-09:30 run is a single final snapshot.  It cannot establish
    # late-auction direction, even if the row itself contains real fields.
    late = None if final_snapshot_only else (late_real if late_real is not None else late_proxy)
    gap = real_gap if real_gap is not None else proxy_gap
    gap_component = _gap_score(gap)
    theme_component = THEME_SCORES.get(record.get("primary_theme_role"))
    if theme_component is not None and theme_source_mode == "INDUSTRY_DEGRADED":
        theme_component = round(theme_component * 0.70, 4)
    setup_type = record.get("setup_type")
    setup_component = SETUP_SCORES.get(setup_type) if setup_type is not None else None
    leader_component = LEADER_SCORES.get(record.get("stock_role")) if record.get("stock_role") is not None else None
    components = {
        "gap_quality": gap_component,
        "auction_volume_strength": real_volume,
        "late_auction_strength": late,
        "theme_resonance": theme_component,
        "previous_setup": setup_component,
        "leader_status": leader_component,
        "risk_quality": _risk_quality(record, latest, late) if data_mode != "UNAVAILABLE" else None,
    }
    score_details = _weighted_score(components)
    hard_rejects = _hard_rejects(record, {"gap_pct": real_gap, "proxy_gap_pct": proxy_gap}, late)
    if score_details["coverage_ratio"] < 0.30:
        hard_rejects.append("DATA_TOO_LOW")
    hard_rejects = list(dict.fromkeys(hard_rejects))
    grade = _grade(score_details["confidence_adjusted_score"], score_details["coverage_ratio"], data_mode, hard_rejects)
    if final_snapshot_only and GRADE_ORDER[grade] < GRADE_ORDER["C"]:
        grade = "C"
    data_confidence = DATA_MODE_CONFIDENCE[data_mode]
    final_score = round(score_details["confidence_adjusted_score"] * data_confidence, 4) if score_details["confidence_adjusted_score"] is not None else None
    state = copy.deepcopy(record)
    state.update({
        "auction_reference_price": latest.get("auction_reference_price"),
        "auction_matched_volume": latest.get("auction_matched_volume"),
        "auction_unmatched_volume": latest.get("auction_unmatched_volume"),
        "auction_unmatched_side": latest.get("auction_unmatched_side"),
        "proxy_price": latest.get("proxy_price"),
        "proxy_buy1": latest.get("proxy_buy1"),
        "proxy_buy1_volume": latest.get("proxy_buy1_volume"),
        "proxy_sell1": latest.get("proxy_sell1"),
        "proxy_sell1_volume": latest.get("proxy_sell1_volume"),
        "proxy_volume": latest.get("proxy_volume"),
        "proxy_amount": latest.get("proxy_amount"),
        "auction_data_mode": data_mode,
        "data_mode_confidence": data_confidence,
        "gap_pct": round(real_gap, 4) if real_gap is not None else None,
        "proxy_gap_pct": round(proxy_gap, 4) if proxy_gap is not None else None,
        "proxy_volume_strength": proxy_volume_strength,
        "late_auction_strength": late,
        "hard_reject_reasons": hard_rejects,
        "auction_grade": grade,
        "auction_qualified": not hard_rejects and grade in {"A", "B", "C"},
        "final_auction_score": final_score,
        "theme_source_mode": theme_source_mode or None,
        "snapshot_count": len(snapshots),
        "final_snapshot_only": final_snapshot_only,
        **score_details,
    })
    state["human_reason"] = _human_reason(state)
    return state


def _build_watchlist(states: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered = sorted(
        states,
        key=lambda item: (
            0 if item.get("auction_qualified") else 1,
            GRADE_ORDER.get(item.get("auction_grade", "D"), 3),
            -(item.get("final_auction_score") if item.get("final_auction_score") is not None else float("-inf")),
            -(_number(item.get("leader_score")) or 0),
            -(_number(item.get("weak_to_strong_score")) or 0),
            item.get("code", ""),
        ),
    )
    result: list[dict[str, Any]] = []
    for rank, item in enumerate([item for item in ordered if item.get("auction_qualified")][:AUCTION_OUTPUT_MAX], start=1):
        result.append({
            "rank": rank,
            "code": item.get("code"),
            "name": item.get("name"),
            "auction_grade": item.get("auction_grade"),
            "final_auction_score": item.get("final_auction_score"),
            "coverage_ratio": item.get("coverage_ratio"),
            "auction_data_mode": item.get("auction_data_mode"),
            "stage4_watchlist_member": bool(item.get("stage4_watchlist_member")),
            "primary_theme": item.get("primary_theme"),
            "primary_theme_role": item.get("primary_theme_role"),
            "stock_role": item.get("stock_role"),
            "leader_score": item.get("leader_score"),
            "hard_reject_reasons": item.get("hard_reject_reasons") or [],
            "human_reason": item.get("human_reason"),
        })
    return result


def _source_mode(states: list[dict[str, Any]]) -> str:
    modes = {item.get("auction_data_mode") for item in states if item.get("auction_data_mode")}
    modes.discard("UNAVAILABLE")
    if not modes:
        return "UNAVAILABLE"
    if modes == {"REAL_AUCTION"}:
        return "REAL_AUCTION"
    if modes <= {"QUOTE_PROXY"}:
        return "QUOTE_PROXY"
    return "MIXED"


def _data_quality(status: str, states: list[dict[str, Any]], failures: list[dict[str, Any]], *, final_snapshot_only: bool, snapshots: list[dict[str, Any]], snapshot_file: bool) -> str:
    if final_snapshot_only and snapshots:
        # One final sample cannot support the normal multi-point auction
        # confirmation, so available data is explicitly partial.
        return "partial" if any(item.get("rows") for item in snapshots) else "unavailable"
    if not snapshot_file and status in {"BEFORE_AUCTION", "OUTSIDE_WINDOW", "NON_TRADING_DAY", "LIVE_DATE_MISMATCH"}:
        return "unavailable"
    if states and all(item.get("auction_data_mode") == "UNAVAILABLE" for item in states):
        return "unavailable"
    if failures or any(item.get("data_quality") != "complete" for item in states):
        return "partial"
    return "complete"


def _failure_payload(
    *,
    target: date,
    status: str,
    snapshot_mode: str,
    workflow_ready_time: str,
    stage4_source_run_id: str,
    stage4_source_date: date | None,
    expected_previous_trading_date: date | None,
    input_meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "phase": "short_term_auction_confirmation_v1",
        "market": "cn",
        "target_date": target.strftime("%Y%m%d"),
        "timezone": "Asia/Shanghai",
        "workflow_ready_time": workflow_ready_time,
        "auction_status": status,
        "snapshot_mode": snapshot_mode,
        "source_mode": "UNAVAILABLE",
        "data_quality": "unavailable",
        "input_pool_count": 0,
        "input_pool_meta": input_meta or {},
        "stage4_source_run_id": stage4_source_run_id or None,
        "stage4_source_date": stage4_source_date.strftime("%Y%m%d") if stage4_source_date else None,
        "expected_previous_trading_date": expected_previous_trading_date.strftime("%Y%m%d") if expected_previous_trading_date else None,
        "missed_snapshots": [],
        "snapshot_targets": [f"{hour:02d}:{minute:02d}:{second:02d}" for hour, minute, second in SNAPSHOT_TARGETS],
        "snapshots": [],
        "auction_states": [],
        "auction_watchlist": [],
        "sources": [],
        "source_failures": [],
        "api_stats": dict(_API_STATS),
        "error": {"code": status, "message": status},
    }


def _enrich_stage5(stage4_pool: dict[str, Any], states: dict[str, dict[str, Any]]) -> dict[str, Any]:
    result = copy.deepcopy(stage4_pool)
    result["stage"] = "short_term_auction_confirmation_v1"
    enriched: list[Any] = []
    for item in stage4_pool.get("candidates", []) or []:
        if not isinstance(item, dict):
            enriched.append(item)
            continue
        copy_item = copy.deepcopy(item)
        state = states.get(_normalize_code(item.get("code")), {})
        copy_item["auction_confirmation"] = {
            "auction_qualified": state.get("auction_qualified", False),
            "auction_grade": state.get("auction_grade", "D"),
            "final_auction_score": state.get("final_auction_score"),
            "coverage_ratio": state.get("coverage_ratio"),
            "auction_data_mode": state.get("auction_data_mode", "UNAVAILABLE"),
            "stage4_watchlist_member": state.get("stage4_watchlist_member", False),
            "hard_reject_reasons": state.get("hard_reject_reasons") or [],
            "human_reason": state.get("human_reason"),
        }
        enriched.append(copy_item)
    result["candidates"] = enriched
    return result


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_markdown(payload: dict[str, Any]) -> None:
    lines = [
        "# 《A股短线集合竞价确认（改造第5阶段）》",
        "",
        "> 本报告是次日集合竞价观察与淘汰层，不是买入名单，不输出自动下单指令；最终仍需第6阶段开盘确认。",
        "",
        f"- 竞价状态：`{_display(payload.get('auction_status'))}`",
        f"- 数据源模式：`{_display(payload.get('source_mode'))}`",
        f"- 数据质量：`{_display(payload.get('data_quality'))}`",
        f"- 输入观察数：`{_display(payload.get('input_pool_count'))}`",
        "",
        "## Auction Watchlist Top5",
        "",
        "| 排名 | 代码 | 名称 | 评级 | 最终分 | 覆盖率 | 数据模式 | Stage4观察池 | 题材 | 角色 |",
        "| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for item in payload.get("auction_watchlist", []) or []:
        lines.append(f"| {_display(item.get('rank'))} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(item.get('auction_grade'))} | {_display(item.get('final_auction_score'))} | {_display(item.get('coverage_ratio'))} | {_display(item.get('auction_data_mode'))} | {_display(item.get('stage4_watchlist_member'))} | {_display(item.get('primary_theme'))} | {_display(item.get('stock_role'))} |")
    lines.extend(["", "## 全部竞价观察状态", "", "| 代码 | 名称 | 竞价模式 | 参考涨幅 | 代理涨幅 | 后段强度 | 评级 | 最终分 | 通过 | 硬否决 |", "| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- | --- |"])
    for item in payload.get("auction_states", []) or []:
        lines.append(f"| {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(item.get('auction_data_mode'))} | {_display(item.get('gap_pct'))}% | {_display(item.get('proxy_gap_pct'))}% | {_display(item.get('late_auction_strength'))} | {_display(item.get('auction_grade'))} | {_display(item.get('final_auction_score'))} | {_display(item.get('auction_qualified'))} | {_display(item.get('hard_reject_reasons'))} |")
    lines.extend(["", "## 说明", "", "竞价确认通过只表示进入观察名单，不能替代09:30开盘确认。代理行情字段以 proxy_ 开头，不能当作真实集合竞价匹配量。", ""])
    OUTPUT_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def _write_stage5_markdown(payload: dict[str, Any]) -> None:
    lines = ["# A股短线候选池（改造第5阶段）", "", "> 保持Stage4候选池原始顺序，仅增加集合竞价确认字段。", "", "| 原排名 | 代码 | 名称 | 竞价评级 | 最终分 | 竞价模式 | 是否通过 |", "| ---: | --- | --- | --- | ---: | --- | --- |"]
    for index, item in enumerate(payload.get("candidates", []) or [], start=1):
        if not isinstance(item, dict):
            continue
        confirmation = item.get("auction_confirmation") or {}
        lines.append(f"| {index} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(confirmation.get('auction_grade'))} | {_display(confirmation.get('final_auction_score'))} | {_display(confirmation.get('auction_data_mode'))} | {_display(confirmation.get('auction_qualified'))} |")
    STAGE5_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stage-5 auction confirmation reports.")
    parser.add_argument("--target-date", default=os.getenv("SHORT_TERM_AUCTION_DATE", ""), help="Target trading date in YYYYMMDD.")
    parser.add_argument("--snapshot-file", default=os.getenv("SHORT_TERM_AUCTION_SNAPSHOT_FILE", ""), help="Offline JSON snapshot file.")
    parser.add_argument("--snapshot-mode", default=os.getenv("SHORT_TERM_AUCTION_SNAPSHOT_MODE", "live"), choices=("live", "snapshot"), help="Live sampling or offline snapshot mode.")
    parser.add_argument("--stage4-run-id", default=os.getenv("STAGE4_SOURCE_RUN_ID", ""), help="GitHub Actions run id that produced the Stage4 artifact.")
    return parser.parse_args()


def _target_date(raw: str) -> date:
    if raw:
        return datetime.strptime(raw, "%Y%m%d").date()
    return datetime.now(MARKET_TIMEZONE).date()


def main() -> int:
    _configure_logging()
    args = _parse_args()
    now = datetime.now(MARKET_TIMEZONE)
    ready_time = _workflow_ready_time(now)
    snapshot_path = Path(args.snapshot_file) if args.snapshot_file else None
    target = _target_date(args.target_date)
    stage4_source_run_id = str(args.stage4_run_id or "")
    expected_previous: date | None = None
    try:
        expected_previous = _previous_trading_day(target)
    except Exception:
        logger.exception("Cannot resolve previous XSHG trading day for %s", target)

    try:
        stage3 = _load_json(STAGE3_PATH)
        stage4 = _load_json(STAGE4_PATH)
        stage4_pool = _load_json(STAGE4_POOL_PATH)
    except Exception:
        logger.exception("Cannot load stage-3/stage-4 inputs")
        return 1

    source_date = _stage4_source_date(stage4, stage3)
    snapshot_error = _snapshot_mode_guard(args.snapshot_mode, bool(snapshot_path))
    if snapshot_error:
        payload = _failure_payload(
            target=target,
            status=snapshot_error,
            snapshot_mode=args.snapshot_mode,
            workflow_ready_time=ready_time,
            stage4_source_run_id=stage4_source_run_id,
            stage4_source_date=source_date,
            expected_previous_trading_date=expected_previous,
        )
        _write_json(OUTPUT_JSON_PATH, payload)
        _write_markdown(payload)
        _write_json(STAGE5_JSON_PATH, stage4_pool)
        _write_stage5_markdown(stage4_pool)
        return 1

    # Live mode must use today's Shanghai date.  This guard runs before any
    # AKShare call, so a weekend or mismatched target cannot create a fake list.
    live_error = _live_date_guard(target, now, snapshot_file=bool(snapshot_path))
    if live_error:
        payload = _failure_payload(
            target=target,
            status=live_error,
            snapshot_mode=args.snapshot_mode,
            workflow_ready_time=ready_time,
            stage4_source_run_id=stage4_source_run_id,
            stage4_source_date=source_date,
            expected_previous_trading_date=expected_previous,
        )
        _write_json(OUTPUT_JSON_PATH, payload)
        _write_markdown(payload)
        _write_json(STAGE5_JSON_PATH, stage4_pool)
        _write_stage5_markdown(stage4_pool)
        return 0 if live_error == "NON_TRADING_DAY" else 1

    if not snapshot_path and expected_previous is not None:
        valid_stage4, source_date = _validate_stage4_date(stage4, stage3, expected_previous)
        if not valid_stage4:
            logger.error("STALE_STAGE4_INPUT: source=%s expected=%s", source_date, expected_previous)
            payload = _failure_payload(
                target=target,
                status="STALE_STAGE4_INPUT",
                snapshot_mode=args.snapshot_mode,
                workflow_ready_time=ready_time,
                stage4_source_run_id=stage4_source_run_id,
                stage4_source_date=source_date,
                expected_previous_trading_date=expected_previous,
            )
            _write_json(OUTPUT_JSON_PATH, payload)
            _write_markdown(payload)
            _write_json(STAGE5_JSON_PATH, stage4_pool)
            _write_stage5_markdown(stage4_pool)
            return 1

    records, input_meta = _input_pool(stage4, stage4_pool, stage3)
    status = _auction_status(now, snapshot_file=bool(snapshot_path))
    sources: list[dict[str, Any]] = []
    missed_snapshots: list[str] = []
    if snapshot_path:
        try:
            snapshots = _load_snapshot_file(snapshot_path)
        except Exception as exc:
            snapshots = []
            sources.append({"function": "snapshot_file", "symbol": None, "status": "failed", "rows": 0, "attempts": 1, "error": {"type": type(exc).__name__, "message": str(exc)}})
    elif status == "AUCTION_WINDOW":
        snapshots, missed_snapshots = _live_snapshots(records, now, sources)
    elif status == "FINAL_SNAPSHOT_ONLY":
        snapshots = [_live_snapshot_once(records, now, sources)]
        missed_snapshots = [f"{now.date().isoformat()} 09:20:05", f"{now.date().isoformat()} 09:23:00"]
    else:
        snapshots = []
    theme_source_mode = str(stage3.get("source_mode") or "")
    final_snapshot_only = status == "FINAL_SNAPSHOT_ONLY" and not snapshot_path
    states = [
        _build_state(record, snapshots, theme_source_mode=theme_source_mode, final_snapshot_only=final_snapshot_only)
        for record in records
    ]
    source_mode = _source_mode(states)
    failures = [source for source in sources if source.get("status") == "failed"]
    data_quality = _data_quality(
        status, states, failures, final_snapshot_only=final_snapshot_only,
        snapshots=snapshots, snapshot_file=bool(snapshot_path),
    )
    watchlist = _build_watchlist(states)
    payload = {
        "phase": "short_term_auction_confirmation_v1",
        "market": "cn",
        "target_date": target.strftime("%Y%m%d"),
        "timezone": "Asia/Shanghai",
        "workflow_ready_time": ready_time,
        "auction_status": status,
        "snapshot_mode": "snapshot" if snapshot_path else "live",
        "final_snapshot_only": final_snapshot_only,
        "stage4_source_run_id": stage4_source_run_id or None,
        "stage4_source_date": source_date.strftime("%Y%m%d") if source_date else None,
        "expected_previous_trading_date": expected_previous.strftime("%Y%m%d") if expected_previous else None,
        "source_mode": source_mode,
        "data_quality": data_quality,
        "input_pool_count": len(records),
        "input_pool_meta": input_meta,
        "missed_snapshots": missed_snapshots,
        "snapshot_targets": [f"{hour:02d}:{minute:02d}:{second:02d}" for hour, minute, second in SNAPSHOT_TARGETS],
        "snapshots": [{"timestamp": item.get("timestamp_text"), "stock_count": len(item.get("rows") or [])} for item in snapshots],
        "auction_states": states,
        "auction_watchlist": watchlist,
        "sources": sources,
        "source_failures": failures,
        "api_stats": dict(_API_STATS),
    }
    stage5 = _enrich_stage5(stage4_pool, {item["code"]: item for item in states})
    _write_json(OUTPUT_JSON_PATH, payload)
    _write_json(STAGE5_JSON_PATH, stage5)
    _write_markdown(payload)
    _write_stage5_markdown(stage5)
    logger.info("Wrote stage-5 reports; input=%d watchlist=%d", len(records), len(watchlist))
    return 0


if __name__ == "__main__":
    sys.exit(main())
