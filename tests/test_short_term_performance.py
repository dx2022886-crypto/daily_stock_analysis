"""Offline contracts for the short-term pipeline performance adapters."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from scripts import profile_short_term_pipeline as profile
from scripts import run_short_term_candidate_pool as candidate_pool
from src.services.screening.daily import _fast_failure_attempt_limit
from src.services.screening.run_context import ShortTermRunContext


def _fixture_results() -> dict[str, dict[str, object]]:
    return {
        strategy: {
            "candidates": [
                {"rank": 1, "code": "600001", "name": "A", "score": 90},
                {"rank": 2, "code": "600002", "name": "B", "score": 80},
            ]
        }
        for strategy in candidate_pool.STRATEGIES
    }


def test_four_strategies_share_one_snapshot() -> None:
    context = ShortTermRunContext()
    calls = {"count": 0}
    frame = pd.DataFrame([{"code": "600001", "price": 10.0}])

    def load() -> pd.DataFrame:
        calls["count"] += 1
        return frame

    assert context.load_snapshot(load) is frame
    assert context.load_snapshot(load) is frame
    assert calls["count"] == 1
    assert context.metrics()["cache_stats"]["snapshot_reused"] == 1


def test_same_stock_history_is_fetched_once_and_target_date_is_in_key() -> None:
    context = ShortTermRunContext(target_date="20260820")
    calls = {"count": 0}
    frame = pd.DataFrame([{"date": "2026-08-20", "close": 10.0}])

    def load() -> pd.DataFrame:
        calls["count"] += 1
        return frame

    first = context.get_history("600001", lookback_days=120, source="auto", loader=load)
    second = context.get_history("600001", lookback_days=120, source="auto", loader=load)
    assert first is second
    assert calls["count"] == 1
    assert context.history_cache_key(
        market="cn", stock_code="600001", start_date="20260801", end_date="20260820"
    ) != context.history_cache_key(
        market="cn", stock_code="600001", start_date="20260801", end_date="20260821"
    )


def test_realtime_quote_cache_is_run_scoped_and_not_auction_cache() -> None:
    context = ShortTermRunContext()
    calls = {"count": 0}

    def load() -> dict[str, object]:
        calls["count"] += 1
        return {"price": calls["count"], "timestamp": calls["count"]}

    assert context.get_realtime_quote("600001", load)["price"] == 1
    assert context.get_realtime_quote("600001", load)["price"] == 1
    assert calls["count"] == 1
    # Stage5 does not receive this context and therefore has no path to reuse it.
    stage5_calls = {"count": 0}

    def stage5_live_fetch() -> dict[str, object]:
        stage5_calls["count"] += 1
        return {"price": stage5_calls["count"]}

    assert stage5_live_fetch()["price"] == 1
    assert stage5_live_fetch()["price"] == 2
    assert stage5_calls["count"] == 2


def test_run_level_source_circuit_breaker_opens_after_threshold() -> None:
    context = ShortTermRunContext()
    assert context.record_source_failure("efinance", "RemoteDisconnected") is False
    assert context.record_source_failure("efinance", "RemoteDisconnected") is False
    assert context.record_source_failure("efinance", "RemoteDisconnected") is True
    assert "skip_count=1" in (context.source_disabled_reason("efinance") or "")


def test_fast_failure_retry_limit_does_not_allow_unbounded_retries() -> None:
    assert _fast_failure_attempt_limit("RemoteDisconnected()") == 2
    assert _fast_failure_attempt_limit("HTTP 403") == 2
    assert _fast_failure_attempt_limit("HTTP 418") == 2
    assert _fast_failure_attempt_limit("HTTP 429") == 2
    assert _fast_failure_attempt_limit("HTTP 503") == 2


def test_deterministic_top30_is_equal_between_fixture_baseline_and_optimized() -> None:
    optimized, _ = candidate_pool._merge_results(_fixture_results())
    baseline_codes = ["600001", "600002"]
    assert [item["code"] for item in optimized[:30]] == baseline_codes


def test_profile_fixture_is_offline_and_reports_consistency() -> None:
    result = profile.benchmark_fixture()
    assert result["top30_consistent"] is True
    assert result["baseline_codes"] == result["optimized_codes"]


def test_performance_metrics_writer_is_best_effort(tmp_path: Path, monkeypatch) -> None:
    metrics_path = tmp_path / "performance_metrics.json"
    monkeypatch.setattr(candidate_pool, "PERFORMANCE_PATH", metrics_path)
    candidate_pool._write_performance({"stage": "stage1", "total_seconds": 0.1})
    assert json.loads(metrics_path.read_text(encoding="utf-8"))["stage"] == "stage1"


def test_performance_metrics_failure_does_not_raise(monkeypatch) -> None:
    monkeypatch.setattr(candidate_pool, "PERFORMANCE_PATH", Path("/nonexistent/metrics.json"))
    candidate_pool._write_performance({"stage": "stage1"})
