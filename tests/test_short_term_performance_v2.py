"""Offline checks for the V2 short-term data-fetching adapters."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace
import time
import sys
import types

import pandas as pd

from scripts import profile_short_term_pipeline as profile
from scripts import run_short_term_candidate_pool as candidate_pool
from src.services.screening import daily, snapshot
from src.services.screening.run_context import ShortTermRunContext


def test_shared_snapshot_prefetch_uses_engine_pipeline_config(monkeypatch) -> None:
    fake_filter = types.ModuleType("src.services.screening.filter")
    fake_filter.requires_daily_features = lambda _filters: False
    fake_filter.without_daily_filters = lambda filters: filters
    fake_pipeline = types.ModuleType("src.services.screening.pipeline")
    fake_pipeline._required_snapshot_columns = lambda _filters: ["code"]
    fake_strategy = types.ModuleType("src.services.screening.strategy")
    fake_strategy.load_all_strategies = lambda _path: {
        name: SimpleNamespace(screening=SimpleNamespace(hard_filters=[]))
        for name in candidate_pool.STRATEGIES
    }
    monkeypatch.setitem(sys.modules, "src.services.screening.filter", fake_filter)
    monkeypatch.setitem(sys.modules, "src.services.screening.pipeline", fake_pipeline)
    monkeypatch.setitem(sys.modules, "src.services.screening.strategy", fake_strategy)
    pipeline_config = SimpleNamespace(
        strategies_dir=Path("strategies"),
        snapshot_source_priority=["em_datacenter"],
        fallback_snapshot_path=None,
        snapshot_fallback_max_age_hours=24,
        snapshot_cache_ttl_seconds=0,
    )
    screening = SimpleNamespace(hard_filters=[])
    monkeypatch.setattr(
        "src.services.screening.config.Config.from_env",
        classmethod(lambda cls: pipeline_config),
    )
    frame = pd.DataFrame([{"code": "600001", "price": 10}])
    frame.attrs["snapshot_source"] = "fixture"
    calls = {"count": 0}

    def fetch(*args, **kwargs):
        calls["count"] += 1
        assert kwargs["run_context"] is context
        return frame

    monkeypatch.setattr("src.services.screening.snapshot.fetch_snapshot_with_fallback", fetch)
    context = ShortTermRunContext(target_date="20260820")
    candidate_pool._prefetch_shared_snapshot(SimpleNamespace(), "cn", context)
    assert calls["count"] == 1
    assert context.snapshot is frame


def test_history_cache_allows_parallel_distinct_keys_and_deduplicates_same_key() -> None:
    context = ShortTermRunContext(target_date="20260820")
    calls = {"count": 0}

    def load() -> pd.DataFrame:
        calls["count"] += 1
        time.sleep(0.02)
        return pd.DataFrame([{"close": calls["count"]}])

    def one(code: str):
        return context.get_history(code, lookback_days=30, source="auto", loader=load)

    with ThreadPoolExecutor(max_workers=5) as executor:
        frames = list(executor.map(one, ["600001", "600002", "600003", "600004", "600005"]))
    assert len(frames) == 5
    assert calls["count"] == 5

    with ThreadPoolExecutor(max_workers=5) as executor:
        list(executor.map(lambda _item: one("600001"), range(5)))
    assert calls["count"] == 5


def test_realtime_cache_uses_one_underlying_call_for_concurrent_requests() -> None:
    context = ShortTermRunContext()
    calls = {"count": 0}

    def load() -> dict[str, int]:
        calls["count"] += 1
        time.sleep(0.02)
        return {"price": calls["count"]}

    with ThreadPoolExecutor(max_workers=5) as executor:
        values = list(executor.map(lambda _item: context.get_realtime_quote("SH600001", load), range(5)))
    assert {value["price"] for value in values} == {1}
    stats = context.metrics()["cache_stats"]
    assert calls["count"] == 1
    assert stats["realtime_http_calls"] == 1
    assert stats["quote_hits"] == 4


def test_short_term_snapshot_timeout_and_history_cache_date_validation(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_TIMEOUT", "10")
    assert snapshot._snapshot_call_timeout_seconds() == 10
    frame = pd.DataFrame([{"date": "2026-08-20", "close": 10}])
    path = daily._daily_history_cache_path(
        tmp_path, code="600001", source="auto", lookback_days=30, target_date="20260820"
    )
    daily._write_daily_history_cache(
        path, frame, code="600001", source="auto", lookback_days=30, target_date="20260820"
    )
    assert daily._read_daily_history_cache(
        path, ttl_seconds=3600, expected_target_date="20260820"
    ) is not None
    assert daily._read_daily_history_cache(
        path, ttl_seconds=3600, expected_target_date="20260821"
    ) is None


def test_akshare_subsource_circuit_opens_only_in_fast_mode(monkeypatch) -> None:
    from data_provider import akshare_fetcher

    monkeypatch.setenv("SHORT_TERM_FAST_RETRY", "true")
    akshare_fetcher.reset_short_term_subsource_health()
    for _ in range(3):
        akshare_fetcher._record_akshare_subsource(
            "akshare:eastmoney_hist", success=False, error="RemoteDisconnected"
        )
    assert akshare_fetcher._akshare_subsource_available("akshare:eastmoney_hist") is False
    assert akshare_fetcher._akshare_subsource_available("akshare:sina_hist") is True
    akshare_fetcher.reset_short_term_subsource_health()


def test_parallel_benchmark_is_offline_and_ordered() -> None:
    result = profile.benchmark_history_parallelism(stock_count=12, workers=5, sleep_seconds=0.01)
    assert result["live_calls"] == 0
    assert result["deterministic_order"] is True
    assert result["parallel_seconds"] < result["serial_seconds"]


def test_short_term_retry_policy_is_bounded() -> None:
    assert daily._fast_failure_attempt_limit("RemoteDisconnected") == 2
    assert daily._fast_failure_attempt_limit("HTTP 403") == 2
    assert daily._fast_failure_attempt_limit("HTTP 429") == 2
