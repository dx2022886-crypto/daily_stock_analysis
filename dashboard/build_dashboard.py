#!/usr/bin/env python3
"""Build the static Stage1-Stage5 short-term decision dashboard.

This module only reads the stable ``reports/short_term/latest_stageX``
snapshots.  It never calls a data source, changes a stage result, or applies a
new score.  Missing snapshots are represented explicitly as unavailable data.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORTS_ROOT = PROJECT_ROOT / "reports" / "short_term"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "docs"
TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "index.html"

STAGE_FILES: dict[str, tuple[str, ...]] = {
    "stage1": ("candidate_pool.json", "candidate_pool.md"),
    "stage2": (
        "market_sentiment.json",
        "market_sentiment.md",
        "candidate_pool_enriched.json",
        "candidate_pool_enriched.md",
    ),
    "stage3": (
        "theme_leader.json",
        "theme_leader.md",
        "candidate_pool_stage3.json",
        "candidate_pool_stage3.md",
    ),
    "stage4": (
        "weak_to_strong.json",
        "weak_to_strong.md",
        "candidate_pool_stage4.json",
        "candidate_pool_stage4.md",
    ),
    "stage5": (
        "auction_confirmation.json",
        "auction_confirmation.md",
        "candidate_pool_stage5.json",
        "candidate_pool_stage5.md",
    ),
}

ROLE_PRIORITY = {
    "MARKET_LEADER": 6,
    "THEME_LEADER": 5,
    "FRONT_CORE": 4,
    "BROKEN_CORE": 3,
    "FOLLOWER": 2,
    "OBSERVE": 1,
}


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain an object")
    return payload


def _load_stage(reports_root: Path, stage: str) -> dict[str, Any]:
    latest_dir = reports_root / f"latest_{stage}"
    files = STAGE_FILES[stage]
    if not latest_dir.is_dir():
        return {"available": False, "stage": stage, "latest_dir": str(latest_dir), "data": {}, "metadata": {}}
    data: dict[str, Any] = {}
    for filename in files:
        path = latest_dir / filename
        if filename.endswith(".json") and path.is_file():
            try:
                data[filename] = _read_json(path)
            except (OSError, ValueError, json.JSONDecodeError):
                return {"available": False, "stage": stage, "latest_dir": str(latest_dir), "data": {}, "metadata": {}}
    metadata: dict[str, Any] = {}
    metadata_path = latest_dir / "metadata.json"
    if metadata_path.is_file():
        try:
            metadata = _read_json(metadata_path)
        except (OSError, ValueError, json.JSONDecodeError):
            metadata = {}
    available = all(filename in data for filename in files if filename.endswith(".json"))
    return {
        "available": available,
        "stage": stage,
        "latest_dir": str(latest_dir),
        "data": data if available else {},
        "metadata": metadata,
    }


def _first(mapping: dict[str, Any] | None, *keys: str) -> Any:
    if not isinstance(mapping, dict):
        return None
    for key in keys:
        value = mapping.get(key)
        if value is not None and value != "":
            return value
    return None


def _list(value: Any) -> list[dict[str, Any]]:
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def _number(value: Any) -> float | int | None:
    if value is None or value == "":
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return int(number) if number.is_integer() else number


def _stage_date(stage: dict[str, Any]) -> str | None:
    metadata = stage.get("metadata") or {}
    payloads = stage.get("data") or {}
    for payload in payloads.values():
        if isinstance(payload, dict):
            value = _first(payload, "target_date", "date", "market_ecology_date")
            if value:
                return str(value)
            current = payload.get("current")
            if isinstance(current, dict) and current.get("date"):
                return str(current["date"])
    return str(metadata.get("target_date")) if metadata.get("target_date") else None


def _market(stage2: dict[str, Any]) -> dict[str, Any]:
    payload = (stage2.get("data") or {}).get("market_sentiment.json") or {}
    current = payload.get("current") or {}
    quality = payload.get("data_quality") or "unavailable"
    return {
        "available": bool(stage2.get("available")),
        "date": _first(payload, "target_date") or _first(current, "date"),
        "updated_at": (stage2.get("metadata") or {}).get("generated_at"),
        "sentiment_phase": _first(current, "sentiment_phase") or "UNKNOWN",
        "sentiment_phase_code": _first(current, "sentiment_phase_code") or "UNKNOWN",
        "sentiment_score": _number(_first(current, "sentiment_score")),
        "limit_up_count": _number(_first(current, "limit_up_count")),
        "limit_down_count": _number(_first(current, "limit_down_count")),
        "broken_board_count": _number(_first(current, "broken_board_count")),
        "broken_board_rate": _first(current, "broken_board_rate"),
        "highest_board": _number(_first(current, "highest_board")),
        "highest_board_stocks": _first(current, "highest_board_stocks") or [],
        "yesterday_premium_median": _first(current, "yesterday_premium_median"),
        "data_quality": quality,
        "data_available": bool(stage2.get("available")),
    }


def _themes(stage3: dict[str, Any]) -> list[dict[str, Any]]:
    payload = (stage3.get("data") or {}).get("theme_leader.json") or {}
    result: list[dict[str, Any]] = []
    for item in _list(payload.get("main_themes"))[:5]:
        result.append({
            "rank": item.get("rank"),
            "theme": _first(item, "theme", "theme_name"),
            "theme_role": item.get("theme_role"),
            "theme_score": _number(item.get("theme_score")),
            "confidence_adjusted": _number(_first(item, "confidence_adjusted", "confidence_adjusted_score")),
            "coverage": _first(item, "coverage", "coverage_ratio"),
            "degraded": bool(item.get("is_degraded_main") or item.get("data_quality") in {"partial", "degraded"}),
        })
    return result


def _merge_leaders(stage3: dict[str, Any]) -> list[dict[str, Any]]:
    payload = (stage3.get("data") or {}).get("theme_leader.json") or {}
    by_code: dict[str, dict[str, Any]] = {}
    for source_name in ("market_leaders", "leaders"):
        for item in _list(payload.get(source_name)):
            code = str(_first(item, "code", "symbol", "stock_code") or "").strip()
            if not code:
                continue
            role = item.get("stock_role") or ("MARKET_LEADER" if source_name == "market_leaders" else None)
            current = by_code.setdefault(code, {"code": code})
            if ROLE_PRIORITY.get(str(role), 0) > ROLE_PRIORITY.get(str(current.get("stock_role")), 0):
                current["stock_role"] = role
            for key in ("name", "primary_theme", "theme", "leader_score", "market_leader_rank", "leader_reasons"):
                value = item.get(key)
                if key == "primary_theme" and value is None:
                    value = item.get("theme")
                if value is not None and current.get(key) is None:
                    current[key] = value
            if _number(item.get("leader_score")) is not None:
                current["leader_score"] = max(_number(current.get("leader_score")) or float("-inf"), _number(item["leader_score"]) or float("-inf"))
            rank = _number(item.get("market_leader_rank"))
            if rank is not None:
                current["market_leader_rank"] = min(_number(current.get("market_leader_rank")) or rank, rank)
    ordered = list(by_code.values())
    ordered.sort(key=lambda item: (ROLE_PRIORITY.get(str(item.get("stock_role")), 0), -(float(item.get("leader_score") or 0)), item.get("code", "")), reverse=True)
    return ordered[:10]


def _stage1_candidates(stage1: dict[str, Any]) -> list[dict[str, Any]]:
    payload = (stage1.get("data") or {}).get("candidate_pool.json") or {}
    result: list[dict[str, Any]] = []
    for index, item in enumerate(_list(payload.get("candidates"))[:30], start=1):
        result.append({
            "rank": item.get("rank") or index,
            "code": item.get("code"),
            "name": item.get("name"),
            "resonance_count": item.get("resonance_count"),
            "strategies": item.get("strategies") or [],
            "average_score": _first(item, "average_score", "average_raw_score"),
        })
    return result


def _stage4_data(stage4: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    payload = (stage4.get("data") or {}).get("weak_to_strong.json") or {}
    watchlist: list[dict[str, Any]] = []
    for item in _list(payload.get("next_day_watchlist")):
        watchlist.append({
            "rank": item.get("rank"),
            "code": item.get("code"),
            "name": item.get("name"),
            "theme": _first(item, "primary_theme", "theme"),
            "stock_role": item.get("stock_role"),
            "setup_type": item.get("setup_type"),
            "weak_to_strong_score": _first(item, "final_weak_to_strong_score", "weak_to_strong_score"),
            "grade": _first(item, "setup_grade", "grade"),
        })
    core: list[dict[str, Any]] = []
    for item in _list(payload.get("weak_to_strong_states")):
        if item.get("stock_role") not in {"MARKET_LEADER", "THEME_LEADER", "FRONT_CORE"}:
            continue
        core.append({
            "code": item.get("code"),
            "name": item.get("name"),
            "theme": _first(item, "primary_theme", "theme"),
            "stock_role": item.get("stock_role"),
            "setup_type": item.get("setup_type"),
            "weak_to_strong_score": _first(item, "final_weak_to_strong_score", "weak_to_strong_score"),
            "grade": _first(item, "setup_grade", "grade"),
        })
    return watchlist, core[:10]


def _stage5_data(stage5: dict[str, Any]) -> dict[str, Any]:
    payload = (stage5.get("data") or {}).get("auction_confirmation.json") or {}
    quality = payload.get("snapshot_quality") or {}
    watchlist = payload.get("auction_watchlist") if isinstance(payload.get("auction_watchlist"), list) else []
    candidates = []
    for item in _list(watchlist)[:5]:
        candidates.append({
            "rank": item.get("rank"),
            "code": item.get("code"),
            "name": item.get("name"),
            "theme": _first(item, "primary_theme", "theme"),
            "stock_role": item.get("stock_role"),
            "auction_score": _first(item, "final_auction_score", "auction_score", "final_score"),
            "auction_grade": item.get("auction_grade"),
            "data_mode": _first(item, "auction_data_mode", "data_mode"),
            "coverage": _first(item, "coverage_ratio", "coverage"),
            "hard_reject_reasons": item.get("hard_reject_reasons") or [],
            "qualified": item.get("auction_qualified", True),
        })
    mode = payload.get("source_mode")
    if not mode and candidates:
        mode = candidates[0].get("data_mode")
    return {
        "available": bool(stage5.get("available")),
        "snapshot_quality": quality,
        "snapshot_quality_label": quality.get("quality") or "UNKNOWN",
        "quality_warning": (quality.get("quality") or "UNKNOWN") != "GOOD",
        "captured_count": quality.get("captured_count"),
        "independent_request_count": quality.get("independent_request_count"),
        "cache_reused_count": quality.get("cache_reused_count"),
        "auction_data_mode": mode or "UNKNOWN",
        "candidates": candidates,
        "data_quality": payload.get("data_quality") or "unavailable",
    }


def _decision_state(status: dict[str, bool]) -> str:
    if status.get("stage5"):
        return "集合竞价确认完成，等待开盘确认 Stage6"
    if status.get("stage4") and status.get("stage3") and status.get("stage2") and status.get("stage1"):
        return "盘后候选已完成，等待下一交易日集合竞价"
    if status.get("stage3") and status.get("stage2") and status.get("stage1"):
        return "主线与龙头已确认，等待弱转强筛选"
    if status.get("stage2") and status.get("stage1"):
        return "候选池与市场情绪已生成，等待主线识别"
    if status.get("stage1"):
        return "候选池已生成，等待市场情绪和主线确认"
    return "暂无最新数据，等待阶段结果生成"


def build_dashboard(*, reports_root: Path = DEFAULT_REPORTS_ROOT, output_dir: Path = DEFAULT_OUTPUT_DIR) -> dict[str, Any]:
    stages = {stage: _load_stage(reports_root, stage) for stage in STAGE_FILES}
    available = {stage: bool(value.get("available")) for stage, value in stages.items()}
    data: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market": _market(stages["stage2"]),
        "themes": _themes(stages["stage3"]),
        "leaders": _merge_leaders(stages["stage3"]),
        "stage1_candidates": _stage1_candidates(stages["stage1"]),
        "stage4_watchlist": _stage4_data(stages["stage4"])[0],
        "stage4_core_states": _stage4_data(stages["stage4"])[1],
        "stage5": _stage5_data(stages["stage5"]),
        "pipeline_status": {
            "stages": available,
            "latest_dirs": {stage: value.get("latest_dir") for stage, value in stages.items()},
            "updated_at": {stage: (value.get("metadata") or {}).get("generated_at") for stage, value in stages.items()},
            "current_stage": max((stage for stage, ok in available.items() if ok), default=None),
        },
    }
    data["decision_state"] = _decision_state(available)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "dashboard_data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    (output_dir / "index.html").write_text(template, encoding="utf-8")
    return data


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the static short-term decision dashboard.")
    parser.add_argument("--reports-root", type=Path, default=DEFAULT_REPORTS_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    result = build_dashboard(reports_root=args.reports_root, output_dir=args.output_dir)
    print(f"Dashboard generated: {args.output_dir} current_stage={result['pipeline_status']['current_stage'] or 'none'}")
