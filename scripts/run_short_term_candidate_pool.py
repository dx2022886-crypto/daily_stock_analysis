#!/usr/bin/env python3
"""Build a short-term candidate pool from four original screening strategies.

This entry point only orchestrates the existing ScreeningService.  It does not
change any strategy, factor, filter, ranking, risk, or portfolio logic.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import os
import re
import sys
import time
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "short_term"
JSON_PATH = REPORT_DIR / "candidate_pool.json"
MARKDOWN_PATH = REPORT_DIR / "candidate_pool.md"
PERFORMANCE_PATH = REPORT_DIR / "performance_metrics.json"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

STRATEGIES = (
    "volume_breakout",
    "capital_heat",
    "momentum_quality",
    "oversold_reversal",
)
STRATEGY_LABELS = {
    "volume_breakout": "放量突破",
    "capital_heat": "资金热度",
    "momentum_quality": "动量质量",
    "oversold_reversal": "超跌反转",
}

logger = logging.getLogger("short_term_candidate_pool")
SHANGHAI = ZoneInfo("Asia/Shanghai")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def _json_safe(value: Any) -> Any:
    if is_dataclass(value):
        return _json_safe(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def _display(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    return str(value).replace("\n", " ").replace("|", "\\|")


def _parse_positive_int(raw: str | None, *, name: str, default: int) -> int:
    value = raw if raw not in (None, "") else str(default)
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a positive integer, got {value!r}") from exc
    if parsed < 1:
        raise ValueError(f"{name} must be a positive integer, got {parsed}")
    return parsed


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the short-term multi-strategy candidate pool.")
    parser.add_argument(
        "--per-strategy-results",
        type=int,
        default=_parse_positive_int(
            os.getenv("SHORT_TERM_PER_STRATEGY_RESULTS"),
            name="SHORT_TERM_PER_STRATEGY_RESULTS",
            default=10,
        ),
        help="Maximum candidates requested from each original strategy (default: 10).",
    )
    parser.add_argument(
        "--max-pool-results",
        type=int,
        default=_parse_positive_int(
            os.getenv("SHORT_TERM_MAX_POOL_RESULTS"),
            name="SHORT_TERM_MAX_POOL_RESULTS",
            default=30,
        ),
        help="Maximum candidates written to the ranked pool (default: 30).",
    )
    parser.add_argument(
        "--market",
        default=os.getenv("SCREENING_MARKET", "cn"),
        help="Market passed to the original screening service (default: cn).",
    )
    args = parser.parse_args()
    if args.per_strategy_results < 1:
        parser.error("--per-strategy-results must be at least 1")
    if args.max_pool_results < 1:
        parser.error("--max-pool-results must be at least 1")
    return args


def _normalize_code(value: Any) -> str:
    """Normalize common A-share code forms to six digits."""
    text = str(value or "").strip().upper().replace(" ", "")
    if not text:
        return ""

    prefix_match = re.fullmatch(r"(?:SH|SZ|BJ)(\d{1,6})", text)
    suffix_match = re.fullmatch(r"(\d{1,6})\.(?:SH|SZ|BJ)", text)
    plain_match = re.fullmatch(r"\d{1,6}", text)
    digits = None
    if prefix_match:
        digits = prefix_match.group(1)
    elif suffix_match:
        digits = suffix_match.group(1)
    elif plain_match:
        digits = plain_match.group(0)
    if digits is None:
        return ""
    return digits.zfill(6)


def _first_present(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = mapping.get(key)
        if value is not None and value != "":
            return value
    return None


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _candidate_list(result: Any) -> list[dict[str, Any]]:
    if not isinstance(result, dict):
        return []
    for key in ("candidates", "results", "items"):
        value = result.get(key)
        if isinstance(value, list):
            return [item if isinstance(item, dict) else {"value": item} for item in value]
    return []


def _merge_results(
    strategy_results: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    merged: dict[str, dict[str, Any]] = {}
    invalid_codes = {strategy: 0 for strategy in STRATEGIES}

    for strategy in STRATEGIES:
        result = strategy_results.get(strategy, {})
        for fallback_rank, candidate in enumerate(_candidate_list(result), start=1):
            raw_candidate = _json_safe(candidate)
            if not isinstance(raw_candidate, dict):
                raw_candidate = {"value": raw_candidate}
            raw_source = raw_candidate.get("raw")
            if not isinstance(raw_source, dict):
                raw_source = {}
            code = _normalize_code(
                _first_present(raw_candidate, "code", "symbol", "stock_code")
                or _first_present(raw_source, "code", "symbol", "stock_code")
            )
            if not code:
                invalid_codes[strategy] += 1
                continue

            rank_value = _first_present(raw_candidate, "rank") or fallback_rank
            rank_number = _number(rank_value)
            score_value = _first_present(raw_candidate, "score", "final_score")
            reason = _first_present(raw_candidate, "reason", "ranking_reason", "summary")
            name = _first_present(raw_candidate, "name", "stock_name")
            details = {
                "rank": rank_value,
                "score": score_value,
                "reason": reason or "",
                "raw_candidate": raw_candidate,
            }
            row = merged.setdefault(
                code,
                {
                    "code": code,
                    "name": name or "",
                    "resonance_count": 0,
                    "strategies": [],
                    "strategy_labels": [],
                    "best_rank": None,
                    "best_score": None,
                    "average_score": None,
                    "strategy_details": {},
                },
            )
            if not row["name"] and name:
                row["name"] = name
            if strategy in row["strategy_details"]:
                continue
            row["strategies"].append(strategy)
            row["strategy_labels"].append(STRATEGY_LABELS[strategy])
            row["resonance_count"] = len(row["strategies"])
            row["strategy_details"][strategy] = details

    for row in merged.values():
        details = row["strategy_details"]
        ranked = [(_number(detail.get("rank")), detail) for detail in details.values()]
        ranked = [(rank, detail) for rank, detail in ranked if rank is not None]
        scored = [(_number(detail.get("score")), detail) for detail in details.values()]
        scored = [(score, detail) for score, detail in scored if score is not None]
        scores = [score for score, _ in scored]
        row["average_score"] = round(sum(scores) / len(scores), 6) if scores else None
        if ranked:
            best_rank, _ = min(ranked, key=lambda item: item[0])
            row["best_rank"] = int(best_rank) if best_rank.is_integer() else best_rank
        if scored:
            _, best_detail = max(scored, key=lambda item: item[0])
            row["best_score"] = best_detail.get("score")

    ordered = sorted(
        merged.values(),
        key=lambda row: (
            -int(row.get("resonance_count") or 0),
            -(row.get("average_score") if row.get("average_score") is not None else float("-inf")),
            row.get("best_rank") if row.get("best_rank") is not None else float("inf"),
            row.get("code", ""),
        ),
    )
    return ordered, invalid_codes


def _build_markdown(payload: dict[str, Any]) -> str:
    candidates = payload.get("candidates") or []
    lines = [
        "# 《A股短线候选池（改造第1阶段）》",
        "",
        "> 本报告只做四套原版模型自动合并、去重和模型共振统计；尚未加入题材、涨停梯队、市场情绪、竞价和开盘确认。",
        "",
        "## 测试概况",
        "",
        f"- 阶段：`{_display(payload.get('phase'))}`",
        f"- 市场：`{_display(payload.get('market'))}`",
        f"- 每套模型返回数量：`{_display(payload.get('per_strategy_results'))}`",
        f"- 合并去重后的候选数量：`{_display(payload.get('merged_candidate_count'))}`",
        f"- 报告输出数量：`{_display(len(candidates))}`",
        "",
        "## 模型运行状态",
        "",
        "| 模型 | 标签 | 状态 | 候选数量 |",
        "| --- | --- | --- | ---: |",
    ]
    strategy_runs = payload.get("strategy_runs") or {}
    for strategy in STRATEGIES:
        run = strategy_runs.get(strategy) or {}
        lines.append(
            f"| `{strategy}` | {_display(STRATEGY_LABELS[strategy])} | "
            f"{_display(run.get('status'))} | {_display(run.get('candidate_count', 0))} |"
        )
        if run.get("error"):
            lines.append(f"| 失败原因 |  | {_display(run.get('error'))} |  |")

    lines.extend([
        "",
        "## 候选池优先级",
        "",
        "排序依次为：共振模型数量（降序）、多个模型平均原始评分（降序）、最佳模型排名（升序）。这里的排序仅表示候选池优先级，不是买入评分。",
        "",
        "| 排名 | 股票代码 | 股票名称 | 共振数 | 入选模型 | 平均原始分 | 最佳名次 |",
        "| ---: | --- | --- | ---: | --- | ---: | ---: |",
    ])
    if candidates:
        for index, candidate in enumerate(candidates, start=1):
            lines.append(
                f"| {index} | {_display(candidate.get('code'))} | {_display(candidate.get('name'))} | "
                f"{_display(candidate.get('resonance_count'))} | "
                f"{_display('、'.join(candidate.get('strategy_labels') or []))} | "
                f"{_display(candidate.get('average_score'))} | {_display(candidate.get('best_rank'))} |"
            )
    else:
        lines.append("| — | — | 未返回有效候选 | 0 | — | — | — |")

    lines.extend([
        "",
        "## 模型明细与原始候选字段",
        "",
        "完整的每套模型返回结果、每只股票的原始候选字段和策略明细请以同目录的 `candidate_pool.json` 为准。",
        "",
        "```json",
        json.dumps(_json_safe(payload.get("candidates") or []), ensure_ascii=False, indent=2),
        "```",
        "",
    ])
    return "\n".join(lines)


def _write_outputs(payload: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    safe_payload = _json_safe(payload)
    JSON_PATH.write_text(
        json.dumps(safe_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    MARKDOWN_PATH.write_text(_build_markdown(safe_payload), encoding="utf-8")
    logger.info("Wrote candidate pool JSON: %s", JSON_PATH)
    logger.info("Wrote candidate pool Markdown: %s", MARKDOWN_PATH)


def _write_performance(metrics: dict[str, Any]) -> None:
    """Write profiling diagnostics without ever failing the screening run."""
    try:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        PERFORMANCE_PATH.write_text(
            json.dumps(_json_safe(metrics), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except Exception as exc:  # pragma: no cover - defensive reporting path
        logger.warning("Unable to write performance metrics: %s", exc)


def _target_date() -> str:
    raw = os.getenv("SHORT_TERM_TARGET_DATE", "").strip().replace("-", "").replace("/", "")
    if len(raw) == 8 and raw.isdigit():
        return raw
    try:
        import exchange_calendars as xcals

        now = datetime.now(SHANGHAI)
        calendar = xcals.get_calendar("XSHG")
        session = calendar.date_to_session(now.date(), direction="previous")
        if session.date() == now.date() and (now.hour, now.minute) < (15, 5):
            session = calendar.previous_session(session)
        return session.strftime("%Y%m%d")
    except Exception:
        return datetime.now(SHANGHAI).strftime("%Y%m%d")


def _prefetch_shared_snapshot(config: Any, market: str, run_context: Any) -> None:
    """Fetch one union-column snapshot before the four strategy calls."""
    from src.services.screening.filter import requires_daily_features, without_daily_filters
    from src.services.screening.pipeline import _required_snapshot_columns
    from src.services.screening.snapshot import fetch_snapshot_with_fallback
    from src.services.screening.strategy import load_all_strategies

    strategies = load_all_strategies(config.strategies_dir)
    required_columns: set[str] = set()
    for strategy in STRATEGIES:
        screening = strategies[strategy].screening
        filters = (
            without_daily_filters(screening.hard_filters)
            if requires_daily_features(screening.hard_filters)
            else screening.hard_filters
        )
        required_columns.update(_required_snapshot_columns(filters))

    run_context.load_snapshot(
        lambda: fetch_snapshot_with_fallback(
            config.snapshot_source_priority,
            required_columns=sorted(required_columns),
            fallback_snapshot_path=config.fallback_snapshot_path,
            fallback_max_age_hours=config.snapshot_fallback_max_age_hours,
            cache_ttl_seconds=config.snapshot_cache_ttl_seconds,
            market=market,
        )
    )


def main() -> int:
    _configure_logging()
    started_at = datetime.now(SHANGHAI)
    started_perf = time.perf_counter()
    args = _parse_args()
    os.environ["SCREENING_ENABLED"] = "true"
    os.environ.setdefault("SHORT_TERM_STAGE1_LLM_RANKING", "true")
    os.environ.setdefault("SHORT_TERM_STAGE1_NEWS_ENABLED", "false")

    strategy_runs: dict[str, dict[str, Any]] = {}
    strategy_results: dict[str, dict[str, Any]] = {}
    service = None
    config = None
    run_context = None
    performance: dict[str, Any] = {
        "stage": "stage1",
        "started_at": started_at.isoformat(timespec="seconds"),
        "strategy_seconds": {},
    }

    try:
        from src.config import Config
        from src.services.screening_service import ScreeningService

        Config.reset_instance()
        config = Config.get_instance()
        if not config.screening_enabled:
            raise RuntimeError("SCREENING_ENABLED=true was not reflected by Config")
        service = ScreeningService(config=config)
        from src.services.screening.run_context import ShortTermRunContext

        run_context = ShortTermRunContext(market=args.market, target_date=_target_date())
        try:
            _prefetch_shared_snapshot(config, args.market, run_context)
        except Exception as exc:
            # Preserve the original per-strategy fallback path if the eager
            # prefetch itself fails.
            logger.warning("Shared snapshot prefetch failed; using engine fallback: %s", exc)
    except Exception as exc:
        logger.exception("Unable to initialize the original screening service")
        for strategy in STRATEGIES:
            strategy_runs[strategy] = {
                "status": "failed",
                "candidate_count": 0,
                "error": {"type": type(exc).__name__, "message": str(exc)},
            }

    if service is not None:
        for strategy in STRATEGIES:
            logger.info(
                "Running original screening strategy=%s market=%s max_results=%s",
                strategy,
                args.market,
                args.per_strategy_results,
            )
            try:
                # Deliberately omit selection_seed: this is a direct, unperturbed
                # call to the original service for each strategy.
                strategy_started = time.perf_counter()
                result = service.screen(
                    strategy=strategy,
                    market=args.market,
                    max_results=args.per_strategy_results,
                    run_context=run_context,
                )
                performance["strategy_seconds"][strategy] = round(
                    time.perf_counter() - strategy_started,
                    6,
                )
                safe_result = _json_safe(result)
                if not isinstance(safe_result, dict):
                    safe_result = {"candidates": safe_result}
                strategy_results[strategy] = safe_result
                strategy_runs[strategy] = {
                    "status": "success",
                    "candidate_count": len(_candidate_list(safe_result)),
                    "raw_result": safe_result,
                }
                logger.info("Strategy %s returned %s candidates", strategy, len(_candidate_list(safe_result)))
            except Exception as exc:  # Keep other strategy results available.
                performance["strategy_seconds"][strategy] = round(
                    time.perf_counter() - strategy_started,
                    6,
                )
                logger.exception("Strategy %s failed", strategy)
                strategy_runs[strategy] = {
                    "status": "failed",
                    "candidate_count": 0,
                    "error": {"type": type(exc).__name__, "message": str(exc)},
                }

    merge_started = time.perf_counter()
    candidates, invalid_codes = _merge_results(strategy_results)
    performance["merge_seconds"] = round(time.perf_counter() - merge_started, 6)
    merged_candidate_count = len(candidates)
    candidates = candidates[: args.max_pool_results]
    successful_runs = sum(1 for run in strategy_runs.values() if run.get("status") == "success")
    payload = {
        "phase": "short_term_candidate_pool_v1",
        "market": args.market,
        "strategies": list(STRATEGIES),
        "strategy_labels": dict(STRATEGY_LABELS),
        "per_strategy_results": args.per_strategy_results,
        "max_pool_results": args.max_pool_results,
        "target_date": _target_date(),
        "merged_candidate_count": merged_candidate_count,
        "returned_candidate_count": len(candidates),
        "successful_strategy_count": successful_runs,
        "strategy_runs": strategy_runs,
        "invalid_code_counts": invalid_codes,
        "candidates": candidates,
    }
    _write_outputs(payload)

    if run_context is not None:
        performance.update(run_context.metrics())
    performance["finished_at"] = datetime.now(SHANGHAI).isoformat(timespec="seconds")
    performance["total_seconds"] = round(time.perf_counter() - started_perf, 6)
    performance["llm_ranking_enabled"] = os.getenv("SHORT_TERM_STAGE1_LLM_RANKING", "true")
    performance["news_enabled"] = os.getenv("SHORT_TERM_STAGE1_NEWS_ENABLED", "false")
    for metric_name in (
        "snapshot_fetch_seconds",
        "history_fetch_seconds",
        "realtime_quote_seconds",
        "llm_rank_seconds",
        "news_search_seconds",
        "merge_seconds",
    ):
        performance.setdefault(metric_name, 0.0)
    performance.setdefault("cache_stats", {})
    performance.setdefault("data_source_stats", {})
    _write_performance(performance)

    if successful_runs == 0:
        logger.error("All four original screening strategies failed")
        return 1
    logger.info("Short-term candidate pool completed with %s candidates", len(candidates))
    return 0


if __name__ == "__main__":
    sys.exit(main())
