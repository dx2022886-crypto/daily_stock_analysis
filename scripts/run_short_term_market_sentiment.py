#!/usr/bin/env python3
"""Build the stage-2 A-share market sentiment and limit-up ecology report.

This script is intentionally independent from the original screening engine.
It reads the stage-1 candidate pool only to add ecology labels and never sorts
or scores those candidates again.
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
from typing import Any, Callable
from zoneinfo import ZoneInfo

import akshare as ak
import exchange_calendars as xcals
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "short_term"
SENTIMENT_JSON_PATH = REPORT_DIR / "market_sentiment.json"
SENTIMENT_MARKDOWN_PATH = REPORT_DIR / "market_sentiment.md"
CANDIDATE_POOL_PATH = REPORT_DIR / "candidate_pool.json"
ENRICHED_JSON_PATH = REPORT_DIR / "candidate_pool_enriched.json"
ENRICHED_MARKDOWN_PATH = REPORT_DIR / "candidate_pool_enriched.md"

MARKET_TIMEZONE = ZoneInfo("Asia/Shanghai")
SESSION_CLOSE_HOUR = 15
SESSION_CLOSE_MINUTE = 5
MAX_HISTORY_DAYS = 10
FETCH_RETRIES = 3

logger = logging.getLogger("short_term_market_sentiment")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
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


def _positive_int(raw: str | None, *, name: str, default: int, maximum: int | None = None) -> int:
    value = raw if raw not in (None, "") else str(default)
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be an integer, got {value!r}") from exc
    if parsed < 1:
        raise ValueError(f"{name} must be at least 1")
    if maximum is not None and parsed > maximum:
        raise ValueError(f"{name} must be at most {maximum}")
    return parsed


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stage-2 A-share market sentiment and limit-up ecology.")
    parser.add_argument(
        "--target-date",
        default=os.getenv("SHORT_TERM_SENTIMENT_DATE", "").strip(),
        help="Target date in YYYYMMDD format; empty means latest completed XSHG session.",
    )
    parser.add_argument(
        "--history-days",
        type=int,
        default=_positive_int(
            os.getenv("SHORT_TERM_SENTIMENT_HISTORY_DAYS"),
            name="SHORT_TERM_SENTIMENT_HISTORY_DAYS",
            default=5,
            maximum=MAX_HISTORY_DAYS,
        ),
        help="Number of completed sessions in the report history (default: 5).",
    )
    args = parser.parse_args()
    if args.history_days < 1 or args.history_days > MAX_HISTORY_DAYS:
        parser.error(f"--history-days must be between 1 and {MAX_HISTORY_DAYS}")
    return args


def _calendar() -> Any:
    return xcals.get_calendar("XSHG")


def _is_session(cal: Any, value: date) -> bool:
    return bool(cal.is_session(value))


def _previous_session(cal: Any, value: date) -> date:
    session = cal.date_to_session(value, direction="previous")
    return cal.previous_session(session).date()


def _nearest_completed_session(now: datetime | None = None) -> date:
    """Resolve the latest completed XSHG session using the 15:05 cutoff."""
    cal = _calendar()
    market_now = now.astimezone(MARKET_TIMEZONE) if now and now.tzinfo else (now or datetime.now(MARKET_TIMEZONE))
    if market_now.tzinfo is None:
        market_now = market_now.replace(tzinfo=MARKET_TIMEZONE)
    today = market_now.date()
    if _is_session(cal, today) and (
        market_now.hour > SESSION_CLOSE_HOUR
        or (market_now.hour == SESSION_CLOSE_HOUR and market_now.minute >= SESSION_CLOSE_MINUTE)
    ):
        return today
    if _is_session(cal, today):
        return _previous_session(cal, today)
    return cal.date_to_session(today, direction="previous").date()


def _resolve_target_date(raw: str) -> date:
    if not raw:
        return _nearest_completed_session()
    try:
        requested = datetime.strptime(raw, "%Y%m%d").date()
    except ValueError as exc:
        raise ValueError("SHORT_TERM_SENTIMENT_DATE must use YYYYMMDD") from exc

    cal = _calendar()
    today = datetime.now(MARKET_TIMEZONE).date()
    if requested == today:
        return _nearest_completed_session()
    if _is_session(cal, requested):
        return requested
    return cal.date_to_session(requested, direction="previous").date()


def _history_dates(target: date, history_days: int) -> list[date]:
    cal = _calendar()
    end_session = cal.date_to_session(target, direction="previous")
    sessions = [end_session]
    # Use the stable single-session API already used by this repository rather
    # than relying on optional/version-specific ``previous_session_n`` helpers.
    for _ in range(history_days - 1):
        sessions.append(cal.previous_session(sessions[-1]))
    return [session.date() for session in reversed(sessions)]


def _load_dates(target: date, history_days: int) -> tuple[list[date], list[date]]:
    """Return output dates plus one prior session needed for promotion rates."""
    output_dates = _history_dates(target, history_days)
    cal = _calendar()
    first = output_dates[0]
    previous = _previous_session(cal, first)
    return [previous, *output_dates], output_dates


def _normalize_column(value: Any) -> str:
    return re.sub(r"\s+", "", str(value or "").strip().lower())


def _column_name(frame: pd.DataFrame, aliases: tuple[str, ...]) -> Any:
    columns = {_normalize_column(column): column for column in frame.columns}
    for alias in aliases:
        found = columns.get(_normalize_column(alias))
        if found is not None:
            return found
    return None


def _row_value(row: dict[str, Any], aliases: tuple[str, ...]) -> Any:
    normalized = {_normalize_column(key): value for key, value in row.items()}
    for alias in aliases:
        value = normalized.get(_normalize_column(alias))
        if value is not None and not (isinstance(value, float) and math.isnan(value)):
            return value
    return None


def _frame_records(frame: pd.DataFrame | None) -> list[dict[str, Any]]:
    if frame is None or frame.empty:
        return []
    return [_json_safe(record) for record in frame.to_dict(orient="records")]


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        if isinstance(value, str):
            value = value.replace("%", "").replace(",", "").strip()
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _integer(value: Any) -> int | None:
    number = _number(value)
    if number is None:
        match = re.search(r"\d+", str(value or ""))
        if not match:
            return None
        number = float(match.group(0))
    return int(number)


def _normalize_code(value: Any) -> str:
    text = str(value or "").strip().upper().replace(" ", "")
    prefix = re.fullmatch(r"(?:SH|SZ|BJ)(\d{1,6})", text)
    suffix = re.fullmatch(r"(\d{1,6})\.(?:SH|SZ|BJ)", text)
    plain = re.fullmatch(r"\d{1,6}", text)
    digits = prefix.group(1) if prefix else suffix.group(1) if suffix else plain.group(0) if plain else ""
    return digits.zfill(6) if digits else ""


def _code(row: dict[str, Any]) -> str:
    return _normalize_code(_row_value(row, ("代码", "code", "股票代码", "symbol", "stock_code")))


def _name(row: dict[str, Any]) -> str:
    return str(_row_value(row, ("名称", "name", "股票名称", "stock_name")) or "")


def _board_count(row: dict[str, Any]) -> int | None:
    value = _row_value(row, ("连板数", "连续涨停天数", "连板天数", "board_count", "板数"))
    parsed = _integer(value)
    # The endpoint represents a limit-up stock; if an old AKShare schema omits
    # the board column, treating it as first board preserves the ladder row.
    return parsed if parsed is not None else 1


def _stock_detail(row: dict[str, Any], *, board_count: int | None = None) -> dict[str, Any]:
    return {
        "code": _code(row),
        "name": _name(row),
        "board_count": board_count if board_count is not None else _board_count(row),
        "first_limit_time": _row_value(row, ("首次封板时间", "首次涨停时间", "first_limit_time")),
        "last_limit_time": _row_value(row, ("最后封板时间", "最后涨停时间", "last_limit_time")),
        "break_count": _integer(_row_value(row, ("炸板次数", "break_count"))),
        "industry": _row_value(row, ("所属行业", "行业", "industry")),
    }


def _fetch_source(function_name: str, target_date: date) -> tuple[pd.DataFrame | None, dict[str, Any]]:
    metadata: dict[str, Any] = {
        "function": function_name,
        "date": target_date.strftime("%Y%m%d"),
        "status": "failed",
        "rows": 0,
        "attempts": 0,
    }
    last_error: Exception | None = None
    function: Callable[..., Any] | None = getattr(ak, function_name, None)
    if function is None:
        error = AttributeError(f"akshare.{function_name} is unavailable")
        metadata["error"] = {"type": type(error).__name__, "message": str(error)}
        return None, metadata

    for attempt in range(1, FETCH_RETRIES + 1):
        metadata["attempts"] = attempt
        try:
            frame = function(date=target_date.strftime("%Y%m%d"))
            if frame is None:
                frame = pd.DataFrame()
            elif not isinstance(frame, pd.DataFrame):
                frame = pd.DataFrame(frame)
            metadata.update({"status": "success", "rows": int(len(frame))})
            return frame, metadata
        except Exception as exc:  # Each endpoint is isolated and retried.
            last_error = exc
            logger.warning("%s failed for %s (attempt %s/%s): %s", function_name, target_date, attempt, FETCH_RETRIES, exc)
            if attempt < FETCH_RETRIES:
                time.sleep(min(attempt, 3))

    assert last_error is not None
    metadata["error"] = {"type": type(last_error).__name__, "message": str(last_error)}
    return None, metadata


def _fetch_day(target_date: date) -> dict[str, Any]:
    functions = {
        "limit_up": "stock_zt_pool_em",
        "broken_board": "stock_zt_pool_zbgc_em",
        "limit_down": "stock_zt_pool_dtgc_em",
        "previous_limit_up": "stock_zt_pool_previous_em",
    }
    frames: dict[str, pd.DataFrame | None] = {}
    sources: list[dict[str, Any]] = []
    for key, function_name in functions.items():
        frame, metadata = _fetch_source(function_name, target_date)
        frames[key] = frame
        sources.append(metadata)
    return {"date": target_date, "frames": frames, "sources": sources}


def _frame_status(day: dict[str, Any], key: str) -> str:
    function_name = {
        "limit_up": "stock_zt_pool_em",
        "broken_board": "stock_zt_pool_zbgc_em",
        "limit_down": "stock_zt_pool_dtgc_em",
        "previous_limit_up": "stock_zt_pool_previous_em",
    }[key]
    for source in day["sources"]:
        if source["function"] == function_name:
            return str(source.get("status"))
    return "failed"


def _records_for(day: dict[str, Any], key: str) -> list[dict[str, Any]]:
    return _frame_records(day["frames"].get(key))


def _limit_up_map(day: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in _records_for(day, "limit_up"):
        code = _code(row)
        if code:
            result[code] = row
    return result


def _previous_change_map(day: dict[str, Any]) -> dict[str, float | None]:
    result: dict[str, float | None] = {}
    for row in _records_for(day, "previous_limit_up"):
        code = _code(row)
        if code:
            result[code] = _number(_row_value(row, ("涨跌幅", "涨跌幅(%)", "change_pct", "今日涨跌幅")))
    return result


def _promotion_rates(previous_day: dict[str, Any] | None, current_day: dict[str, Any]) -> dict[str, dict[str, Any] | None]:
    empty = {
        "1_to_2": {"eligible": 0, "promoted": 0, "rate": 0.0},
        "2_to_3": {"eligible": 0, "promoted": 0, "rate": 0.0},
        "3_plus": {"eligible": 0, "promoted": 0, "rate": 0.0},
    }
    if previous_day is None or _frame_status(previous_day, "limit_up") == "failed" or _frame_status(current_day, "limit_up") == "failed":
        return {key: None for key in empty}

    previous_map = _limit_up_map(previous_day)
    current_map = _limit_up_map(current_day)
    eligible = {"1_to_2": [], "2_to_3": [], "3_plus": []}
    for code, row in previous_map.items():
        board = _board_count(row)
        if board == 1:
            eligible["1_to_2"].append((code, board))
        elif board == 2:
            eligible["2_to_3"].append((code, board))
        elif board is not None and board >= 3:
            eligible["3_plus"].append((code, board))

    output: dict[str, dict[str, Any]] = {}
    for key, rows in eligible.items():
        promoted = 0
        for code, previous_board in rows:
            current_board = _board_count(current_map[code]) if code in current_map else None
            threshold = previous_board + 1 if key == "3_plus" else previous_board + 1
            if current_board is not None and current_board >= threshold:
                promoted += 1
        count = len(rows)
        output[key] = {
            "eligible": count,
            "promoted": promoted,
            "rate": round(promoted / count * 100, 4) if count else 0.0,
        }
    return output


def _ladder(day: dict[str, Any]) -> dict[str, Any]:
    if _frame_status(day, "limit_up") == "failed":
        return {
            "ladder_counts": None,
            "highest_board": None,
            "highest_board_stocks": [],
            "ladder_integrity": None,
            "ladder_missing_levels": None,
        }
    rows = _records_for(day, "limit_up")
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6_plus": 0}
    details: list[dict[str, Any]] = []
    for row in rows:
        board = _board_count(row)
        if board is None or board < 1:
            continue
        key = str(board) if board <= 5 else "6_plus"
        counts[key] += 1
        details.append(_stock_detail(row, board_count=board))
    highest = max((_board_count(row) or 0 for row in rows), default=0)
    highest_stocks = [item for item in details if item.get("board_count") == highest] if highest else []
    present_levels = {level for level in range(1, highest + 1) if any(item.get("board_count") == level for item in details)}
    missing = [level for level in range(1, highest + 1) if level not in present_levels]
    integrity = round(len(present_levels) / highest * 100, 2) if highest else 0.0
    return {
        "ladder_counts": counts,
        "highest_board": highest or 0,
        "highest_board_stocks": highest_stocks,
        "ladder_integrity": integrity,
        "ladder_missing_levels": missing,
    }


def _premium(day: dict[str, Any]) -> dict[str, Any]:
    if _frame_status(day, "previous_limit_up") == "failed":
        return {
            "yesterday_limit_up_count": None,
            "yesterday_premium_mean": None,
            "yesterday_premium_median": None,
            "yesterday_red_rate": None,
        }
    changes = [
        _number(_row_value(row, ("涨跌幅", "涨跌幅(%)", "change_pct", "今日涨跌幅")))
        for row in _records_for(day, "previous_limit_up")
    ]
    changes = [value for value in changes if value is not None]
    return {
        "yesterday_limit_up_count": len(_records_for(day, "previous_limit_up")),
        "yesterday_premium_mean": round(float(pd.Series(changes).mean()), 4) if changes else None,
        "yesterday_premium_median": round(float(pd.Series(changes).median()), 4) if changes else None,
        "yesterday_red_rate": round(sum(value > 0 for value in changes) / len(changes) * 100, 4) if changes else None,
    }


def _day_metrics(previous_day: dict[str, Any] | None, day: dict[str, Any]) -> dict[str, Any]:
    limit_up_count = len(_records_for(day, "limit_up")) if _frame_status(day, "limit_up") == "success" else None
    broken_count = len(_records_for(day, "broken_board")) if _frame_status(day, "broken_board") == "success" else None
    limit_down_count = len(_records_for(day, "limit_down")) if _frame_status(day, "limit_down") == "success" else None
    total_board_events = None if limit_up_count is None or broken_count is None else limit_up_count + broken_count
    broken_rate = None if total_board_events is None else round(broken_count / total_board_events * 100, 4) if total_board_events else 0.0
    ladder = _ladder(day)
    premium = _premium(day)
    promotion = _promotion_rates(previous_day, day)
    return {
        "date": day["date"].strftime("%Y%m%d"),
        "limit_up_count": limit_up_count,
        "limit_down_count": limit_down_count,
        "broken_board_count": broken_count,
        "broken_board_rate": broken_rate,
        **ladder,
        **premium,
        "promotion_rates": promotion,
    }


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _score_components(metrics: dict[str, Any]) -> dict[str, float | None]:
    """Transparent sentiment v1 rules; each line's cap matches the spec.

    - breadth: 80 limit-ups maps to the full 20 points.
    - damage_control: 0 limit-downs is 15 points; 30 or more is 0.
    - seal_quality: 0% broken-board rate is 15 points; 100% is 0.
    - yesterday_premium: -5% maps to 0; +5% or more maps to 15.
    - promotion: the mean of available promotion rates maps to 20 points.
    - ladder: contiguous ladder percentage maps to 15 points.

    A failed source yields None rather than an invented zero.  A successful
    empty dataset is allowed to produce a real zero where the rule calls for it.
    """
    limit_up = _number(metrics.get("limit_up_count"))
    limit_down = _number(metrics.get("limit_down_count"))
    broken_rate = _number(metrics.get("broken_board_rate"))
    premium = _number(metrics.get("yesterday_premium_mean"))
    integrity = _number(metrics.get("ladder_integrity"))
    rates = [
        _number(item.get("rate"))
        for item in (metrics.get("promotion_rates") or {}).values()
        if isinstance(item, dict)
    ]
    rates = [rate for rate in rates if rate is not None]
    return {
        "breadth": round(_clamp(limit_up / 80 * 20, 0, 20), 4) if limit_up is not None else None,
        "damage_control": round(_clamp(15 * (1 - limit_down / 30), 0, 15), 4) if limit_down is not None else None,
        "seal_quality": round(_clamp(15 * (1 - broken_rate / 100), 0, 15), 4) if broken_rate is not None else None,
        "yesterday_premium": round(_clamp((premium + 5) / 10 * 15, 0, 15), 4) if premium is not None else None,
        "promotion": round(_clamp(sum(rates) / len(rates) / 100 * 20, 0, 20), 4) if rates else 0.0,
        "ladder": round(_clamp(integrity / 100 * 15, 0, 15), 4) if integrity is not None else None,
    }


def _sentiment_score(components: dict[str, float | None]) -> float | None:
    if any(value is None for value in components.values()):
        return None
    return round(sum(float(value) for value in components.values()), 4)


PHASES = {
    "ICE_POINT": "冰点",
    "RECOVERY": "修复",
    "START": "启动",
    "FERMENTATION": "发酵",
    "CLIMAX": "高潮",
    "DIVERGENCE": "分歧",
    "RETREAT": "退潮",
    "UNKNOWN": "数据不足",
}


def _sentiment_phase(score: float | None, previous_score: float | None) -> tuple[str, str]:
    if score is None:
        return PHASES["UNKNOWN"], "UNKNOWN"
    if previous_score is not None:
        change = score - previous_score
        # Trend takes precedence over a single absolute score. For example,
        # 60 after 75 is divergence, while 35 after 20 is recovery.
        if score <= 30 and change <= -5:
            return PHASES["ICE_POINT"], "ICE_POINT"
        if change >= 10 and score < 50:
            return PHASES["RECOVERY"], "RECOVERY"
        if change >= 8 and score < 65:
            return PHASES["START"], "START"
        if score >= 85 and change >= 0:
            return PHASES["CLIMAX"], "CLIMAX"
        if score >= 70 and change >= 5:
            return PHASES["FERMENTATION"], "FERMENTATION"
        if change <= -8 and score >= 50:
            return PHASES["DIVERGENCE"], "DIVERGENCE"
        if change <= -5:
            return PHASES["RETREAT"], "RETREAT"
    if score <= 30:
        return PHASES["ICE_POINT"], "ICE_POINT"
    if score <= 45:
        return PHASES["RECOVERY"], "RECOVERY"
    if score <= 60:
        return PHASES["START"], "START"
    if score <= 75:
        return PHASES["FERMENTATION"], "FERMENTATION"
    return PHASES["CLIMAX"], "CLIMAX"


def _build_day_report(previous_day: dict[str, Any] | None, day: dict[str, Any], previous_score: float | None) -> dict[str, Any]:
    metrics = _day_metrics(previous_day, day)
    components = _score_components(metrics)
    score = _sentiment_score(components)
    phase, phase_code = _sentiment_phase(score, previous_score)
    return {
        **metrics,
        "score_components": components,
        "sentiment_score": score,
        "sentiment_phase": phase,
        "sentiment_phase_code": phase_code,
        "sentiment_change": round(score - previous_score, 4) if score is not None and previous_score is not None else None,
    }


def _source_failures(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [source for source in sources if source.get("status") == "failed"]


def _load_candidate_pool(target_date: str, current: dict[str, Any], previous: dict[str, Any] | None) -> tuple[dict[str, Any], str | None]:
    try:
        payload = json.loads(CANDIDATE_POOL_PATH.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("candidate_pool.json must contain an object")
    except Exception as exc:
        payload = {
            "phase": "short_term_candidate_pool_v1",
            "market": "cn",
            "strategies": [],
            "per_strategy_results": None,
            "merged_candidate_count": 0,
            "candidates": [],
        }
        return payload, f"无法读取第1阶段候选池：{type(exc).__name__}: {exc}"

    previous_map = _limit_up_map(previous) if previous else {}
    today_map = _limit_up_map(current)
    today_broken = {_code(row) for row in _records_for(current, "broken_board") if _code(row)}
    today_down = {_code(row) for row in _records_for(current, "limit_down") if _code(row)}
    previous_change = _previous_change_map(current)
    enriched = []
    for candidate in payload.get("candidates") or []:
        if not isinstance(candidate, dict):
            enriched.append(candidate)
            continue
        item = copy.deepcopy(candidate)
        raw = item.get("raw_candidate") if isinstance(item.get("raw_candidate"), dict) else {}
        candidate_code = _normalize_code(item.get("code") or raw.get("code") or raw.get("symbol") or raw.get("stock_code"))
        current_row = today_map.get(candidate_code)
        previous_row = previous_map.get(candidate_code)
        item["market_ecology"] = {
            "date": target_date,
            "is_limit_up": candidate_code in today_map,
            "is_broken_board": candidate_code in today_broken,
            "is_limit_down": candidate_code in today_down,
            "was_yesterday_limit_up": candidate_code in previous_map,
            "board_count": _board_count(current_row) if current_row else None,
            "first_limit_time": _row_value(current_row, ("首次封板时间", "首次涨停时间", "first_limit_time")) if current_row else None,
            "last_limit_time": _row_value(current_row, ("最后封板时间", "最后涨停时间", "last_limit_time")) if current_row else None,
            "break_count": _integer(_row_value(current_row, ("炸板次数", "break_count"))) if current_row else None,
            "industry": _row_value(current_row, ("所属行业", "行业", "industry")) if current_row else None,
            "yesterday_board_count": _board_count(previous_row) if previous_row else None,
            "yesterday_current_change_pct": previous_change.get(candidate_code),
        }
        enriched.append(item)
    payload["candidates"] = enriched
    payload["market_ecology_date"] = target_date
    payload["market_sentiment_summary"] = {
        "sentiment_score": current.get("sentiment_score"),
        "sentiment_phase": current.get("sentiment_phase"),
        "sentiment_phase_code": current.get("sentiment_phase_code"),
    }
    return payload, None


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_sentiment_markdown(payload: dict[str, Any]) -> None:
    current = payload.get("current") or {}
    components = current.get("score_components") or {}
    ladder = current.get("ladder_counts") or {}
    promotion = current.get("promotion_rates") or {}
    highest_stocks = current.get("highest_board_stocks") or []
    lines = [
        "# 《A股短线市场情绪与涨停生态（改造第2阶段）》",
        "",
        "> 本阶段只新增市场情绪、涨停/炸板/跌停、连板梯队和晋级率；尚未把情绪分直接用于候选股买入评分，也尚未加入主线题材、龙头辨识、集合竞价和开盘确认。",
        "",
        "## 当前交易日概况",
        "",
        f"- 交易日：`{_display(current.get('date'))}`",
        f"- 情绪评分：`{_display(current.get('sentiment_score'))}` / 100",
        f"- 情绪阶段：`{_display(current.get('sentiment_phase'))}`（`{_display(current.get('sentiment_phase_code'))}`）",
        f"- 较上一日变化：`{_display(current.get('sentiment_change'))}`",
        f"- 涨停家数：`{_display(current.get('limit_up_count'))}`",
        f"- 跌停家数：`{_display(current.get('limit_down_count'))}`",
        f"- 炸板家数：`{_display(current.get('broken_board_count'))}`",
        f"- 炸板率：`{_display(current.get('broken_board_rate'))}`%",
        f"- 最高板：`{_display(current.get('highest_board'))}`",
        f"- 最高板股票：`{_display(highest_stocks)}`",
        "",
        "## 评分分项",
        "",
        "| 分项 | 得分 | 满分 |",
        "| --- | ---: | ---: |",
        f"| breadth 涨停广度 | {_display(components.get('breadth'))} | 20 |",
        f"| damage_control 跌停风险 | {_display(components.get('damage_control'))} | 15 |",
        f"| seal_quality 封板质量 | {_display(components.get('seal_quality'))} | 15 |",
        f"| yesterday_premium 昨日涨停溢价 | {_display(components.get('yesterday_premium'))} | 15 |",
        f"| promotion 连板晋级 | {_display(components.get('promotion'))} | 20 |",
        f"| ladder 连板梯队 | {_display(components.get('ladder'))} | 15 |",
        f"| 合计 | {_display(current.get('sentiment_score'))} | 100 |",
        "",
        "## 涨停生态",
        "",
        f"- 连板梯队：`{_display(ladder)}`",
        f"- 梯队完整度：`{_display(current.get('ladder_integrity'))}`%",
        f"- 梯队缺失层级：`{_display(current.get('ladder_missing_levels'))}`",
        "",
        "| 晋级 | eligible | promoted | rate |",
        "| --- | ---: | ---: | ---: |",
    ]
    for key, label in (("1_to_2", "1进2"), ("2_to_3", "2进3"), ("3_plus", "3板以上")):
        item = promotion.get(key)
        lines.append(f"| {label} | {_display(item.get('eligible') if item else None)} | {_display(item.get('promoted') if item else None)} | {_display(item.get('rate') if item else None)}% |")

    lines.extend([
        "",
        "## 昨日涨停赚钱效应",
        "",
        f"- 昨日涨停家数：`{_display(current.get('yesterday_limit_up_count'))}`",
        f"- 昨日涨停平均溢价：`{_display(current.get('yesterday_premium_mean'))}`%",
        f"- 昨日涨停中位溢价：`{_display(current.get('yesterday_premium_median'))}`%",
        f"- 昨日涨停翻红率：`{_display(current.get('yesterday_red_rate'))}`%",
        "",
        "## 最近交易日情绪轨迹",
        "",
        "| 日期 | 情绪评分 | 阶段 | 涨停 | 炸板 | 炸板率 | 跌停 | 最高板 | 昨日涨停中位溢价 |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ])
    for item in payload.get("history") or []:
        lines.append(
            f"| {_display(item.get('date'))} | {_display(item.get('sentiment_score'))} | {_display(item.get('sentiment_phase'))} | "
            f"{_display(item.get('limit_up_count'))} | {_display(item.get('broken_board_count'))} | {_display(item.get('broken_board_rate'))}% | "
            f"{_display(item.get('limit_down_count'))} | {_display(item.get('highest_board'))} | {_display(item.get('yesterday_premium_median'))}% |"
        )
    lines.extend(["", "## 数据源状态", "", "完整 sources、失败原因和原始接口行数请以 `market_sentiment.json` 为准。", ""])
    SENTIMENT_MARKDOWN_PATH.write_text("\n".join(lines), encoding="utf-8")


def _write_enriched_markdown(payload: dict[str, Any], error: str | None) -> None:
    lines = [
        "# A股短线候选池（第2阶段市场生态标签）",
        "",
        "> 第1阶段候选池的原始排序已保留。本报告只新增市场生态标签，不因涨停、炸板或跌停重新排序。",
        "",
    ]
    if error:
        lines.extend([f"> {error}", ""])
    lines.extend([
        "| 原排名 | 股票代码 | 股票名称 | 共振数 | 最高优先级排序字段 | 涨停 | 炸板 | 跌停 | 昨日涨停 | 连板数 |",
        "| ---: | --- | --- | ---: | --- | --- | --- | --- | --- | ---: |",
    ])
    for index, candidate in enumerate(payload.get("candidates") or [], start=1):
        if not isinstance(candidate, dict):
            continue
        ecology = candidate.get("market_ecology") or {}
        lines.append(
            f"| {index} | {_display(candidate.get('code'))} | {_display(candidate.get('name'))} | {_display(candidate.get('resonance_count'))} | "
            f"{_display(candidate.get('strategies'))} | {_display(ecology.get('is_limit_up'))} | {_display(ecology.get('is_broken_board'))} | "
            f"{_display(ecology.get('is_limit_down'))} | {_display(ecology.get('was_yesterday_limit_up'))} | {_display(ecology.get('board_count'))} |"
        )
    ENRICHED_MARKDOWN_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    _configure_logging()
    args = _parse_args()
    target = _resolve_target_date(args.target_date)
    load_dates, output_dates = _load_dates(target, args.history_days)
    logger.info("Using target session %s; history=%s", target.strftime("%Y%m%d"), [item.strftime("%Y%m%d") for item in output_dates])

    days = [_fetch_day(item) for item in load_dates]
    by_date = {item["date"]: item for item in days}
    reports: list[dict[str, Any]] = []
    previous_score: float | None = None
    for item in days:
        previous_date = _previous_session(_calendar(), item["date"])
        previous_day = by_date.get(previous_date)
        report = _build_day_report(previous_day, item, previous_score)
        if item["date"] in output_dates:
            reports.append(report)
        previous_score = report.get("sentiment_score")

    current = reports[-1] if reports else {
        "date": target.strftime("%Y%m%d"),
        "sentiment_score": None,
        "sentiment_phase": PHASES["UNKNOWN"],
        "sentiment_phase_code": "UNKNOWN",
    }
    all_sources = [source for day in days for source in day["sources"]]
    previous_day = by_date.get(_previous_session(_calendar(), target))
    enriched_payload, enrichment_error = _load_candidate_pool(current["date"], by_date[target], previous_day)

    payload = {
        "phase": "short_term_market_sentiment_v1",
        "market": "cn",
        "target_date": current["date"],
        "history_days": args.history_days,
        "data_cutoff": "15:05 Asia/Shanghai",
        "current": current,
        "history": reports,
        "sources": all_sources,
        "source_failures": _source_failures(all_sources),
        "data_quality": "failed" if len(_source_failures(all_sources)) == len(all_sources) else "partial" if _source_failures(all_sources) else "complete",
    }
    _write_json(SENTIMENT_JSON_PATH, payload)
    _write_sentiment_markdown(payload)
    enriched_payload["sentiment_source_failures"] = _source_failures(all_sources)
    if enrichment_error:
        enriched_payload["enrichment_error"] = enrichment_error
    _write_json(ENRICHED_JSON_PATH, enriched_payload)
    _write_enriched_markdown(enriched_payload, enrichment_error)
    logger.info("Wrote market sentiment: %s", SENTIMENT_JSON_PATH)
    logger.info("Wrote enriched candidate pool: %s", ENRICHED_JSON_PATH)

    # Preserve a usable artifact even with partial source failures. Exit nonzero
    # only when every data endpoint failed, so Actions still uploads diagnostics.
    return 1 if len(_source_failures(all_sources)) == len(all_sources) else 0


if __name__ == "__main__":
    sys.exit(main())
