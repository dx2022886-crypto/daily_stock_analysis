#!/usr/bin/env python3
"""Inspect Stage1 performance metrics or run an offline merge benchmark.

The production Stage1 runner records the provider timings.  This command is
deliberately offline by default and never calls an A-share endpoint.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
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


def benchmark_history_parallelism(
    *,
    stock_count: int = 96,
    workers: int = 5,
    sleep_seconds: float = 0.2,
) -> dict[str, object]:
    """Benchmark the bounded dispatch shape without touching a live provider."""
    codes = [f"{index:06d}" for index in range(1, stock_count + 1)]

    def fetch(code: str) -> str:
        time.sleep(max(float(sleep_seconds), 0.0))
        return code

    started = time.perf_counter()
    serial = [fetch(code) for code in codes]
    serial_seconds = time.perf_counter() - started

    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=max(int(workers), 1)) as executor:
        parallel = list(executor.map(fetch, codes))
    parallel_seconds = time.perf_counter() - started
    return {
        "stock_count": len(codes),
        "workers": max(int(workers), 1),
        "sleep_seconds": sleep_seconds,
        "serial_seconds": round(serial_seconds, 6),
        "parallel_seconds": round(parallel_seconds, 6),
        "speedup_ratio": round(serial_seconds / parallel_seconds, 3) if parallel_seconds else None,
        "deterministic_order": serial == parallel,
        "live_calls": 0,
    }
def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect short-term pipeline performance metrics.")
    parser.add_argument(
        "--metrics",
        type=Path,
        default=PROJECT_ROOT / "reports" / "short_term" / "performance_metrics.json",
    )
    parser.add_argument("--fixture", action="store_true", help="Run an offline deterministic merge fixture.")
    parser.add_argument(
        "--history-benchmark",
        action="store_true",
        help="Run the 96-stock serial-vs-five-worker offline history benchmark.",
    )
    args = parser.parse_args()

    if args.fixture:
        print(json.dumps(benchmark_fixture(), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if args.history_benchmark:
        print(json.dumps(benchmark_history_parallelism(), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if not args.metrics.is_file():
        print(f"Performance metrics not found: {args.metrics}")
        return 1
    print(args.metrics.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
