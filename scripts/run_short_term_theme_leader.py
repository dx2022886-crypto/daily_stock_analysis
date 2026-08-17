#!/usr/bin/env python3
"""Build stage-3 theme-strength and leader-recognition reports.

This is a transparent, close-after-market analysis layer.  It consumes the
stage-2 reports and never changes the original screening engine or the stage-1
candidate order.  Missing data remains missing; scores are normalized only
over components that are actually available.
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
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "short_term"
SENTIMENT_PATH = REPORT_DIR / "market_sentiment.json"
ENRICHED_POOL_PATH = REPORT_DIR / "candidate_pool_enriched.json"
THEME_JSON_PATH = REPORT_DIR / "theme_leader.json"
THEME_MD_PATH = REPORT_DIR / "theme_leader.md"
STAGE3_JSON_PATH = REPORT_DIR / "candidate_pool_stage3.json"
STAGE3_MD_PATH = REPORT_DIR / "candidate_pool_stage3.md"

MARKET_TIMEZONE = ZoneInfo("Asia/Shanghai")
FETCH_RETRIES = 3
THEME_WEIGHTS = {
    "limit_up_strength": 25.0,
    "board_height": 15.0,
    "candidate_resonance": 15.0,
    "sector_momentum": 15.0,
    "popularity": 10.0,
    "seal_quality": 10.0,
    "ladder_quality": 10.0,
}
LEADER_WEIGHTS = {
    "board_height": 20.0,
    "limit_up_position": 20.0,
    "theme_position": 15.0,
    "popularity": 15.0,
    "model_resonance": 10.0,
    "sector_leadership": 10.0,
    "risk_following": 10.0,
}
THEME_ROLE_PRIORITY = {"MAIN": 3, "DEGRADED_MAIN": 3, "SECONDARY": 2, "ROTATION": 1, "WEAK": 0}

logger = logging.getLogger("short_term_theme_leader")
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
    if not text:
        return ""
    match = re.fullmatch(r"(?:SH|SZ|BJ)?(\d{1,6})(?:\.(?:SH|SZ|BJ))?", text)
    return match.group(1).zfill(6) if match else ""


def _first(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = mapping.get(key)
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


def _row_code(row: dict[str, Any]) -> str:
    return _normalize_code(_first(row, "代码", "股票代码", "证券代码", "code", "symbol", "stock_code"))


def _row_name(row: dict[str, Any]) -> str:
    return str(_first(row, "名称", "股票名称", "name", "stock_name") or "")


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


def _fetch(function: str, *, source: str = "akshare", **kwargs: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Call one endpoint once per parameter tuple, retaining failure metadata."""
    cache_key = json.dumps([function, kwargs], ensure_ascii=False, sort_keys=True, default=str)
    if cache_key in _API_CACHE:
        _API_STATS["cache_hits"] += 1
        rows, metadata = _API_CACHE[cache_key]
        cached = copy.deepcopy(metadata)
        cached["cache_hit"] = True
        return copy.deepcopy(rows), cached

    _API_STATS["requests"] += 1
    if not hasattr(ak, function):
        metadata = {
            "function": function,
            "source": source,
            "status": "failed",
            "rows": 0,
            "attempts": 0,
            "params": _json_safe(kwargs),
            "error": {"type": "AttributeError", "message": f"AKShare function {function} is unavailable"},
        }
        _API_CACHE[cache_key] = ([], copy.deepcopy(metadata))
        return [], metadata

    last_error: Exception | None = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            frame = getattr(ak, function)(**kwargs)
            rows = _records(frame)
            metadata = {
                "function": function,
                "source": source,
                "status": "success",
                "rows": len(rows),
                "attempts": attempt,
                "params": _json_safe(kwargs),
            }
            _API_CACHE[cache_key] = (copy.deepcopy(rows), copy.deepcopy(metadata))
            return rows, metadata
        except Exception as exc:  # Each source must fail independently.
            last_error = exc
            if attempt < FETCH_RETRIES:
                time.sleep(2 ** (attempt - 1))
    metadata = {
        "function": function,
        "source": source,
        "status": "failed",
        "rows": 0,
        "attempts": FETCH_RETRIES,
        "params": _json_safe(kwargs),
        "error": {"type": type(last_error).__name__, "message": str(last_error)},
    }
    _API_CACHE[cache_key] = ([], copy.deepcopy(metadata))
    return [], metadata


def _source_ok(source: dict[str, Any] | None) -> bool:
    return bool(source and source.get("status") == "success")


def _parse_date(raw: str | None) -> date | None:
    if not raw:
        return None
    try:
        return datetime.strptime(raw, "%Y%m%d").date()
    except ValueError as exc:
        raise ValueError(f"target date must be YYYYMMDD, got {raw!r}") from exc


def _target_date(sentiment: dict[str, Any], raw: str | None) -> date:
    parsed = _parse_date(raw)
    if parsed:
        return parsed
    parsed = _parse_date(str(sentiment.get("target_date") or sentiment.get("current", {}).get("date") or ""))
    if parsed:
        return parsed
    now = datetime.now(MARKET_TIMEZONE)
    candidate = now.date()
    if now.hour < 15 or (now.hour == 15 and now.minute < 5):
        candidate -= timedelta(days=1)
    while candidate.weekday() >= 5:
        candidate -= timedelta(days=1)
    return candidate


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain an object")
    return payload


def _candidate_map(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    candidates = [item for item in payload.get("candidates", []) if isinstance(item, dict)]
    result: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        raw = candidate.get("raw_candidate") if isinstance(candidate.get("raw_candidate"), dict) else {}
        code = _normalize_code(_first(candidate, "code", "symbol") or _first(raw, "code", "symbol", "stock_code"))
        if code:
            item = copy.deepcopy(candidate)
            item["code"] = code
            result[code] = item
    return candidates, result


def _fetch_market_data(target: date) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    date_text = target.strftime("%Y%m%d")
    data: dict[str, Any] = {"date": date_text}
    sources: list[dict[str, Any]] = []
    for key, function in (("limit_up", "stock_zt_pool_em"), ("broken_board", "stock_zt_pool_zbgc_em")):
        rows, source = _fetch(function, source="eastmoney", date=date_text)
        data[key] = rows
        data[f"{key}_source"] = source
        sources.append(source)
    hot_rows, hot_source = _fetch("stock_hot_rank_em", source="eastmoney")
    data["hot"] = hot_rows
    data["hot_source"] = hot_source
    sources.append(hot_source)
    data["data_coverage"] = {
        "limit_up_available": _source_ok(data["limit_up_source"]),
        "broken_board_available": _source_ok(data["broken_board_source"]),
        "hot_rank_available": _source_ok(data["hot_source"]),
    }
    return data, sources


def _theme_name(row: dict[str, Any]) -> str:
    return str(_first(row, "板块名称", "题材名称", "概念名称", "行业名称", "名称", "theme_name", "name") or "").strip()


def _theme_symbol(row: dict[str, Any], fallback: str) -> str:
    # AKShare's EM constituent endpoints historically take the board name,
    # while other providers expose an index code.  Prefer the name for EM
    # compatibility and retain code fields for THS/normalized output.
    return str(_first(row, "板块名称", "行业名称", "名称", "板块代码", "指数代码", "代码", "theme_code", "code", "symbol") or fallback)


def _missing_source(function: str, source: str) -> dict[str, Any]:
    return {
        "function": function,
        "source": source,
        "status": "failed",
        "rows": 0,
        "attempts": 0,
        "params": {},
        "error": {"type": "AttributeError", "message": f"AKShare function {function} is unavailable"},
    }


def _merge_theme_member(
    stock_to_themes: dict[str, list[str]],
    theme_sources: dict[str, dict[str, Any]],
    code: str,
    theme: str,
    source: str,
    industry: str | None = None,
) -> None:
    if not code or not theme:
        return
    stock_to_themes.setdefault(code, []).append(theme)
    record = theme_sources.setdefault(code, {"themes": [], "industries": [], "sources": []})
    record["themes"].append(theme)
    if industry:
        record["industries"].append(industry)
    record["sources"].append(source)


def _fetch_theme_universe(
    target_date_text: str,
    market: dict[str, Any] | None = None,
    candidates: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build one normalized theme universe with EM, THS and industry fallback."""
    market = market or {"limit_up": [], "broken_board": [], "hot": []}
    candidates = candidates or {}
    themes: dict[str, dict[str, Any]] = {}
    stock_to_themes: dict[str, list[str]] = {}
    stock_to_industries: dict[str, list[str]] = {}
    theme_sources: dict[str, dict[str, Any]] = {}
    sources: list[dict[str, Any]] = []
    em_concept_ok = False
    ths_concept_ok = False
    em_industry_ok = False
    ths_industry_ok = False

    def ensure_theme(name: str, symbol: str, theme_type: str, source: str, row: dict[str, Any] | None = None) -> dict[str, Any]:
        entry = themes.setdefault(name, {
            "theme_name": name,
            "theme_type": theme_type,
            "theme_code": symbol,
            "source": source,
            "members": [],
            "member_rows": [],
            "board_change_pct": _number(_first(row or {}, "涨跌幅", "涨跌幅(%)", "change_pct")),
            "hist_available": False,
            "concept_available": False,
            "data_quality": "partial" if source != "eastmoney" else "complete",
            "is_degraded": False,
        })
        return entry

    def append_members(entry: dict[str, Any], rows: list[dict[str, Any]], source: str) -> None:
        existing = set(entry.get("members") or [])
        for row in rows:
            code = _row_code(row)
            if not code:
                continue
            existing.add(code)
            entry.setdefault("member_rows", []).append(row)
            _merge_theme_member(stock_to_themes, theme_sources, code, entry["theme_name"], source, _first(row, "所属行业", "行业", "industry"))
        entry["members"] = sorted(existing)

    # EastMoney concept source.
    em_rows, em_name_source = _fetch("stock_board_concept_name_em", source="eastmoney")
    sources.append(em_name_source)
    em_concept_ok = _source_ok(em_name_source) and bool(em_rows)
    if em_concept_ok:
        for board in em_rows:
            name = _theme_name(board)
            if not name:
                continue
            symbol = _theme_symbol(board, name)
            entry = ensure_theme(name, symbol, "CONCEPT", "eastmoney", board)
            members, member_source = _fetch("stock_board_concept_cons_em", source="eastmoney", symbol=symbol)
            sources.append(member_source)
            entry["concept_available"] = _source_ok(member_source)
            append_members(entry, members, "eastmoney")
            hist_rows, hist_source = _fetch(
                "stock_board_concept_hist_em",
                source="eastmoney",
                symbol=symbol,
                period="daily",
                start_date=target_date_text,
                end_date=target_date_text,
                adjust="",
            )
            sources.append(hist_source)
            if _source_ok(hist_source) and hist_rows:
                entry["board_change_pct"] = _number(_first(hist_rows[-1], "涨跌幅", "涨跌幅(%)", "change_pct"))
                entry["hist_available"] = entry["board_change_pct"] is not None

    # THS concept fallback/supplement.  Every optional function is checked at runtime.
    need_ths_concept = not em_concept_ok or not any(item.get("members") for item in themes.values())
    ths_concept_rows: list[dict[str, Any]] = []
    if need_ths_concept:
        for function in ("stock_board_concept_name_ths", "stock_board_concept_index_ths"):
            if not hasattr(ak, function):
                sources.append(_missing_source(function, "ths"))
                continue
            ths_concept_rows, ths_name_source = _fetch(function, source="ths")
            sources.append(ths_name_source)
            if _source_ok(ths_name_source) and ths_concept_rows:
                ths_concept_ok = True
                break
    for board in ths_concept_rows:
        name = _theme_name(board)
        if not name:
            continue
        symbol = _theme_symbol(board, name)
        entry = ensure_theme(name, symbol, "CONCEPT", "ths", board)
        if entry.get("source") == "eastmoney" and entry.get("members"):
            continue
        entry["source"] = "ths"
        entry["data_quality"] = "partial"
        # Optional constituent APIs are queried only for a bounded set of boards.
        cons_function = next((candidate for candidate in ("stock_board_concept_cons_ths", "stock_board_cons_ths") if hasattr(ak, candidate)), None)
        if cons_function and len([item for item in themes.values() if item.get("source") == "ths"]) <= 50:
            members, member_source = _fetch(cons_function, source="ths", symbol=symbol)
            sources.append(member_source)
            append_members(entry, members, "ths")

    # EastMoney industry source, then THS industry fallback.
    em_industry_rows, em_industry_source = _fetch("stock_board_industry_name_em", source="eastmoney")
    sources.append(em_industry_source)
    em_industry_ok = _source_ok(em_industry_source) and bool(em_industry_rows)
    industry_rows = em_industry_rows
    industry_source_name = "eastmoney"
    if not em_industry_ok:
        industry_rows = []
        for function in ("stock_board_industry_name_ths", "stock_board_industry_index_ths", "stock_board_industry_summary_ths"):
            if not hasattr(ak, function):
                sources.append(_missing_source(function, "ths"))
                continue
            industry_rows, industry_list_source = _fetch(function, source="ths")
            sources.append(industry_list_source)
            if _source_ok(industry_list_source) and industry_rows:
                ths_industry_ok = True
                industry_source_name = "ths"
                break
    for board in industry_rows:
        industry = _theme_name(board)
        if not industry:
            continue
        symbol = _theme_symbol(board, industry)
        members, member_source = _fetch(
            "stock_board_industry_cons_em" if industry_source_name == "eastmoney" else "stock_board_industry_cons_ths",
            source=industry_source_name,
            symbol=symbol,
        ) if (industry_source_name == "eastmoney" and hasattr(ak, "stock_board_industry_cons_em")) or (industry_source_name == "ths" and hasattr(ak, "stock_board_industry_cons_ths")) else ([], _missing_source("stock_board_industry_cons_ths", "ths"))
        sources.append(member_source)
        if not _source_ok(member_source):
            continue
        for row in members:
            code = _row_code(row)
            if code:
                stock_to_industries.setdefault(code, []).append(industry)
                _merge_theme_member(stock_to_themes, theme_sources, code, industry, industry_source_name, industry)
        if industry_source_name == "eastmoney" and hasattr(ak, "stock_board_industry_hist_em"):
            _, industry_hist_source = _fetch(
                "stock_board_industry_hist_em",
                source="eastmoney",
                symbol=symbol,
                period="daily",
                start_date=target_date_text,
                end_date=target_date_text,
                adjust="",
            )
            sources.append(industry_hist_source)

    # Pool fields provide a cheap stock -> industry supplement even when board
    # constituent pages are unavailable.
    pool_rows = list(market.get("limit_up") or []) + list(market.get("broken_board") or [])
    for candidate in candidates.values():
        ecology = candidate.get("market_ecology") or {}
        code = _normalize_code(candidate.get("code"))
        industry = str(ecology.get("industry") or "").strip()
        if code and industry:
            pool_rows.append({"代码": code, "名称": candidate.get("name"), "所属行业": industry})
    for row in pool_rows:
        code = _row_code(row)
        industry = str(_first(row, "所属行业", "行业", "industry") or "").strip()
        if code and industry:
            stock_to_industries.setdefault(code, []).append(industry)
            if not stock_to_themes.get(code):
                _merge_theme_member(stock_to_themes, theme_sources, code, industry, "zt_pool", industry)

    concept_available = em_concept_ok or ths_concept_ok
    market_available = bool(
        _source_ok(market.get("limit_up_source"))
        or _source_ok(market.get("broken_board_source"))
        or _source_ok(market.get("hot_source"))
    )
    if not concept_available:
        # Lowest-cost fallback: group available limit-up/broken-board rows by industry.
        degraded: dict[str, dict[str, Any]] = {}
        for row in pool_rows:
            industry = str(_first(row, "所属行业", "行业", "industry") or "").strip()
            code = _row_code(row)
            if not industry or not code:
                continue
            entry = degraded.setdefault(industry, {
                "theme_name": industry,
                "theme_type": "INDUSTRY_DEGRADED",
                "theme_code": industry,
                "source": "limit_up_industry_cluster",
                "members": [],
                "member_rows": [],
                "board_change_pct": None,
                "hist_available": False,
                "concept_available": True,
                "data_quality": "degraded",
                "is_degraded": True,
            })
            if code not in entry["members"]:
                entry["members"].append(code)
                entry["member_rows"].append(row)
                _merge_theme_member(stock_to_themes, theme_sources, code, industry, "zt_pool", industry)
        themes = degraded

    for code in stock_to_themes:
        stock_to_themes[code] = sorted(set(stock_to_themes[code]))
    for code in stock_to_industries:
        stock_to_industries[code] = sorted(set(stock_to_industries[code]))
    for code, record in theme_sources.items():
        record["themes"] = sorted(set(record["themes"]))
        record["industries"] = sorted(set(record["industries"]))
        record["sources"] = sorted(set(record["sources"]))

    em_concept_members_ok = any(item.get("source") == "eastmoney" and item.get("members") for item in themes.values())
    ths_concept_members_ok = any(item.get("source") == "ths" and item.get("members") for item in themes.values())
    if em_concept_members_ok and em_concept_ok and em_industry_ok:
        source_mode = "FULL_EASTMONEY"
    elif ths_concept_members_ok and ths_concept_ok and ths_industry_ok and not em_concept_ok:
        source_mode = "FULL_THS"
    elif themes and any(item.get("is_degraded") for item in themes.values()):
        source_mode = "INDUSTRY_DEGRADED"
    elif themes:
        source_mode = "MIXED"
    elif market_available:
        source_mode = "MARKET_ONLY"
    else:
        source_mode = "UNAVAILABLE"
    data_quality = "complete" if source_mode == "FULL_EASTMONEY" else "partial" if source_mode in {"FULL_THS", "MIXED"} else "degraded" if source_mode in {"INDUSTRY_DEGRADED", "MARKET_ONLY"} else "unavailable"
    source_failures = [item for item in sources if item.get("status") == "failed"]
    return {
        "themes": themes,
        "stock_to_themes": stock_to_themes,
        "stock_to_industries": stock_to_industries,
        "theme_sources": theme_sources,
        "sources": sources,
        "source_failures": source_failures,
        "source": "eastmoney" if source_mode == "FULL_EASTMONEY" else "ths" if source_mode == "FULL_THS" else "degraded" if source_mode in {"INDUSTRY_DEGRADED", "MARKET_ONLY"} else "unavailable",
        "source_mode": source_mode,
        "data_quality": data_quality,
        "data_coverage": {
            "concept_available": concept_available,
            "industry_available": em_industry_ok or ths_industry_ok,
            "limit_up_available": _source_ok(market.get("limit_up_source")),
            "broken_board_available": _source_ok(market.get("broken_board_source")),
            "hot_rank_available": _source_ok(market.get("hot_source")),
        },
    }


def _fetch_themes(
    target_date_text: str,
    market: dict[str, Any] | None = None,
    candidates: dict[str, dict[str, Any]] | None = None,
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]], dict[str, list[str]], list[dict[str, Any]], dict[str, Any]]:
    universe = _fetch_theme_universe(target_date_text, market, candidates)
    return universe["themes"], universe["stock_to_themes"], universe["stock_to_industries"], universe["sources"], universe


def _stock_map(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        code = _row_code(row)
        if code:
            result[code] = row
    return result


def _board_count(row: dict[str, Any] | None) -> int | None:
    if not row:
        return None
    return _integer(_first(row, "连板数", "连板", "板数", "board_count"))


def _time_score(value: Any) -> float | None:
    text = str(value or "").strip().replace(":", "")
    match = re.search(r"(\d{3,4})", text)
    if not match:
        return None
    minutes = int(match.group(1)[-4:-2]) * 60 + int(match.group(1)[-2:])
    # 09:30 is 10 points and 14:50 is near 0; this is a transparent proxy for
    # early sealing, not an intraday prediction.
    return max(0.0, min(10.0, (15 * 60 - minutes) / 330 * 10))


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _score_components(components: dict[str, float | None], weights: dict[str, float]) -> dict[str, Any]:
    available = {key: value for key, value in components.items() if value is not None}
    raw = round(sum(float(value) for value in available.values()), 4) if available else None
    available_weight = round(sum(weights[key] for key in available), 4)
    normalized = round(raw / available_weight * 100, 4) if raw is not None and available_weight else None
    coverage_ratio = round(available_weight / sum(weights.values()), 4) if weights else 0.0
    confidence_adjusted = round(normalized * math.sqrt(coverage_ratio), 4) if normalized is not None else None
    return {
        "score_raw": raw,
        "available_weight": available_weight,
        "coverage_ratio": coverage_ratio,
        "normalized_score": normalized,
        "confidence_adjusted_score": confidence_adjusted,
        "data_quality": "complete" if len(available) == len(weights) else "partial" if available else "unavailable",
        "components": {key: (round(float(value), 4) if value is not None else None) for key, value in components.items()},
    }


def _theme_components(metrics: dict[str, Any]) -> dict[str, float | None]:
    up = _number(metrics.get("limit_up_count"))
    members = _number(metrics.get("member_count"))
    if up is None or members is None:
        limit_up_strength = None
    else:
        limit_up_strength = _clamp(up / 10 * 12.5 + (up / members * 100 if members else 0) / 10 * 12.5, 0, 25)

    highest = _number(metrics.get("highest_board"))
    board_height = _clamp(highest / 5 * 15, 0, 15) if highest is not None else None

    candidate_count = _number(metrics.get("candidate_count"))
    resonance_sum = _number(metrics.get("candidate_resonance_sum"))
    candidate_resonance = None if candidate_count is None or resonance_sum is None else _clamp(candidate_count / 5 * 7.5 + resonance_sum / 20 * 7.5, 0, 15)

    board_change = _number(metrics.get("board_change_pct"))
    average_change = _number(metrics.get("average_change_pct"))
    sector_momentum = None if board_change is None or average_change is None else _clamp((board_change + 5) / 10 * 10 + (average_change + 5) / 10 * 5, 0, 15)

    hot_count = _number(metrics.get("hot_stock_count"))
    popularity = _clamp(hot_count / 10 * 10, 0, 10) if hot_count is not None else None

    broken = _number(metrics.get("broken_board_count"))
    seal_quality = None if up is None or broken is None else _clamp(up / (up + broken) * 10, 0, 10) if up + broken else 0.0

    ladder = metrics.get("ladder_counts")
    ladder_quality = None
    if isinstance(ladder, dict):
        ladder_quality = sum(10 / 3 for key in ("1", "2", "3_plus") if _number(ladder.get(key)) and _number(ladder.get(key)) > 0)
        ladder_quality = _clamp(ladder_quality, 0, 10)
    return {
        "limit_up_strength": limit_up_strength,
        "board_height": board_height,
        "candidate_resonance": candidate_resonance,
        "sector_momentum": sector_momentum,
        "popularity": popularity,
        "seal_quality": seal_quality,
        "ladder_quality": ladder_quality,
    }


def _theme_role(score: float | None, rank: int, metrics: dict[str, Any], first_score: float | None) -> str | None:
    if score is None:
        return None
    gap = (first_score - score) if first_score is not None else math.inf
    coverage = _number(metrics.get("coverage_ratio")) or 0.0
    degraded = bool(metrics.get("is_degraded")) or metrics.get("data_quality") == "degraded"
    if degraded and rank == 1 and score >= 50 and ((_number(metrics.get("limit_up_count")) or 0) >= 5 or (_number(metrics.get("highest_board")) or 0) >= 3):
        metrics["is_degraded_main"] = True
        return "MAIN"
    if coverage < 0.4:
        return "ROTATION"
    if rank == 1 and score >= 70 and coverage >= 0.6:
        return "MAIN"
    if score >= 60 and gap <= 10 and coverage >= 0.4:
        return "SECONDARY"
    if score >= 50:
        return "ROTATION"
    # A visible high-board core should not be mechanically classified as WEAK.
    if (_number(metrics.get("highest_board")) or 0) >= 4:
        return "ROTATION"
    return "WEAK"


def _theme_sort_key(item: dict[str, Any]) -> tuple[Any, ...]:
    return (
        -(item.get("confidence_adjusted_score") if item.get("confidence_adjusted_score") is not None else float("-inf")),
        -(item.get("limit_up_count") if item.get("limit_up_count") is not None else float("-inf")),
        -(item.get("highest_board") if item.get("highest_board") is not None else float("-inf")),
        -(item.get("candidate_resonance_sum") if item.get("candidate_resonance_sum") is not None else float("-inf")),
        str(item.get("theme_name") or ""),
    )


def _select_primary_theme(themes: list[str], theme_metrics: dict[str, dict[str, Any]], leader_scores: dict[str, float] | None = None) -> str | None:
    if not themes:
        return None
    leader_scores = leader_scores or {}
    return sorted(
        themes,
        key=lambda theme: (
            -(theme_metrics.get(theme, {}).get("theme_score") if theme_metrics.get(theme, {}).get("theme_score") is not None else float("-inf")),
            -THEME_ROLE_PRIORITY.get(theme_metrics.get(theme, {}).get("theme_role"), -1),
            -(theme_metrics.get(theme, {}).get("limit_up_count") if theme_metrics.get(theme, {}).get("limit_up_count") is not None else float("-inf")),
            -leader_scores.get(theme, float("-inf")),
            theme,
        ),
    )[0]


def _build_theme_metrics(
    themes: dict[str, dict[str, Any]],
    candidates: dict[str, dict[str, Any]],
    stock_to_themes: dict[str, list[str]],
    market: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    up_map = _stock_map(market["limit_up"])
    broken_map = _stock_map(market["broken_board"])
    up_available = _source_ok(market["limit_up_source"])
    broken_available = _source_ok(market["broken_board_source"])
    hot_available = _source_ok(market["hot_source"])
    hot_codes = {_row_code(row) for row in market["hot"] if _row_code(row)}
    result: dict[str, dict[str, Any]] = {}
    for theme, data in themes.items():
        member_codes = set(data.get("members") or [])
        member_rows = data.get("member_rows") or []
        candidate_codes = sorted(code for code in candidates if code in member_codes)
        up_codes = sorted(code for code in member_codes if code in up_map) if up_available else None
        broken_codes = sorted(code for code in member_codes if code in broken_map) if broken_available else None
        changes = [_number(_first(row, "涨跌幅", "涨跌幅(%)", "change_pct")) for row in member_rows]
        changes = [value for value in changes if value is not None]
        board_counts = [_board_count(up_map[code]) for code in (up_codes or []) if code in up_map]
        board_counts = [value for value in board_counts if value is not None]
        ladder = {"1": 0, "2": 0, "3_plus": 0}
        for count in board_counts:
            if count == 1:
                ladder["1"] += 1
            elif count == 2:
                ladder["2"] += 1
            elif count >= 3:
                ladder["3_plus"] += 1
        metrics: dict[str, Any] = {
            "theme_name": theme,
            "theme_type": data.get("theme_type", "CONCEPT"),
            "theme_code": data.get("theme_code"),
            "source": data.get("source"),
            "candidate_count": len(candidate_codes) if data.get("concept_available") else None,
            "candidate_codes": candidate_codes if data.get("concept_available") else [],
            "member_count": len(member_codes) if data.get("concept_available") else None,
            "limit_up_count": len(up_codes) if up_codes is not None else None,
            "broken_board_count": len(broken_codes) if broken_codes is not None else None,
            "highest_board": max(board_counts) if board_counts else (0 if up_codes == [] else None),
            "leader_stock": None,
            "average_change_pct": round(sum(changes) / len(changes), 4) if changes else None,
            "board_change_pct": data.get("board_change_pct"),
            "hot_stock_count": sum(code in hot_codes for code in member_codes) if hot_available else None,
            "candidate_resonance_sum": sum(int(candidates[code].get("resonance_count") or 0) for code in candidate_codes) if data.get("concept_available") else None,
            "ladder_counts": ladder if up_codes is not None else None,
            "data_available": {
                "concept_members": bool(data.get("concept_available")),
                "concept_history": bool(data.get("hist_available")),
                "limit_up": up_available,
                "broken_board": broken_available,
                "hot_rank": hot_available,
            },
            "is_degraded": bool(data.get("is_degraded")),
        }
        score_details = _score_components(_theme_components(metrics), THEME_WEIGHTS)
        if data.get("data_quality") == "degraded":
            score_details["data_quality"] = "degraded"
        elif data.get("data_quality") == "partial" and score_details["data_quality"] == "complete":
            score_details["data_quality"] = "partial"
        metrics.update(score_details)
        metrics["theme_score"] = score_details["normalized_score"]
        result[theme] = metrics

    ranked = sorted(result.values(), key=_theme_sort_key)
    first_score = ranked[0].get("theme_score") if ranked else None
    for rank, item in enumerate(ranked, start=1):
        item["rank"] = rank
        item["theme_role"] = _theme_role(item.get("theme_score"), rank, item, first_score)
    return result


def _build_hot_map(rows: list[dict[str, Any]]) -> tuple[dict[str, int], dict[str, str]]:
    ranks: dict[str, int] = {}
    names: dict[str, str] = {}
    for fallback, row in enumerate(rows, start=1):
        code = _row_code(row)
        if not code:
            continue
        rank = _integer(_first(row, "当前排名", "排名", "人气排名", "rank")) or fallback
        ranks[code] = rank
        names[code] = _row_name(row)
    return ranks, names


def _build_stock_records(
    candidates: dict[str, dict[str, Any]],
    stock_to_themes: dict[str, list[str]],
    stock_to_industries: dict[str, list[str]],
    theme_metrics: dict[str, dict[str, Any]],
    market: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    up_map = _stock_map(market["limit_up"])
    broken_map = _stock_map(market["broken_board"])
    hot_ranks, hot_names = _build_hot_map(market["hot"])
    codes = set(candidates) | set(up_map) | set(broken_map) | set(hot_ranks)
    result: dict[str, dict[str, Any]] = {}
    for code in sorted(codes):
        up_row = up_map.get(code)
        broken_row = broken_map.get(code)
        candidate = candidates.get(code, {})
        # Industries may be present in stock_to_themes for provenance, but
        # only normalized theme metrics can be selected as a primary theme.
        themes = [theme for theme in stock_to_themes.get(code, []) if theme in theme_metrics]
        primary = _select_primary_theme(themes, theme_metrics)
        theme = theme_metrics.get(primary or "", {})
        board_count = _board_count(up_row)
        if board_count is None and broken_row:
            board_count = _board_count(broken_row)
        result[code] = {
            "code": code,
            "name": _row_name(up_row or broken_row or {}) or str(candidate.get("name") or hot_names.get(code) or ""),
            "themes": themes,
            "industry": (stock_to_industries.get(code) or [None])[0],
            "is_limit_up": up_row is not None,
            "is_broken_board": broken_row is not None,
            "board_count": board_count,
            "first_limit_time": _first(up_row or broken_row or {}, "首次封板时间", "首次涨停时间", "first_limit_time"),
            "last_limit_time": _first(up_row or broken_row or {}, "最后封板时间", "最后涨停时间", "last_limit_time"),
            "break_count": _integer(_first(up_row or broken_row or {}, "炸板次数", "break_count")),
            "hot_rank": hot_ranks.get(code) if _source_ok(market["hot_source"]) else None,
            "resonance_count": int(candidate.get("resonance_count") or 0) if candidate else 0,
            "candidate": bool(candidate),
            "primary_theme": primary,
            "primary_theme_role": theme.get("theme_role"),
        }
    return result


def _leader_components(stock: dict[str, Any], theme_metrics: dict[str, dict[str, Any]], highest_market_board: int | None) -> dict[str, float | None]:
    board = _number(stock.get("board_count"))
    board_height = _clamp(board / max(highest_market_board or 5, 5) * 20, 0, 20) if board is not None else None
    if stock.get("is_limit_up"):
        position = 10.0
        early = _time_score(stock.get("first_limit_time"))
        if early is not None:
            position += early
        else:
            position += 5.0
        breaks = _number(stock.get("break_count"))
        position += _clamp(5 - (breaks or 0), 0, 5)
    elif stock.get("is_broken_board"):
        position = 8.0
        early = _time_score(stock.get("first_limit_time"))
        position += early / 2 if early is not None else 2.0
        position -= _clamp((_number(stock.get("break_count")) or 0) * 1.5, 0, 5)
    else:
        position = None
    role = stock.get("primary_theme_role")
    theme_position = None if not role else {"MAIN": 12.0, "DEGRADED_MAIN": 10.0, "SECONDARY": 9.0, "ROTATION": 6.0, "WEAK": 3.0}.get(role, 0.0) + _clamp((len(stock.get("themes") or []) - 1) * 1.5, 0, 3)
    rank = _number(stock.get("hot_rank"))
    popularity = _clamp((101 - rank) / 100 * 15, 0, 15) if rank is not None else None
    model_resonance = _clamp((_number(stock.get("resonance_count")) or 0) / 4 * 10, 0, 10)
    theme = theme_metrics.get(stock.get("primary_theme") or "", {})
    board_change = _number(theme.get("board_change_pct"))
    average_change = _number(theme.get("average_change_pct"))
    sector_leadership = None if board_change is None or average_change is None else _clamp((board_change + 5) / 10 * 5 + (average_change + 5) / 10 * 5, 0, 10)
    risk = 10.0
    risk -= _clamp((_number(stock.get("break_count")) or 0) * 2, 0, 6)
    if not stock.get("is_limit_up"):
        risk -= 2.0
    if not stock.get("candidate") and (stock.get("hot_rank") or 999) > 50:
        risk -= 2.0
    return {
        "board_height": board_height,
        "limit_up_position": _clamp(position, 0, 20) if position is not None else None,
        "theme_position": _clamp(theme_position, 0, 15) if theme_position is not None else None,
        "popularity": popularity,
        "model_resonance": model_resonance,
        "sector_leadership": sector_leadership,
        "risk_following": _clamp(risk, 0, 10),
    }


def _stock_role(stock: dict[str, Any], theme_rank: int | None, highest_market_board: int | None) -> str:
    if stock.get("is_broken_board") and (theme_rank or 99) <= 2:
        return "BROKEN_CORE"
    if not stock.get("themes"):
        if stock.get("is_limit_up") and stock.get("board_count") == highest_market_board:
            return "MARKET_LEADER"
        if stock.get("is_broken_board") and (stock.get("candidate") or stock.get("hot_rank") is not None):
            return "BROKEN_CORE"
        if stock.get("candidate") or stock.get("hot_rank") is not None:
            return "FRONT_CORE"
        return "OBSERVE"
    if stock.get("is_limit_up") and stock.get("board_count") == highest_market_board and stock.get("primary_theme_role") == "MAIN":
        return "MARKET_LEADER"
    if stock.get("primary_theme_role") in {"MAIN", "SECONDARY"} and theme_rank == 1:
        return "THEME_LEADER"
    if stock.get("primary_theme_role") in {"MAIN", "SECONDARY"} and (theme_rank or 99) <= 3:
        return "FRONT_CORE"
    if stock.get("is_limit_up") or stock.get("is_broken_board"):
        return "FOLLOWER"
    return "OBSERVE"


def _leader_reasons(stock: dict[str, Any], theme_rank: int | None, theme: dict[str, Any], highest_market_board: int | None) -> list[str]:
    reasons: list[str] = []
    if stock.get("board_count") is not None and stock.get("board_count") == highest_market_board:
        reasons.append("市场最高板")
    if stock.get("primary_theme_role") == "MAIN" and theme_rank == 1:
        reasons.append("所属主线题材排名第1")
    if stock.get("hot_rank") is not None and stock.get("hot_rank") <= 10:
        reasons.append("东方财富人气榜Top10")
    if theme.get("limit_up_count") is not None and theme.get("limit_up_count") > 0:
        reasons.append("题材内部存在涨停梯队")
    if stock.get("resonance_count", 0) >= 2:
        reasons.append("第1阶段多模型共振")
    if _time_score(stock.get("first_limit_time")) is not None and _time_score(stock.get("first_limit_time")) >= 7:
        reasons.append("封板时间靠前")
    if not reasons:
        reasons.append("具备可观测的题材或市场数据")
    return reasons


def _build_leaders(stock_records: dict[str, dict[str, Any]], theme_metrics: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    boards = [stock.get("board_count") for stock in stock_records.values() if stock.get("board_count") is not None]
    highest = max(boards) if boards else None
    for stock in stock_records.values():
        details = _score_components(_leader_components(stock, theme_metrics, highest), LEADER_WEIGHTS)
        stock.update(details)
        stock["leader_score"] = details["confidence_adjusted_score"]
        stock["leader_data_quality"] = details["data_quality"]
        stock["leader_source_mode"] = "full_theme" if stock.get("themes") else "market_only"

    by_theme: dict[str, list[dict[str, Any]]] = {}
    for stock in stock_records.values():
        for theme in stock.get("themes") or []:
            by_theme.setdefault(theme, []).append(stock)
    theme_rank_map: dict[str, dict[str, int]] = {}
    for theme, stocks in by_theme.items():
        ordered = sorted(stocks, key=lambda item: (-(item.get("leader_score") if item.get("leader_score") is not None else float("-inf")), item["code"]))
        theme_rank_map[theme] = {stock["code"]: rank for rank, stock in enumerate(ordered, start=1)}
        if ordered:
            theme_metrics[theme]["leader_stock"] = {key: ordered[0].get(key) for key in ("code", "name", "leader_score")}
            theme_metrics[theme]["leader_stock_rank"] = 1

    leaders: list[dict[str, Any]] = []
    for stock in stock_records.values():
        theme = stock.get("primary_theme")
        theme_data = theme_metrics.get(theme or "", {})
        rank = theme_rank_map.get(theme or "", {}).get(stock["code"])
        stock["primary_theme_rank"] = rank
        stock["stock_role"] = _stock_role(stock, rank, highest)
        stock["leader_reasons"] = _leader_reasons(stock, rank, theme_data, highest)
        if stock.get("is_limit_up") or stock.get("is_broken_board") or stock.get("candidate") or stock.get("hot_rank") is not None:
            leaders.append(copy.deepcopy(stock))
    leaders.sort(key=lambda item: (-(item.get("leader_score") if item.get("leader_score") is not None else float("-inf")), item["code"]))
    market_leaders = []
    for rank, stock in enumerate(leaders[:5], start=1):
        item = {
            "market_leader_rank": rank,
            "code": stock["code"],
            "name": stock["name"],
            "primary_theme": stock.get("primary_theme"),
            "stock_role": "MARKET_LEADER" if rank == 1 else stock.get("stock_role"),
            "leader_score": stock.get("leader_score"),
            "leader_data_quality": stock.get("leader_data_quality"),
            "leader_source_mode": stock.get("leader_source_mode"),
            "board_count": stock.get("board_count"),
            "hot_rank": stock.get("hot_rank"),
            "resonance_count": stock.get("resonance_count"),
            "leader_reasons": stock.get("leader_reasons") or [],
        }
        market_leaders.append(item)
    return leaders, market_leaders


def _theme_environment(phase: str | None) -> str:
    return {
        "冰点": "等待修复",
        "修复": "关注最先走强题材",
        "启动": "积极寻找主线",
        "发酵": "主线强化",
        "高潮": "警惕一致性过强",
        "分歧": "只关注最强主线前排",
        "退潮": "降低接力预期",
    }.get(phase or "", "数据不足，暂不判断")


def _enrich_candidates(payload: dict[str, Any], stock_records: dict[str, dict[str, Any]], theme_metrics: dict[str, dict[str, Any]]) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    enriched: list[Any] = []
    for original in payload.get("candidates", []) or []:
        if not isinstance(original, dict):
            enriched.append(original)
            continue
        item = copy.deepcopy(original)
        code = _normalize_code(item.get("code"))
        stock = stock_records.get(code, {"code": code, "themes": [], "industry": None, "leader_score": None, "stock_role": "OBSERVE", "leader_reasons": []})
        themes = stock.get("themes") or []
        primary = _select_primary_theme(themes, theme_metrics)
        theme = theme_metrics.get(primary or "", {})
        item["themes"] = themes
        item["industry"] = stock.get("industry")
        item["theme_analysis"] = {
            "primary_theme": primary,
            "themes": themes,
            "primary_theme_rank": stock.get("primary_theme_rank"),
            "primary_theme_score": theme.get("theme_score"),
            "primary_theme_role": theme.get("theme_role"),
            "leader_score": stock.get("leader_score"),
            "stock_role": stock.get("stock_role", "OBSERVE"),
            "market_leader_rank": None,
            "leader_reasons": stock.get("leader_reasons") or [],
        }
        enriched.append(item)
    result["candidates"] = enriched
    result["stage"] = "short_term_theme_leader_v1"
    return result


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_theme_markdown(payload: dict[str, Any]) -> None:
    context = payload.get("market_context") or {}
    lines = [
        "# 《A股短线主线题材与龙头辨识（改造第3阶段）》",
        "",
        "> 本阶段只做收盘后主线题材、板块强度和龙头辨识；未加入集合竞价、9:25/9:30确认、自动买入或明确买卖信号。",
        "",
        "## 市场情绪联动",
        "",
        f"- 情绪评分：`{_display(context.get('sentiment_score'))}`",
        f"- 情绪阶段：`{_display(context.get('sentiment_phase'))}`",
        f"- 环境判断：`{_display(context.get('theme_environment'))}`",
        "",
        "## Top10题材榜",
        "",
        "| 排名 | 题材 | 分数 | 角色 | 涨停 | 炸板 | 最高板 | 板块涨幅 | 候选数量 | 人气数量 | 龙头 |",
        "| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    ranked = sorted(payload.get("theme_metrics", {}).values(), key=_theme_sort_key)
    for item in ranked[:10]:
        leader = item.get("leader_stock") or {}
        lines.append(
            f"| {_display(item.get('rank'))} | {_display(item.get('theme_name'))} | {_display(item.get('theme_score'))} | {_display(item.get('theme_role'))} | "
            f"{_display(item.get('limit_up_count'))} | {_display(item.get('broken_board_count'))} | {_display(item.get('highest_board'))} | "
            f"{_display(item.get('board_change_pct'))}% | {_display(item.get('candidate_count'))} | {_display(item.get('hot_stock_count'))} | "
            f"{_display(leader.get('name') or leader.get('code'))} |"
        )
    lines.extend(["", "## 主线题材详细信息", ""])
    for item in ranked[:10]:
        lines.extend([
            f"### {item.get('theme_name')}（{_display(item.get('theme_role'))}）",
            "",
            f"分数：`{_display(item.get('theme_score'))}`；原始分：`{_display(item.get('score_raw'))}`；可用权重：`{_display(item.get('available_weight'))}`；数据质量：`{_display(item.get('data_quality'))}`。",
            f"评分分项：`{_display(item.get('components'))}`",
            "",
        ])
    lines.extend([
        "## 市场龙头榜 Top5",
        "",
        "| 排名 | 代码 | 名称 | 题材 | 角色 | leader_score | 连板数 | 人气排名 | 模型共振 | 理由 |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ])
    for item in payload.get("market_leaders", []):
        lines.append(
            f"| {_display(item.get('market_leader_rank'))} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(item.get('primary_theme'))} | "
            f"{_display(item.get('stock_role'))} | {_display(item.get('leader_score'))} | {_display(item.get('board_count'))} | {_display(item.get('hot_rank'))} | "
            f"{_display(item.get('resonance_count'))} | {_display(item.get('leader_reasons'))} |"
        )
    lines.extend(["", "## 第1阶段候选池增强结果", "", "候选池原始顺序保持不变；完整字段请查看 `candidate_pool_stage3.json`。", ""])
    THEME_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def _write_stage3_markdown(payload: dict[str, Any]) -> None:
    lines = [
        "# A股短线候选池（改造第3阶段）",
        "",
        "> 本文件保留第1阶段候选池原始顺序，只增加题材、行业、主线角色和龙头辨识字段。",
        "",
        "| 原排名 | 代码 | 名称 | 主线题材 | 题材分数 | 题材角色 | 龙头分数 | 股票角色 |",
        "| ---: | --- | --- | --- | ---: | --- | ---: | --- |",
    ]
    for index, item in enumerate(payload.get("candidates", []) or [], start=1):
        if not isinstance(item, dict):
            continue
        analysis = item.get("theme_analysis") or {}
        lines.append(
            f"| {index} | {_display(item.get('code'))} | {_display(item.get('name'))} | {_display(analysis.get('primary_theme'))} | "
            f"{_display(analysis.get('primary_theme_score'))} | {_display(analysis.get('primary_theme_role'))} | {_display(analysis.get('leader_score'))} | {_display(analysis.get('stock_role'))} |"
        )
    STAGE3_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stage-3 theme and leader reports.")
    parser.add_argument("--target-date", default=os.getenv("SHORT_TERM_THEME_DATE", ""), help="Target date in YYYYMMDD.")
    return parser.parse_args()


def main() -> int:
    _configure_logging()
    args = _parse_args()
    try:
        sentiment = _load_json(SENTIMENT_PATH)
        enriched = _load_json(ENRICHED_POOL_PATH)
    except Exception as exc:
        logger.exception("Cannot load stage-2 inputs")
        return 1

    target = _target_date(sentiment, args.target_date)
    original_candidates, candidates = _candidate_map(enriched)
    # Fetch market pools first so the theme universe can fall back to an
    # industry cluster when both concept-board providers are unavailable.
    market, market_sources = _fetch_market_data(target)
    themes, stock_to_themes, stock_to_industries, theme_sources, universe = _fetch_themes(
        target.strftime("%Y%m%d"), market, candidates
    )
    theme_metrics = _build_theme_metrics(themes, candidates, stock_to_themes, market)
    stock_records = _build_stock_records(candidates, stock_to_themes, stock_to_industries, theme_metrics, market)
    leaders, market_leaders = _build_leaders(stock_records, theme_metrics)

    # Re-select primary themes after internal leader scores exist, honoring all
    # four requested tie-breakers without changing candidate list order.
    for stock in stock_records.values():
        theme_scores = {theme: max((item.get("leader_score") for item in leaders if theme in (item.get("themes") or []) and item.get("leader_score") is not None), default=float("-inf")) for theme in stock.get("themes") or []}
        stock["primary_theme"] = _select_primary_theme(stock.get("themes") or [], theme_metrics, theme_scores)
        selected = theme_metrics.get(stock.get("primary_theme") or "", {})
        stock["primary_theme_role"] = selected.get("theme_role")
    leaders, market_leaders = _build_leaders(stock_records, theme_metrics)
    if universe["source_mode"] == "UNAVAILABLE":
        # Candidate data alone is not a market-data substitute.  Preserve the
        # candidate pool, but do not manufacture market leaders without any
        # usable board/hot-rank source.
        leaders = []
        market_leaders = []
    leader_mode = "industry_degraded" if universe["source_mode"] == "INDUSTRY_DEGRADED" else "market_only" if universe["source_mode"] in {"MARKET_ONLY", "UNAVAILABLE"} else "full_theme"
    for stock in stock_records.values():
        stock["leader_source_mode"] = leader_mode if universe["source_mode"] == "INDUSTRY_DEGRADED" or not stock.get("themes") else "full_theme"
    for item in leaders:
        item["leader_source_mode"] = stock_records.get(item.get("code"), {}).get("leader_source_mode", item.get("leader_source_mode"))
    for item in market_leaders:
        item["leader_source_mode"] = stock_records.get(item.get("code"), {}).get("leader_source_mode", item.get("leader_source_mode"))

    current = sentiment.get("current") or {}
    all_sources = universe["sources"] + market_sources
    failures = [source for source in all_sources if source.get("status") == "failed"]
    theme_payload = {
        "phase": "short_term_theme_leader_v1",
        "market": "cn",
        "target_date": target.strftime("%Y%m%d"),
        "market_context": {
            "sentiment_score": current.get("sentiment_score"),
            "sentiment_phase": current.get("sentiment_phase"),
            "theme_environment": _theme_environment(current.get("sentiment_phase")),
        },
        "stock_to_themes": stock_to_themes,
        "stock_to_industries": stock_to_industries,
        "theme_sources": universe["theme_sources"],
        "source_mode": universe["source_mode"],
        "source": universe["source"],
        "data_coverage": universe["data_coverage"],
        "theme_metrics": theme_metrics,
        "main_themes": [
            {
                "rank": item.get("rank"),
                "theme": item.get("theme_name"),
                "theme_score": item.get("theme_score"),
                "confidence_adjusted_score": item.get("confidence_adjusted_score"),
                "coverage_ratio": item.get("coverage_ratio"),
                "theme_role": item.get("theme_role"),
                "data_quality": item.get("data_quality"),
                "is_degraded_main": bool(item.get("is_degraded_main")),
            }
            for item in sorted(theme_metrics.values(), key=_theme_sort_key)[:10]
        ],
        "leaders": leaders,
        "market_leaders": market_leaders,
        "sources": all_sources,
        "source_failures": failures,
        "data_quality": universe["data_quality"],
        "api_stats": dict(_API_STATS),
    }
    stage3 = _enrich_candidates(enriched, stock_records, theme_metrics)
    market_rank = {item["code"]: item["market_leader_rank"] for item in market_leaders}
    for item in stage3.get("candidates", []) or []:
        if isinstance(item, dict):
            analysis = item.get("theme_analysis") or {}
            analysis["market_leader_rank"] = market_rank.get(_normalize_code(item.get("code")))
            item["theme_analysis"] = analysis
    stage3["market_context"] = theme_payload["market_context"]
    stage3["source_failures"] = failures
    _write_json(THEME_JSON_PATH, theme_payload)
    _write_json(STAGE3_JSON_PATH, stage3)
    _write_theme_markdown(theme_payload)
    _write_stage3_markdown(stage3)
    logger.info("Wrote %s, %s, %s, %s", THEME_JSON_PATH, THEME_MD_PATH, STAGE3_JSON_PATH, STAGE3_MD_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
