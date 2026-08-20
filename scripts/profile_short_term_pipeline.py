#!/usr/bin/env python3
"""Inspect Stage1 performance metrics or run an offline merge benchmark.

The production Stage1 runner records the provider timings.  This command is
deliberately offline by default and never calls an A-share endpoint.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def benchmark_fixture(*, repeats: int = 100) -> dict[str, object]:
    from scripts.run_short_term_candidate_pool import _merge_results

    fixture = {
        strategy: {
            "candidates": [
                {
                    "rank": index,
                    "code": code,
                    "name": f"Fixture-{code}",
                    "score": score,
                    "reason": "offline fixture",
                }
                for index, (code, score) in enumerate(
                    [("600001", 90), ("600002", 80), ("600003", 70)],
                    start=1,
                )
            ]
        }
        for strategy in (
            "volume_breakout",
            "capital_heat",
            "momentum_quality",
            "oversold_reversal",
        )
    }
    started = time.perf_counter()
    optimized, _ = _merge_results(fixture)
    elapsed = time.perf_counter() - started
    baseline_codes = ["600001", "600002", "600003"]
    optimized_codes = [item["code"] for item in optimized[:30]]
    return {
        "repeats": repeats,
        "elapsed_seconds": round(elapsed, 6),
        "baseline_codes": baseline_codes,
        "optimized_codes": optimized_codes,
        "top30_consistent": baseline_codes == optimized_codes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect short-term pipeline performance metrics.")
    parser.add_argument(
        "--metrics",
        type=Path,
        default=PROJECT_ROOT / "reports" / "short_term" / "performance_metrics.json",
    )
    parser.add_argument("--fixture", action="store_true", help="Run an offline deterministic merge fixture.")
    args = parser.parse_args()

    if args.fixture:
        print(json.dumps(benchmark_fixture(), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if not args.metrics.is_file():
        print(f"Performance metrics not found: {args.metrics}")
        return 1
    print(args.metrics.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
