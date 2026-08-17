#!/usr/bin/env python3
"""Detect weak-to-strong setups for the next trading day's observation.

This is a close-after-market research layer.  It consumes stage-3 outputs and
does not alter any prior-stage ranking or produce an order/buy signal.
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
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import akshare as ak
import exchange_calendars as xcals
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "short_term"
STAGE3_PATH = REPORT_DIR / "candidate_pool_stage3.json"
THEME_PATH = REPORT_DIR / "theme_leader.json"
SENTIMENT_PATH = REPORT_DIR / "market_sentiment.json"
OUTPUT_JSON_PATH = REPORT_DIR / "weak_to_strong.json"
OUTPUT_MD_PATH = REPORT_DIR / "weak_to_strong.md"
STAGE4_JSON_PATH = REPORT_DIR / "candidate_pool_stage4.json"
STAGE4_MD_PATH = REPORT_DIR / "candidate_pool_stage4.md"

MARKET_TIMEZONE = ZoneInfo("Asia/Shanghai")
FETCH_RETRIES = 3
WEIGHTS = {
    "core_status": 20.0,
    "theme_strength": 15.0,
    "divergence_quality": 20.0,
    "capital_support": 15.0,
    "technical_structure": 10.0,
    "model_resonance": 10.0,
    "next_day_space": 10.0,
}
CORE_SCORES = {"MARKET_LEADER": 20.0, "THEME_LEADER": 17.0, "FRONT_CORE": 14.0, "BROKEN_CORE": 12.0, "FOLLOWER": 5.0, "OBSERVE": 0.0}
THEME_SCORES = {"MAIN": 15.0, "SECONDARY": 11.0, "ROTATION": 6.0, "WEAK": 2.0}
GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}
PHASE_ADJUSTMENTS = {"冰点": -8.0, "修复": 5.0, "启动": 6.0, "发酵": 2.0, "高潮": -6.0, "分歧": 8.0, "退潮": -8.0}
ENVIRONMENT_RULES = {
    "冰点": (2, "只保留极少数市场核心，等待修复确认"),
    "修复": (6, "重点寻找最先修复核心"),
    "启动": (8, "重点观察主线龙头和前排"),
    "发酵": (8, "允许核心分歧转强，回避后排"),
    "高潮": (4, "降低追涨预期，只看核心分歧"),
    "分歧": (8, "适合观察最强主线核心弱转强"),
    "退潮": (2, "大幅降低弱转强预期"),
}

logger = logging.getLogger("short_term_weak_to_strong")
_API_CACHE: dict[str, tuple[list[dict[str, Any]], dict[str, Any]]] = {}
_API_STATS = {"requests": 0, "cache_hits": 0}


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


def _integer(value: Any) -> int | None:
    number = _number(value)
    return int(number) if number is not None else None


def _records(frame: Any) -> list[dict[str, Any]]:
    if isinstance(frame, list):
        return [row for row in frame if isinstance(row, dict)]
    if isinstance(frame, dict):
        return [frame]
    if frame is None:
        return []
    try:
        rows = frame.to_dict(orient="records")
    except Exception:
        return []
    return [row for row in rows if isinstance(row, dict)]


def _row_code(row: dict[str, Any]) -> str:
    return _normalize_code(_first(row, "代码", "股票代码", "证券代码", "code", "symbol", "stock_code"))


def _row_name(row: dict[str, Any]) -> str:
    return str(_first(row, "名称", "股票名称", "name", "stock_name") or "")


def _source_ok(source: dict[str, Any] | None) -> bool:
    return bool(source and source.get("status") == "success")


def _fetch_cached(function: str, **kwargs: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Fetch once per endpoint/parameter tuple, with three independent retries."""
    key = json.dumps([function, kwargs], ensure_ascii=False, sort_keys=True, default=str)
    if key in _API_CACHE:
        _API_STATS["cache_hits"] += 1
        rows, metadata = _API_CACHE[key]
        cached = copy.deepcopy(metadata)
        cached["cache_hit"] = True
        return copy.deepcopy(rows), cached

    _API_STATS["requests"] += 1
    last_error: Exception | None = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            rows = _records(getattr(ak, function)(**kwargs))
            metadata = {"function": function, "status": "success", "rows": len(rows), "attempts": attempt, "params": _json_safe(kwargs)}
            _API_CACHE[key] = (copy.deepcopy(rows), copy.deepcopy(metadata))
            return rows, metadata
        except Exception as exc:  # One endpoint failure must not erase all other data.
            last_error = exc
            if attempt < FETCH_RETRIES:
                time.sleep(min(2 ** (attempt - 1), 4))
    metadata = {
        "function": function,
        "status": "failed",
        "rows": 0,
        "attempts": FETCH_RETRIES,
        "params": _json_safe(kwargs),
        "error": {"type": type(last_error).__name__, "message": str(last_error)},
    }
    _API_CACHE[key] = ([], copy.deepcopy(metadata))
    return [], metadata


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain an object")
    return payload


def _parse_date(raw: Any) -> date | None:
    if not raw:
        return None
    try:
        return datetime.strptime(str(raw), "%Y%m%d").date()
    except ValueError:
        return None


def _target_date(sentiment: dict[str, Any], raw: str | None) -> date:
    for value in (raw, sentiment.get("target_date"), (sentiment.get("current") or {}).get("date")):
        parsed = _parse_date(value)
        if parsed:
            return parsed
    now = datetime.now(MARKET_TIMEZONE)
    target = now.date() - timedelta(days=1 if now.hour < 15 or (now.hour == 15 and now.minute < 5) else 0)
    while target.weekday() >= 5:
        target -= timedelta(days=1)
    return target


def _recent_sessions(target: date, count: int = 5) -> list[date]:
    try:
        calendar = xcals.get_calendar("XSHG")
        start = pd.Timestamp(target - timedelta(days=60))
        end = pd.Timestamp(target)
        sessions = calendar.sessions_in_range(start, end)
        dates = [stamp.date() for stamp in sessions]
        return dates[-count:]
    except Exception:
        dates: list[date] = []
        current = target
        while len(dates) < count:
            if current.weekday() < 5:
                dates.append(current)
            current -= timedelta(days=1)
        return list(reversed(dates))


def _history_row_value(row: dict[str, Any], *keys: str) -> float | None:
    return _number(_first(row, *keys))


def _close_position(close: float | None, low: float | None, high: float | None) -> float | None:
    if close is None or low is None or high is None or high <= low:
        return None
    return max(0.0, min(1.0, (close - low) / (high - low)))


def _history_metrics(rows: list[dict[str, Any]], target: date) -> dict[str, Any]:
    if not rows:
        return {key: None for key in ("open_price", "high_price", "low_price", "close_price", "current_change_pct", "open_pct", "high_pct", "low_pct", "close_pct", "turnover_rate", "amount", "volume_ratio", "close_position", "pct_change_1d", "pct_change_2d", "pct_change_3d", "pct_change_5d", "ma5", "ma10", "bias_ma5", "bias_ma10", "volume_ratio_5d", "max_drawdown_3d", "consecutive_up_days")}

    def row_date(row: dict[str, Any]) -> date | None:
        value = _first(row, "日期", "交易日期", "date")
        if isinstance(value, (datetime, date, pd.Timestamp)):
            return value.date() if hasattr(value, "date") else value
        return _parse_date(str(value).replace("-", ""))

    ordered = sorted(rows, key=lambda row: row_date(row) or date.min)
    current_index = max((index for index, row in enumerate(ordered) if row_date(row) in (target, None)), default=len(ordered) - 1)
    current_index = min(current_index, len(ordered) - 1)
    current = ordered[current_index]
    closes = [_history_row_value(row, "收盘", "close", "close_price") for row in ordered[: current_index + 1]]
    closes = [value for value in closes if value is not None]
    volumes = [_history_row_value(row, "成交量", "volume") for row in ordered[: current_index + 1]]
    volumes = [value for value in volumes if value is not None]
    close = _history_row_value(current, "收盘", "close", "close_price")
    low = _history_row_value(current, "最低", "low", "low_price")
    high = _history_row_value(current, "最高", "high", "high_price")
    previous_close = _history_row_value(ordered[current_index - 1], "收盘", "close", "close_price") if current_index >= 1 else None
    open_price = _history_row_value(current, "开盘", "open", "open_price")
    change = _history_row_value(current, "涨跌幅", "涨跌幅(%)", "change_pct")
    change = change if change is not None else ((close / previous_close - 1) * 100 if close is not None and previous_close else None)

    def period_change(days: int) -> float | None:
        if close is None or len(closes) <= days:
            return None
        base = closes[-days - 1]
        return (close / base - 1) * 100 if base else None

    ma5 = sum(closes[-5:]) / 5 if len(closes) >= 5 else None
    ma10 = sum(closes[-10:]) / 10 if len(closes) >= 10 else None
    prior_volumes = volumes[-6:-1] if len(volumes) >= 6 else []
    volume_ratio_5d = volumes[-1] / (sum(prior_volumes) / len(prior_volumes)) if prior_volumes and volumes[-1] is not None and sum(prior_volumes) else None
    last_three = closes[-3:] if len(closes) >= 3 else []
    max_drawdown = (close / max(last_three) - 1) * 100 if close is not None and last_three and max(last_three) else None
    consecutive = 0
    for row in reversed(ordered[: current_index + 1]):
        value = _history_row_value(row, "涨跌幅", "涨跌幅(%)", "change_pct")
        if value is None:
            break
        if value > 0:
            consecutive += 1
        else:
            break
    return {
        "open_price": open_price,
        "high_price": high,
        "low_price": low,
        "close_price": close,
        "current_change_pct": change,
        "open_pct": (open_price / previous_close - 1) * 100 if open_price is not None and previous_close else None,
        "high_pct": (high / previous_close - 1) * 100 if high is not None and previous_close else None,
        "low_pct": (low / previous_close - 1) * 100 if low is not None and previous_close else None,
        "close_pct": (close / previous_close - 1) * 100 if close is not None and previous_close else None,
        "turnover_rate": _history_row_value(current, "换手率", "turnover_rate"),
        "amount": _history_row_value(current, "成交额", "amount"),
        "volume_ratio": _history_row_value(current, "量比", "volume_ratio"),
        "close_position": _close_position(close, low, high),
        "pct_change_1d": period_change(1),
        "pct_change_2d": period_change(2),
        "pct_change_3d": period_change(3),
        "pct_change_5d": period_change(5),
        "ma5": ma5,
        "ma10": ma10,
        "bias_ma5": (close / ma5 - 1) * 100 if close is not None and ma5 else None,
        "bias_ma10": (close / ma10 - 1) * 100 if close is not None and ma10 else None,
        "volume_ratio_5d": volume_ratio_5d,
        "max_drawdown_3d": max_drawdown,
        "consecutive_up_days": consecutive,
    }


def _fetch_stock_history(code: str, target: date, sources: list[dict[str, Any]]) -> dict[str, Any]:
    rows, source = _fetch_cached(
        "stock_zh_a_hist",
        symbol=code,
        period="daily",
        start_date=(target - timedelta(days=30)).strftime("%Y%m%d"),
        end_date=target.strftime("%Y%m%d"),
        adjust="qfq",
    )
    sources.append(source)
    metrics = _history_metrics(rows, target) if _source_ok(source) else _history_metrics([], target)
    metrics["history_data_available"] = _source_ok(source)
    return metrics


def _fetch_recent_pools(target: date, codes: set[str], sources: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, bool]]:
    limit_map: dict[str, dict[str, Any]] = {}
    broken_map: dict[str, dict[str, Any]] = {}
    down_map: dict[str, dict[str, Any]] = {}
    availability: dict[str, bool] = {}
    for session in _recent_sessions(target, 5):
        text = session.strftime("%Y%m%d")
        up_rows, up_source = _fetch_cached("stock_zt_pool_em", date=text)
        broken_rows, broken_source = _fetch_cached("stock_zt_pool_zbgc_em", date=text)
        down_rows, down_source = _fetch_cached("stock_zt_pool_dtgc_em", date=text)
        sources.extend([up_source, broken_source, down_source])
        availability[f"limit_up_{text}"] = _source_ok(up_source)
        availability[f"broken_board_{text}"] = _source_ok(broken_source)
        availability[f"limit_down_{text}"] = _source_ok(down_source)
        if session == target:
            for row in up_rows:
                if _row_code(row) in codes:
                    limit_map[_row_code(row)] = row
            for row in broken_rows:
                if _row_code(row) in codes:
                    broken_map[_row_code(row)] = row
            for row in down_rows:
                if _row_code(row) in codes:
                    down_map[_row_code(row)] = row
    return limit_map, broken_map, down_map, availability


def _recent_counts(code: str, target: date, sources: list[dict[str, Any]]) -> tuple[int | None, int | None]:
    up_count = 0
    broken_count = 0
    saw_up = saw_broken = False
    for session in _recent_sessions(target, 5):
        text = session.strftime("%Y%m%d")
        up_rows, up_source = _fetch_cached("stock_zt_pool_em", date=text)
        broken_rows, broken_source = _fetch_cached("stock_zt_pool_zbgc_em", date=text)
        sources.extend([up_source, broken_source])
        if _source_ok(up_source):
            saw_up = True
            up_count += sum(_row_code(row) == code for row in up_rows)
        if _source_ok(broken_source):
            saw_broken = True
            broken_count += sum(_row_code(row) == code for row in broken_rows)
    return (up_count if saw_up else None, broken_count if saw_broken else None)


def _stage3_stock_maps(stage3: dict[str, Any], theme: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    records: dict[str, dict[str, Any]] = {}
    candidates = [item for item in stage3.get("candidates", []) if isinstance(item, dict)]
    for item in candidates:
        code = _normalize_code(item.get("code"))
        if not code:
            continue
        analysis = item.get("theme_analysis") or {}
        ecology = item.get("market_ecology") or {}
        records[code] = {
            "code": code,
            "name": item.get("name") or "",
            "primary_theme": analysis.get("primary_theme"),
            "primary_theme_rank": analysis.get("primary_theme_rank"),
            "primary_theme_score": analysis.get("primary_theme_score"),
            "primary_theme_role": analysis.get("primary_theme_role"),
            "stock_role": analysis.get("stock_role") or "OBSERVE",
            "leader_score": analysis.get("leader_score"),
            "market_leader_rank": analysis.get("market_leader_rank"),
            "resonance_count": item.get("resonance_count"),
            "is_limit_up": ecology.get("is_limit_up"),
            "is_broken_board": ecology.get("is_broken_board"),
            "is_limit_down": ecology.get("is_limit_down"),
            "board_count": ecology.get("board_count"),
            "break_count": ecology.get("break_count"),
            "themes": item.get("themes") or [],
            "candidate": True,
        }
    for item in theme.get("leaders", []) or []:
        if not isinstance(item, dict):
            continue
        code = _normalize_code(item.get("code"))
        if not code:
            continue
        record = records.setdefault(code, {"code": code, "candidate": False, "themes": item.get("themes") or []})
        for key in ("name", "primary_theme", "primary_theme_rank", "primary_theme_role", "stock_role", "leader_score", "market_leader_rank", "resonance_count", "is_limit_up", "is_broken_board", "is_limit_down", "board_count", "break_count", "themes"):
            if item.get(key) is not None:
                record[key] = item.get(key)
        record["candidate"] = bool(record.get("candidate"))
    return records, candidates


def _weak_signals(stock: dict[str, Any]) -> list[str]:
    signals: list[str] = []
    if stock.get("is_broken_board") is True:
        signals.append("BROKEN_BOARD")
    change = _number(stock.get("current_change_pct"))
    high = _number(stock.get("high_pct"))
    open_pct = _number(stock.get("open_pct"))
    close_position = _number(stock.get("close_position"))
    if (_number(stock.get("recent_limit_up_count")) or 0) > 0 and change is not None and change <= -2:
        signals.append("POST_LIMIT_DIVERGENCE")
    if high is not None and change is not None and high >= 5 and high - change >= 5:
        signals.append("HIGH_TO_LOW")
    if open_pct is not None and change is not None and open_pct >= 2 and open_pct - change >= 3:
        signals.append("GAP_UP_FADE")
    board = _number(stock.get("board_count"))
    if board is not None and board >= 2 and stock.get("is_limit_up") is False:
        signals.append("BOARD_BREAK")
    if change is not None and change < 0 and (_number(stock.get("recent_limit_up_count")) or 0) > 0 and (_number(stock.get("pct_change_5d")) or 0) > 8:
        signals.append("FIRST_STRONG_PULLBACK")
    if high is not None and change is not None and high - change >= 4 and close_position is not None and close_position < 0.5:
        signals.append("LATE_DIVERGENCE")
    role = stock.get("stock_role")
    if role in {"MARKET_LEADER", "THEME_LEADER", "FRONT_CORE", "BROKEN_CORE"} and signals and "HIGH_TO_LOW" in signals:
        signals.append("MAIN_CORE_PULLBACK")
    return list(dict.fromkeys(signals))


def _strength_foundation(stock: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if stock.get("primary_theme_role") in {"MAIN", "SECONDARY"}:
        reasons.append(f"{stock.get('primary_theme_role')}题材")
    if stock.get("stock_role") in {"MARKET_LEADER", "THEME_LEADER", "FRONT_CORE"}:
        reasons.append(str(stock.get("stock_role")))
    if _number(stock.get("hot_rank")) is not None and stock.get("hot_rank") <= 20:
        reasons.append("人气榜前20")
    if (_number(stock.get("board_count")) or 0) >= 2:
        reasons.append("具备连板高度")
    if (_number(stock.get("resonance_count")) or 0) >= 2:
        reasons.append("四模型多重共振")
    amount = _number(stock.get("amount"))
    if amount is not None and amount >= 1e8:
        reasons.append("成交额达到1亿元")
    bias5 = _number(stock.get("bias_ma5"))
    bias10 = _number(stock.get("bias_ma10"))
    if (bias5 is not None and abs(bias5) <= 5) or (bias10 is not None and abs(bias10) <= 8):
        reasons.append("仍在MA5/MA10附近")
    return reasons


def _score_components(stock: dict[str, Any]) -> dict[str, float | None]:
    role = stock.get("stock_role")
    theme_role = stock.get("primary_theme_role")
    core_status = CORE_SCORES.get(role)
    theme_strength = THEME_SCORES.get(theme_role)
    signals = stock.get("weak_signals") or []
    close_position = _number(stock.get("close_position"))
    max_drawdown = _number(stock.get("max_drawdown_3d"))
    bias10 = _number(stock.get("bias_ma10"))
    if not signals:
        divergence_quality = None
    else:
        divergence_quality = 10.0
        if "BROKEN_BOARD" in signals and close_position is not None and close_position >= 0.5:
            divergence_quality += 5
        if "FIRST_STRONG_PULLBACK" in signals:
            divergence_quality += 4
        if "HIGH_TO_LOW" in signals and close_position is not None and close_position >= 0.4:
            divergence_quality += 3
        if max_drawdown is not None and max_drawdown <= -15:
            divergence_quality -= 8
        if bias10 is not None and bias10 <= -8:
            divergence_quality -= 5
        divergence_quality = max(0.0, min(20.0, divergence_quality))

    capital_parts: list[float] = []
    turnover = _number(stock.get("turnover_rate"))
    if turnover is not None:
        capital_parts.append(max(0.0, min(5.0, turnover / 10 * 5)))
    if close_position is not None:
        capital_parts.append(close_position * 5)
    volume_ratio = _number(stock.get("volume_ratio_5d"))
    if volume_ratio is not None:
        capital_parts.append(max(0.0, min(5.0, volume_ratio / 2 * 5)))
    capital_support = sum(capital_parts) / len(capital_parts) * 3 if capital_parts else None

    technical_parts: list[float] = []
    if bias10 is not None:
        technical_parts.append(max(0.0, 5 - abs(bias10) / 5))
    bias5 = _number(stock.get("bias_ma5"))
    if bias5 is not None:
        technical_parts.append(max(0.0, 5 - abs(bias5) / 5))
    technical_structure = sum(technical_parts) if technical_parts else None

    resonance = _number(stock.get("resonance_count"))
    model_resonance = max(0.0, min(10.0, resonance / 4 * 10)) if resonance is not None else None

    space_parts: list[float] = []
    if _number(stock.get("board_count")) is not None:
        space_parts.append(max(0.0, 10 - (_number(stock.get("board_count")) or 0) * 1.2))
    if _number(stock.get("pct_change_5d")) is not None:
        space_parts.append(max(0.0, min(10.0, 10 - max(0.0, (_number(stock.get("pct_change_5d")) or 0) - 15) / 3)))
    next_day_space = sum(space_parts) / len(space_parts) if space_parts else None
    return {
        "core_status": core_status,
        "theme_strength": theme_strength,
        "divergence_quality": divergence_quality,
        "capital_support": capital_support,
        "technical_structure": technical_structure,
        "model_resonance": model_resonance,
        "next_day_space": next_day_space,
    }


def _weighted_score(components: dict[str, float | None]) -> dict[str, Any]:
    available = {key: value for key, value in components.items() if value is not None}
    raw = round(sum(float(value) for value in available.values()), 4) if available else None
    available_weight = round(sum(WEIGHTS[key] for key in available), 4)
    normalized = round(raw / available_weight * 100, 4) if raw is not None and available_weight else None
    return {"score_raw": raw, "available_weight": available_weight, "data_quality": "complete" if len(available) == len(WEIGHTS) else "partial" if available else "unavailable", "weak_to_strong_score": normalized, "score_components": {key: (round(float(value), 4) if value is not None else None) for key, value in components.items()}}


def _risk_penalties(stock: dict[str, Any]) -> dict[str, float]:
    risks: dict[str, float] = {}
    if stock.get("is_limit_down") is True or (_number(stock.get("current_change_pct")) is not None and _number(stock.get("current_change_pct")) <= -9.5):
        risks["LIMIT_DOWN"] = 30.0
    drawdown = _number(stock.get("max_drawdown_3d"))
    pct5 = _number(stock.get("pct_change_5d"))
    if drawdown is not None and drawdown <= -25 and pct5 is not None and pct5 <= -20:
        risks["A_SHAPE"] = 25.0
    if _number(stock.get("bias_ma10")) is not None and (_number(stock.get("bias_ma10")) or 0) <= -8:
        risks["BROKEN_TREND"] = 15.0
    if pct5 is not None and pct5 >= 35:
        risks["OVER_EXTENDED"] = 10.0
    if stock.get("is_broken_board") is True and (_number(stock.get("break_count")) or 0) >= 3 and (_number(stock.get("board_count")) or 0) >= 4:
        risks["HIGH_POSITION_EXPLOSION"] = 12.0
    if stock.get("stock_role") in {"FOLLOWER", "OBSERVE"} and stock.get("primary_theme_role") not in {"MAIN", "SECONDARY"}:
        risks["FOLLOWER_ONLY"] = 12.0
    if stock.get("primary_theme_role") == "WEAK":
        risks["WEAK_THEME"] = 10.0
    if pct5 is not None and pct5 <= -12:
        risks["MULTI_DAY_DECLINE"] = 15.0
    return risks


def _setup_type(stock: dict[str, Any]) -> str:
    signals = set(stock.get("weak_signals") or [])
    role = stock.get("stock_role")
    if not signals:
        return "NONE"
    if "BROKEN_BOARD" in signals:
        return "BROKEN_BOARD_RECOVERY"
    if "BOARD_BREAK" in signals:
        return "BOARD_BREAK_RECOVERY"
    if "FIRST_STRONG_PULLBACK" in signals:
        return "FIRST_PULLBACK"
    if role in {"MARKET_LEADER", "THEME_LEADER"}:
        return "LEADER_DIVERGENCE"
    if stock.get("primary_theme_role") in {"MAIN", "SECONDARY"}:
        return "THEME_CORE_DIVERGENCE"
    return "TREND_CORE_PULLBACK"


def _grade(score: float | None, risks: dict[str, float], stock: dict[str, Any]) -> str:
    if score is None:
        return "D"
    grade = "A" if score >= 75 else "B" if score >= 65 else "C" if score >= 55 else "D"
    if "LIMIT_DOWN" in risks or "A_SHAPE" in risks:
        return "D"
    if any(key in risks for key in ("BROKEN_TREND", "FOLLOWER_ONLY", "WEAK_THEME", "MULTI_DAY_DECLINE")):
        grade = min(grade, "C", key=lambda value: GRADE_ORDER[value])
    return grade


def _tomorrow_plan(stock: dict[str, Any], phase: str | None) -> dict[str, Any] | None:
    if stock.get("setup_grade") not in {"A", "B"}:
        return None
    close = _number(stock.get("close_price"))
    high = _number(stock.get("high_price"))
    low = _number(stock.get("low_price"))
    return {
        "must_confirm": [
            "集合竞价不能明显低于预期",
            "所属主线不能明显转弱",
            "开盘后必须快速收复昨日关键价位",
        ],
        "invalid_conditions": [
            "竞价或开盘后跌破结构性失效价",
            "主线题材明显退潮",
            "市场情绪进入退潮且个股没有绝对核心地位",
        ],
        "max_acceptable_gap_down_pct": -2.0,
        "ideal_gap_min_pct": -0.5,
        "ideal_gap_max_pct": 3.0,
        "need_theme_strength": stock.get("primary_theme_role") in {"MAIN", "SECONDARY"},
        "need_market_sentiment_not_retreat": phase != "退潮",
        "key_price_reference": close,
        "breakout_reference": high,
        "invalid_below_price": low if low is not None else close,
        "is_observation_condition_only": True,
    }


def _build_environment(sentiment: dict[str, Any], max_size_override: int | None = None) -> dict[str, Any]:
    current = sentiment.get("current") or {}
    phase = current.get("sentiment_phase")
    max_size, label = ENVIRONMENT_RULES.get(phase, (3, "情绪数据不足，仅作少量观察"))
    score = _number(current.get("sentiment_score"))
    return {"sentiment_phase": phase, "environment_score": score, "environment_label": label, "max_watchlist_size": max_size_override or max_size}


def _build_state(record: dict[str, Any], history: dict[str, Any], recent_up: int | None, recent_broken: int | None, phase: str | None) -> dict[str, Any]:
    state = copy.deepcopy(record)
    state.update(history)
    state["recent_limit_up_count"] = recent_up
    state["recent_broken_board_count"] = recent_broken
    state["weak_signals"] = _weak_signals(state)
    state["strength_foundation"] = _strength_foundation(state)
    state["setup_type"] = _setup_type(state)
    components = _score_components(state)
    score_details = _weighted_score(components)
    state.update(score_details)
    risks = _risk_penalties(state)
    state["risk_penalties"] = risks
    state["risk_penalty_total"] = round(sum(risks.values()), 4)
    base = state.get("weak_to_strong_score")
    adjustment = PHASE_ADJUSTMENTS.get(phase or "", 0.0) if base is not None else None
    state["sentiment_adjustment"] = adjustment
    final = max(0.0, min(100.0, base - state["risk_penalty_total"] + (adjustment or 0))) if base is not None else None
    state["final_weak_to_strong_score"] = round(final, 4) if final is not None else None
    state["setup_grade"] = _grade(state["final_weak_to_strong_score"], risks, state)
    state["tomorrow_plan"] = _tomorrow_plan(state, phase)
    return state


def _watchlist(states: list[dict[str, Any]], environment: dict[str, Any]) -> list[dict[str, Any]]:
    eligible_roles = {"MARKET_LEADER", "THEME_LEADER", "FRONT_CORE", "BROKEN_CORE"}
    candidates = [
        item
        for item in states
        if item.get("setup_grade") in {"A", "B", "C"}
        and item.get("setup_type") != "NONE"
        and item.get("final_weak_to_strong_score") is not None
        and item.get("stock_role") in eligible_roles
    ]
    candidates.sort(key=lambda item: (GRADE_ORDER[item.get("setup_grade", "D")], -(item.get("final_weak_to_strong_score") or 0), item.get("market_leader_rank") if item.get("market_leader_rank") is not None else 999, item.get("primary_theme_rank") if item.get("primary_theme_rank") is not None else 999, -(item.get("leader_score") or 0), item.get("code", "")))
    result: list[dict[str, Any]] = []
    for rank, item in enumerate(candidates[: int(environment.get("max_watchlist_size") or 10)], start=1):
        result.append({key: item.get(key) for key in ("code", "name", "setup_grade", "setup_type", "final_weak_to_strong_score", "primary_theme", "primary_theme_role", "stock_role", "leader_score", "weak_signals", "strength_foundation", "risk_penalties", "tomorrow_plan")})
        result[-1]["rank"] = rank
    return result[:10]


def _enrich_stage4(stage3: dict[str, Any], states: dict[str, dict[str, Any]], watchlist: list[dict[str, Any]]) -> dict[str, Any]:
    result = copy.deepcopy(stage3)
    ranks = {item.get("code"): item.get("rank") for item in watchlist}
    output: list[Any] = []
    for original in stage3.get("candidates", []) or []:
        if not isinstance(original, dict):
            output.append(original)
            continue
        item = copy.deepcopy(original)
        state = states.get(_normalize_code(item.get("code")), {})
        item["weak_to_strong_analysis"] = {
            "weak_to_strong_score": state.get("weak_to_strong_score"),
            "risk_penalty_total": state.get("risk_penalty_total"),
            "final_weak_to_strong_score": state.get("final_weak_to_strong_score"),
            "setup_grade": state.get("setup_grade", "D"),
            "setup_type": state.get("setup_type", "NONE"),
            "weak_signals": state.get("weak_signals", []),
            "strength_foundation": state.get("strength_foundation", []),
            "sentiment_adjustment": state.get("sentiment_adjustment"),
            "tomorrow_plan": state.get("tomorrow_plan"),
            "next_day_watchlist_rank": ranks.get(_normalize_code(item.get("code"))),
        }
        output.append(item)
    result["candidates"] = output
    result["stage"] = "short_term_weak_to_strong_v1"
    return result


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_markdown(payload: dict[str, Any]) -> None:
    environment = payload.get("weak_to_strong_environment") or {}
    lines = [
        "# 《A股短线弱转强识别与次日观察预案（改造第4阶段）》",
        "",
        "> 次日弱转强观察池 ≠ 买入名单。真正买入资格必须等第5阶段集合竞价确认 + 第6阶段开盘确认。",
        "",
        "## 市场环境",
        "",
        f"- 情绪阶段：`{_display(environment.get('sentiment_phase'))}`",
        f"- 环境分数：`{_display(environment.get('environment_score'))}`",
        f"- 环境判断：`{_display(environment.get('environment_label'))}`",
        f"- 最大观察数量：`{_display(environment.get('max_watchlist_size'))}`",
        "",
        "## 次日弱转强观察池",
        "",
        "| 排名 | 代码 | 名称 | 等级 | 类型 | 最终分 | 题材 | 角色 | 龙头分 | 风险 |",
        "| ---: | --- | --- | --- | --- | ---: | --- | --- | ---: | --- |",
    ]
    for item in payload.get("next_day_watchlist", []) or []:
        lines.append(f"| {_display(item.get('rank'))} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(item.get('setup_grade'))} | {_display(item.get('setup_type'))} | {_display(item.get('final_weak_to_strong_score'))} | {_display(item.get('primary_theme'))} | {_display(item.get('stock_role'))} | {_display(item.get('leader_score'))} | {_display(item.get('risk_penalties'))} |")
    lines.extend(["", "## 全部弱转强状态", "", "| 代码 | 名称 | 弱信号 | 基础分 | 风险扣分 | 最终分 | 等级 | 类型 | 数据质量 |", "| --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |"])
    for item in payload.get("weak_to_strong_states", []) or []:
        lines.append(f"| {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(item.get('weak_signals'))} | {_display(item.get('weak_to_strong_score'))} | {_display(item.get('risk_penalty_total'))} | {_display(item.get('final_weak_to_strong_score'))} | {_display(item.get('setup_grade'))} | {_display(item.get('setup_type'))} | {_display(item.get('data_quality'))} |")
    lines.extend(["", "## 说明", "", "所有 tomorrow_plan 仅是次日观察条件，不是自动买入条件；集合竞价和开盘确认留到后续阶段。", "", f"API请求次数：`{_display(payload.get('api_stats', {}).get('requests'))}`；缓存命中次数：`{_display(payload.get('api_stats', {}).get('cache_hits'))}`。", ""])
    OUTPUT_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def _write_stage4_markdown(payload: dict[str, Any]) -> None:
    lines = ["# A股短线候选池（改造第4阶段）", "", "> 保持第1阶段候选池原始顺序，仅增加弱转强分析字段。", "", "| 原排名 | 代码 | 名称 | 最终分 | 等级 | 类型 | 观察池排名 |", "| ---: | --- | --- | ---: | --- | --- | ---: |"]
    for index, item in enumerate(payload.get("candidates", []) or [], start=1):
        if not isinstance(item, dict):
            continue
        analysis = item.get("weak_to_strong_analysis") or {}
        lines.append(f"| {index} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(analysis.get('final_weak_to_strong_score'))} | {_display(analysis.get('setup_grade'))} | {_display(analysis.get('setup_type'))} | {_display(analysis.get('next_day_watchlist_rank'))} |")
    STAGE4_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stage-4 weak-to-strong observation reports.")
    parser.add_argument("--target-date", default=os.getenv("SHORT_TERM_SENTIMENT_DATE", ""), help="Target date in YYYYMMDD.")
    return parser.parse_args()


def main() -> int:
    _configure_logging()
    args = _parse_args()
    try:
        stage3 = _load_json(STAGE3_PATH)
        theme = _load_json(THEME_PATH)
        sentiment = _load_json(SENTIMENT_PATH)
    except Exception:
        logger.exception("Cannot load stage-3 inputs")
        return 1
    target = _target_date(sentiment, args.target_date)
    records, original_candidates = _stage3_stock_maps(stage3, theme)
    codes = set(records)
    sources: list[dict[str, Any]] = []
    limit_map, broken_map, down_map, _ = _fetch_recent_pools(target, codes, sources)
    current_date_text = target.strftime("%Y%m%d")
    current_up_source = next((source for source in sources if source.get("function") == "stock_zt_pool_em" and source.get("params", {}).get("date") == current_date_text), None)
    current_broken_source = next((source for source in sources if source.get("function") == "stock_zt_pool_zbgc_em" and source.get("params", {}).get("date") == current_date_text), None)
    current_down_source = next((source for source in sources if source.get("function") == "stock_zt_pool_dtgc_em" and source.get("params", {}).get("date") == current_date_text), None)
    for code, record in records.items():
        if _source_ok(current_up_source):
            record["is_limit_up"] = code in limit_map
        elif record.get("is_limit_up") is None:
            record["is_limit_up"] = None
        if _source_ok(current_broken_source):
            record["is_broken_board"] = code in broken_map
        elif record.get("is_broken_board") is None:
            record["is_broken_board"] = None
        if _source_ok(current_down_source):
            record["is_limit_down"] = code in down_map
        elif record.get("is_limit_down") is None:
            record["is_limit_down"] = None
        if code in limit_map:
            record["board_count"] = _integer(_first(limit_map[code], "连板数", "连板", "板数")) or record.get("board_count")
            record["break_count"] = _integer(_first(limit_map[code], "炸板次数", "break_count")) if _first(limit_map[code], "炸板次数", "break_count") is not None else record.get("break_count")
    states: list[dict[str, Any]] = []
    phase = (sentiment.get("current") or {}).get("sentiment_phase")
    for code, record in records.items():
        history = _fetch_stock_history(code, target, sources)
        recent_up, recent_broken = _recent_counts(code, target, sources)
        record.update(history)
        record["weak_signals"] = []
        state = _build_state(record, history, recent_up, recent_broken, phase)
        states.append(state)
    environment = _build_environment(sentiment)
    watchlist = _watchlist(states, environment)
    watch_codes = {item.get("code") for item in watchlist}
    for state in states:
        state["next_day_watchlist_rank"] = next((item.get("rank") for item in watchlist if item.get("code") == state.get("code")), None)
        if state.get("setup_grade") in {"A", "B"}:
            state["tomorrow_plan"] = _tomorrow_plan(state, phase)
        elif state.get("code") not in watch_codes:
            state["tomorrow_plan"] = None
    failures = [source for source in sources if source.get("status") == "failed"]
    payload = {
        "phase": "short_term_weak_to_strong_v1",
        "market": "cn",
        "target_date": target.strftime("%Y%m%d"),
        "weak_to_strong_environment": environment,
        "weak_to_strong_states": states,
        "next_day_watchlist": watchlist,
        "sources": sources,
        "source_failures": failures,
        "api_stats": dict(_API_STATS),
        "data_quality": "failed" if sources and len(failures) == len(sources) else "partial" if failures else "complete",
    }
    stage4 = _enrich_stage4(stage3, {item["code"]: item for item in states}, watchlist)
    stage4["weak_to_strong_environment"] = environment
    stage4["source_failures"] = failures
    _write_json(OUTPUT_JSON_PATH, payload)
    _write_json(STAGE4_JSON_PATH, stage4)
    _write_markdown(payload)
    _write_stage4_markdown(stage4)
    logger.info("AKShare API requests=%d cache_hits=%d", _API_STATS["requests"], _API_STATS["cache_hits"])
    logger.info("Wrote stage-4 reports for %s", target.strftime("%Y%m%d"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
