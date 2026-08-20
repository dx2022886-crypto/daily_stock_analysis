"""Offline checks for the V2 short-term data-fetching adapters."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace
import time
import sys
import types

import pandas as pd
import pytest

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


def test_history_provider_path_has_no_os_name_error(monkeypatch) -> None:
    from data_provider.base import DataFetcherManager

    class FixtureFetcher:
        name = "FixtureFetcher"
        priority = 1

        def get_daily_data(self, stock_code: str, **_kwargs):
            return pd.DataFrame(
                [{
                    "date": "2026-08-20",
                    "open": 10.0,
                    "high": 11.0,
                    "low": 9.0,
                    "close": 10.5,
                    "volume": 100,
                }]
            )

    monkeypatch.setenv("SHORT_TERM_FAST_RETRY", "true")
    DataFetcherManager.reset_daily_source_health()
    manager = DataFetcherManager(fetchers=[FixtureFetcher()])
    frame, provider = manager.get_daily_data("600001", days=30)
    assert provider == "FixtureFetcher"
    assert list(frame.columns)[:6] == ["date", "open", "high", "low", "close", "volume"]


def test_fixed_history_path_preserves_baseline_ohlcv_fixture(monkeypatch) -> None:
    from data_provider.base import DataFetcherManager

    baseline = pd.DataFrame(
        [
            {"date": "2026-08-19", "open": 10.0, "high": 10.8, "low": 9.8, "close": 10.5, "volume": 100},
            {"date": "2026-08-20", "open": 10.5, "high": 11.2, "low": 10.3, "close": 11.0, "volume": 120},
        ]
    )

    class BaselineFetcher:
        name = "FixtureFetcher"
        priority = 1

        def get_daily_data(self, stock_code: str, **_kwargs):
            return baseline.copy()

    monkeypatch.setenv("SHORT_TERM_FAST_RETRY", "true")
    DataFetcherManager.reset_daily_source_health()
    manager = DataFetcherManager(fetchers=[BaselineFetcher()])
    fixed, _provider = manager.get_daily_data("600001", days=30)
    columns = ["date", "open", "high", "low", "close", "volume"]
    pd.testing.assert_frame_equal(
        fixed[columns].reset_index(drop=True),
        baseline[columns].reset_index(drop=True),
        check_dtype=False,
    )


@pytest.mark.skipif(sys.version_info < (3, 10), reason="screening service requires Python 3.10+")
def test_screening_and_post_rank_quote_paths_share_one_run_cache(monkeypatch) -> None:
    from src.config import Config
    from src.services import screening_service
    from src.services.screening.dsa_provider import apply_dsa_provider_context
    from src.services.screening.models import Pick

    context = ShortTermRunContext(target_date="20260820")
    quote_calls = {"count": 0}

    def quote(_code: str) -> dict[str, object]:
        quote_calls["count"] += 1
        return {"price": 10.5, "change_pct": 1.2, "amount": 1000000}

    monkeypatch.setattr(screening_service, "get_dsa_realtime_quote", quote)
    monkeypatch.setattr(
        screening_service,
        "get_dsa_fundamental_context",
        lambda _code: {"coverage": {}},
    )
    monkeypatch.setattr(
        screening_service,
        "_get_dsa_fetcher_manager",
        lambda: SimpleNamespace(get_stock_name=lambda _code, allow_realtime=False: "Fixture"),
    )
    monkeypatch.setattr(
        screening_service,
        "search_dsa_stock_news",
        lambda *_args, **_kwargs: {"success": False, "results": []},
    )
    monkeypatch.setattr(
        screening_service,
        "search_dsa_stock_events",
        lambda *_args, **_kwargs: {"success": False, "results": []},
    )

    provider_context = screening_service._build_screening_context(
        Config(screening_enabled=True),
        max_results=5,
        run_context=context,
    )
    pick = Pick(rank=1, code="SH600001", name="Fixture", final_score=90.0, screen_score=90.0)
    apply_dsa_provider_context([pick], provider_context)

    # This is the optional post-rank path in ScreeningService.  It must use
    # the same adapter as the pipeline's pre-rank screening path.
    enriched, _ = screening_service._enrich_candidates_with_dsa(
        [{"code": "600001", "name": "Fixture"}],
        realtime_quote_getter=provider_context["dsa"]["get_realtime_quote"],
    )
    assert quote_calls["count"] == 1
    assert context.metrics()["cache_stats"]["quote_hits"] >= 1
    assert enriched[0]["price"] == 10.5


def _snapshot_fixture(*, rows: int = 120, target_date: str = "20260820") -> pd.DataFrame:
    frame = pd.DataFrame(
        {
            "code": [f"{index:06d}" for index in range(rows)],
            "name": [f"Fixture {index}" for index in range(rows)],
            "price": [10.0] * rows,
            "volume_ratio": [1.0] * rows,
        }
    )
    frame.attrs["snapshot_source"] = "em_datacenter"
    frame.attrs["snapshot_target_date"] = target_date
    frame.attrs["snapshot_data_as_of"] = target_date
    frame.attrs["snapshot_fetched_at"] = "2026-08-20T07:00:00.000+00:00"
    return frame


def test_failed_shared_snapshot_is_memoized_for_all_strategy_calls(monkeypatch) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_PREFER_LAST_GOOD", "false")
    monkeypatch.setattr(snapshot, "_SOURCE_HEALTH", {})
    context = ShortTermRunContext(target_date="20260820")
    calls: list[str] = []

    def fail(source: str) -> pd.DataFrame:
        calls.append(source)
        raise TimeoutError(f"{source} timeout")

    monkeypatch.setattr(snapshot, "fetch_cn_snapshot", fail)
    loader = lambda: snapshot.fetch_snapshot_with_fallback(
        ["em_datacenter", "sina", "efinance", "akshare_em"],
        required_columns=["code", "volume_ratio"],
        run_context=context,
    )
    with pytest.raises(RuntimeError):
        context.load_snapshot(loader)
    for _ in range(4):
        with pytest.raises(RuntimeError):
            context.load_snapshot(loader)

    assert calls == ["em_datacenter", "sina", "efinance", "akshare_em"]
    assert context.snapshot_fetch_failed is True
    assert context.metrics()["snapshot_source_attempts"] == 4


def test_em_datacenter_timeout_is_longer_than_other_snapshot_sources(monkeypatch) -> None:
    monkeypatch.setenv("SHORT_TERM_FAST_RETRY", "true")
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_TIMEOUT", "10")
    assert snapshot._snapshot_call_timeout_seconds("em_datacenter") == 30.0
    assert snapshot._snapshot_call_timeout_seconds("em_datacenter") > snapshot._snapshot_call_timeout_seconds("sina")
    assert snapshot._snapshot_call_timeout_seconds("sina") == 10.0
    assert snapshot._snapshot_call_timeout_seconds("efinance") == 6.0
    assert snapshot._snapshot_call_timeout_seconds("akshare_em") == 12.0


def test_validated_last_good_same_target_date_skips_live_sources(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_PREFER_LAST_GOOD", "true")
    cache_path = tmp_path / "snapshot.last_good.json"
    cached = _snapshot_fixture()
    snapshot._write_last_good_snapshot(
        cache_path,
        cached,
        source_priority=["em_datacenter", "sina"],
        market="cn",
        target_date="20260820",
    )
    calls: list[str] = []
    monkeypatch.setattr(snapshot, "fetch_cn_snapshot", lambda source: calls.append(source))
    context = ShortTermRunContext(target_date="20260820")
    result = snapshot.fetch_snapshot_with_fallback(
        ["em_datacenter", "sina"],
        required_columns=["code", "volume_ratio"],
        fallback_snapshot_path=cache_path,
        market="cn",
        run_context=context,
    )
    assert calls == []
    assert len(result) == 120
    assert result.attrs["snapshot_is_cached"] is True
    assert result.attrs["snapshot_target_date"] == "20260820"
    assert result.attrs["snapshot_data_as_of"] == "20260820"


def test_cross_trading_day_last_good_is_not_reused(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_PREFER_LAST_GOOD", "true")
    monkeypatch.setattr(snapshot, "_SOURCE_HEALTH", {})
    cache_path = tmp_path / "snapshot.last_good.json"
    snapshot._write_last_good_snapshot(
        cache_path,
        _snapshot_fixture(target_date="20260819"),
        source_priority=["sina"],
        market="cn",
        target_date="20260819",
    )
    calls: list[str] = []

    def fail(source: str) -> pd.DataFrame:
        calls.append(source)
        raise RuntimeError("live unavailable")

    monkeypatch.setattr(snapshot, "fetch_cn_snapshot", fail)
    with pytest.raises(RuntimeError, match="All snapshot sources failed"):
        snapshot.fetch_snapshot_with_fallback(
            ["sina"],
            required_columns=["code", "volume_ratio"],
            fallback_snapshot_path=cache_path,
            market="cn",
            run_context=ShortTermRunContext(target_date="20260820"),
        )
    assert calls == ["sina"]


def test_live_failure_falls_back_to_validated_last_good(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_PREFER_LAST_GOOD", "false")
    monkeypatch.setattr(snapshot, "_SOURCE_HEALTH", {})
    cache_path = tmp_path / "snapshot.last_good.json"
    snapshot._write_last_good_snapshot(
        cache_path,
        _snapshot_fixture(),
        source_priority=["sina"],
        market="cn",
        target_date="20260820",
    )
    monkeypatch.setattr(
        snapshot,
        "fetch_cn_snapshot",
        lambda _source: (_ for _ in ()).throw(RuntimeError("live unavailable")),
    )
    result = snapshot.fetch_snapshot_with_fallback(
        ["sina"],
        required_columns=["code", "volume_ratio"],
        fallback_snapshot_path=cache_path,
        market="cn",
        run_context=ShortTermRunContext(target_date="20260820"),
    )
    assert len(result) == 120
    assert result.attrs["snapshot_is_cached"] is True
    assert result.attrs["fallback_used"] is True


def test_invalid_last_good_after_live_failure_fails(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SHORT_TERM_SNAPSHOT_PREFER_LAST_GOOD", "false")
    monkeypatch.setattr(snapshot, "_SOURCE_HEALTH", {})
    cache_path = tmp_path / "snapshot.last_good.json"
    snapshot._write_last_good_snapshot(
        cache_path,
        _snapshot_fixture(),
        source_priority=["sina"],
        market="cn",
        target_date="20260819",
    )
    monkeypatch.setattr(
        snapshot,
        "fetch_cn_snapshot",
        lambda _source: (_ for _ in ()).throw(RuntimeError("live unavailable")),
    )
    with pytest.raises(RuntimeError, match="All snapshot sources failed"):
        snapshot.fetch_snapshot_with_fallback(
            ["sina"],
            required_columns=["code", "volume_ratio"],
            fallback_snapshot_path=cache_path,
            market="cn",
            run_context=ShortTermRunContext(target_date="20260820"),
        )
