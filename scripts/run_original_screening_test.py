#!/usr/bin/env python3
"""Run the built-in screening engine and persist its original response.

This is deliberately a thin test entry point.  The selection strategy, filters,
scoring, ranking, risk, and portfolio logic remain entirely inside
``ScreeningService.screen``.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_ROOT / "reports" / "screening"
JSON_PATH = REPORT_DIR / "original_screening.json"
MARKDOWN_PATH = REPORT_DIR / "original_screening.md"

# ``python scripts/run_original_screening_test.py`` puts ``scripts/`` first on
# sys.path; make the repository package importable without changing the app.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

logger = logging.getLogger("original_screening_test")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the original stock screening engine.")
    parser.add_argument(
        "--strategy",
        default=os.getenv("SCREENING_STRATEGY", "balanced_alpha"),
        help="Screening strategy name (default: balanced_alpha).",
    )
    parser.add_argument(
        "--market",
        default=os.getenv("SCREENING_MARKET", "cn"),
        help="Market scope (default: cn).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=int(os.getenv("SCREENING_MAX_RESULTS", "10")),
        help="Maximum number of returned candidates (default: 10).",
    )
    return parser.parse_args()


def _json_safe(value: Any) -> Any:
    """Convert incidental dataclass/path values without changing engine data."""
    if is_dataclass(value):
        return _json_safe(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _display(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    return str(value).replace("\n", " ").replace("|", "\\|")


def _candidate_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    for key in ("candidates", "results", "items"):
        value = result.get(key)
        if isinstance(value, list):
            return [item if isinstance(item, dict) else {"value": item} for item in value]
    return []


def _candidate_value(candidate: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = candidate.get(key)
        if value is not None and value != "":
            return value
    raw = candidate.get("raw")
    if isinstance(raw, dict):
        for key in keys:
            value = raw.get(key)
            if value is not None and value != "":
                return value
    return None


def _risk_text(candidate: dict[str, Any]) -> str:
    risk_parts = []
    for key in ("risk_summary", "risk_level", "risk_flags", "llm_risks", "llm_watch_items", "llm_invalidators"):
        value = _candidate_value(candidate, key)
        if value not in (None, "", [], {}):
            risk_parts.append(f"{key}: {_display(value)}")
    return "；".join(risk_parts) or "未提供"


def _build_markdown(result: dict[str, Any], *, requested_strategy: str, requested_market: str) -> str:
    strategy = result.get("strategy") or requested_strategy
    market = result.get("market") or requested_market
    candidates = _candidate_rows(result)
    candidate_count = result.get("candidate_count")
    if candidate_count is None:
        candidate_count = len(candidates)

    lines = [
        "# 原版自动选股测试报告",
        "",
        "> 本报告直接调用 `src.services.screening_service.ScreeningService.screen()`；未传入 `selection_seed`，未复制或改写原选股算法。",
        "",
        "## 测试概况",
        "",
        f"- 选股策略：`{_display(strategy)}`",
        f"- 市场：`{_display(market)}`",
        f"- 实际候选数量：`{_display(candidate_count)}`",
    ]

    for key in (
        "run_id",
        "snapshot_count",
        "after_filter_count",
        "snapshot_source",
        "ranking_mode",
        "llm_ranked",
        "llm_model_used",
        "llm_coverage",
        "risk_enabled",
        "portfolio_diversity_enabled",
        "result_variant_applied",
        "result_variant_pool_size",
        "result_variant_rotated_slots",
    ):
        if key in result:
            lines.append(f"- {key}：`{_display(result.get(key))}`")

    lines.extend(["", "## 入选股票", ""])
    if candidates:
        lines.extend([
            "| 排名 | 股票代码 | 股票名称 | 最终评分 | 入选理由 | 风险提示 |",
            "| ---: | --- | --- | ---: | --- | --- |",
        ])
        for index, candidate in enumerate(candidates, start=1):
            rank = _candidate_value(candidate, "rank") or index
            code = _candidate_value(candidate, "code", "symbol", "stock_code")
            name = _candidate_value(candidate, "name", "stock_name")
            score = _candidate_value(candidate, "score", "final_score")
            reason = _candidate_value(candidate, "reason", "ranking_reason", "summary") or "未提供"
            lines.append(
                f"| {_display(rank)} | {_display(code)} | {_display(name)} | {_display(score)} | "
                f"{_display(reason)} | {_display(_risk_text(candidate))} |"
            )
    else:
        lines.append("未返回候选股票。")

    lines.extend(["", "## 原版系统返回的其他关键字段", ""])
    excluded_keys = {"candidates", "results", "items"}
    other_fields = {key: value for key, value in result.items() if key not in excluded_keys}
    if other_fields:
        lines.extend([
            "```json",
            json.dumps(_json_safe(other_fields), ensure_ascii=False, indent=2, sort_keys=True),
            "```",
        ])
    else:
        lines.append("无其他顶层字段。")

    lines.extend(["", "## 候选原始字段补充", ""])
    lines.append("完整返回结构请以同目录的 `original_screening.json` 为准。")
    if candidates:
        lines.extend(["", "```json", json.dumps(_json_safe(candidates), ensure_ascii=False, indent=2), "```"])
    lines.append("")
    return "\n".join(lines)


def _write_outputs(payload: dict[str, Any], markdown: str) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(
        json.dumps(_json_safe(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    MARKDOWN_PATH.write_text(markdown, encoding="utf-8")
    logger.info("Wrote screening JSON: %s", JSON_PATH)
    logger.info("Wrote screening Markdown: %s", MARKDOWN_PATH)


def main() -> int:
    _configure_logging()
    args = _parse_args()
    if args.max_results < 1:
        raise SystemExit("--max-results must be at least 1")

    # Set this before obtaining Config: the global Config is a singleton and
    # reads SCREENING_ENABLED during _load_from_env().
    os.environ["SCREENING_ENABLED"] = "true"

    config = None
    try:
        from src.config import Config
        from src.services.screening_service import ScreeningService

        Config.reset_instance()
        config = Config.get_instance()
        logger.info(
            "Starting original screening: strategy=%s market=%s max_results=%s screening_enabled=%s",
            args.strategy,
            args.market,
            args.max_results,
            config.screening_enabled,
        )
        if not config.screening_enabled:
            raise RuntimeError("SCREENING_ENABLED=true was not reflected by Config")

        # Intentionally call the service layer exactly as the application does.
        # Do not pass selection_seed: an empty seed would still be harmless, but
        # omitting it makes the no-perturbation intent explicit.
        result = ScreeningService(config=config).screen(
            strategy=args.strategy,
            market=args.market,
            max_results=args.max_results,
        )
        payload = _json_safe(result)
        if not isinstance(payload, dict):
            payload = {"result": payload}
        markdown = _build_markdown(payload, requested_strategy=args.strategy, requested_market=args.market)
        _write_outputs(payload, markdown)
        logger.info("Original screening completed with %s candidates", len(_candidate_rows(payload)))
        return 0
    except Exception as exc:  # Keep failure details in the artifact for Actions diagnostics.
        logger.exception("Original screening failed")
        payload = {
            "enabled": bool(getattr(config, "screening_enabled", False)),
            "strategy": args.strategy,
            "market": args.market,
            "candidate_count": 0,
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }
        markdown = _build_markdown(payload, requested_strategy=args.strategy, requested_market=args.market)
        _write_outputs(payload, markdown)
        return 1


if __name__ == "__main__":
    sys.exit(main())
