"""Offline, deterministic tests for Stage 5 auction confirmation."""

from __future__ import annotations

import importlib
import json
import sys
import types
from datetime import date, datetime, timedelta


def _module():
    try:
        import akshare  # noqa: F401
    except ModuleNotFoundError:
        sys.modules["akshare"] = types.ModuleType("akshare")
    try:
        import pandas  # noqa: F401
    except ModuleNotFoundError:
        pandas = types.ModuleType("pandas")
        pandas.Timestamp = type("Timestamp", (), {})
        sys.modules["pandas"] = pandas
    try:
        import exchange_calendars  # noqa: F401
    except ModuleNotFoundError:
        sys.modules["exchange_calendars"] = types.ModuleType("exchange_calendars")
    return importlib.import_module("scripts.run_short_term_auction_confirmation")


def _fake_xshg(module):
    class Calendar:
        def sessions_in_range(self, start, end):
            import pandas as pd
            current = start.date()
            final = end.date()
            days = []
            while current <= final:
                if current.weekday() < 5:
                    days.append(pd.Timestamp(current))
                current += timedelta(days=1)
            return pd.DatetimeIndex(days)

    module.xcals = types.SimpleNamespace(get_calendar=lambda name: Calendar())


def _record(code="000001", **overrides):
    record = {
        "code": code,
        "name": "测试股",
        "primary_theme": "通信设备",
        "primary_theme_role": "MAIN",
        "primary_theme_rank": 1,
        "stock_role": "THEME_LEADER",
        "leader_score": 80,
        "resonance_count": 3,
        "setup_type": "FIRST_PULLBACK",
        "setup_grade": "A",
        "weak_to_strong_score": 80,
        "prev_close": 10.0,
        "prev_volume": 1000,
        "stage4_watchlist_member": True,
    }
    record.update(overrides)
    return record


def _snapshot(module, price=10.2, matched=1500, timestamp="2026-08-18T09:24:50+08:00", **extra):
    row = {
        "code": "000001",
        "name": "测试股",
        "prev_close": 10.0,
        "auction_reference_price": price,
        "auction_matched_volume": matched,
        "auction_unmatched_volume": 100,
        "auction_unmatched_side": "买",
    }
    row.update(extra)
    return {"timestamp": timestamp, "rows": [row]}


def _proxy_snapshot(module, price=10.1, volume=1200, timestamp="2026-08-18T09:24:50+08:00", **extra):
    row = {"code": "000001", "prev_close": 10.0, "最新价": price, "成交量": volume, "买一价": price - 0.01, "买一量": 500, "卖一价": price + 0.01, "卖一量": 400}
    row.update(extra)
    return {"timestamp": timestamp, "rows": [row]}


def test_window_statuses_are_explicit():
    module = _module()
    assert module._auction_status(datetime.fromisoformat("2026-08-18T09:14:59+08:00")) == "BEFORE_AUCTION"
    assert module._auction_status(datetime.fromisoformat("2026-08-18T09:20:00+08:00")) == "AUCTION_WINDOW"
    assert module._auction_status(datetime.fromisoformat("2026-08-18T09:27:00+08:00")) == "FINAL_SNAPSHOT_ONLY"
    assert module._auction_status(datetime.fromisoformat("2026-08-18T09:31:00+08:00")) == "OUTSIDE_WINDOW"
    assert module._auction_status(datetime.fromisoformat("2026-08-18T15:00:00+08:00"), snapshot_file=True) == "SNAPSHOT_TEST"


def test_gap_score_uses_healthy_middle_range():
    module = _module()
    assert module._gap_score(-2) == 0
    assert module._gap_score(-0.5) == 4
    assert module._gap_score(0.5) == 8
    assert module._gap_score(2.1) == 15
    assert module._gap_score(4) == 12
    assert module._gap_score(6) == 7
    assert module._gap_score(8) == 3


def test_real_auction_small_high_open_with_late_buying_is_strong():
    module = _module()
    snapshots = [
        _snapshot(module, price=10.1, matched=1000, timestamp="2026-08-18T09:20:05+08:00"),
        _snapshot(module, price=10.25, matched=1800, timestamp="2026-08-18T09:24:50+08:00"),
    ]
    state = module._build_state(_record(), snapshots)
    assert state["auction_data_mode"] == "REAL_AUCTION"
    assert state["gap_pct"] == 2.5
    assert state["late_auction_strength"] > 12
    assert state["auction_qualified"] is True
    assert state["auction_grade"] in {"A", "B"}


def test_flat_open_then_progressive_strength_can_score_high():
    module = _module()
    snapshots = [
        _snapshot(module, price=10.0, matched=900, timestamp="2026-08-18T09:20:05+08:00"),
        _snapshot(module, price=10.08, matched=1700, timestamp="2026-08-18T09:24:50+08:00"),
    ]
    state = module._build_state(_record(), snapshots)
    assert state["gap_pct"] == 0.8
    assert state["auction_qualified"] is True
    assert state["final_auction_score"] >= 70


def test_late_auction_weakness_rejects_early_strength():
    module = _module()
    snapshots = [
        _snapshot(module, price=10.8, matched=2000, timestamp="2026-08-18T09:20:05+08:00", auction_unmatched_side="买"),
        _snapshot(module, price=10.7, matched=700, timestamp="2026-08-18T09:24:50+08:00", auction_unmatched_side="卖"),
    ]
    state = module._build_state(_record(), snapshots)
    assert state["late_auction_strength"] < 5
    assert "LATE_AUCTION_COLLAPSE" in state["hard_reject_reasons"]
    assert state["auction_qualified"] is False


def test_high_open_with_buying_decay_is_not_accepted():
    module = _module()
    snapshots = [
        _snapshot(module, price=10.8, matched=2000, timestamp="2026-08-18T09:20:05+08:00"),
        _snapshot(module, price=10.65, matched=600, timestamp="2026-08-18T09:24:50+08:00", auction_unmatched_side="卖"),
    ]
    state = module._build_state(_record(), snapshots)
    assert state["gap_pct"] == 6.5
    assert state["auction_qualified"] is False
    assert state["auction_grade"] == "D"


def test_real_matched_volume_is_distinct_from_proxy_volume():
    module = _module()
    state = module._build_state(_record(), [_snapshot(module)])
    assert state["auction_matched_volume"] == 1500
    assert state["proxy_volume"] is None
    assert state["score_components"]["auction_volume_strength"] == 20


def test_quote_proxy_never_gets_real_auction_fields_and_is_capped_at_b():
    module = _module()
    snapshots = [_proxy_snapshot(module, price=10.1, volume=1000), _proxy_snapshot(module, price=10.2, volume=1800, timestamp="2026-08-18T09:24:50+08:00")]
    state = module._build_state(_record(), snapshots)
    assert state["auction_data_mode"] == "QUOTE_PROXY"
    assert state["auction_reference_price"] is None
    assert state["auction_matched_volume"] is None
    assert state["proxy_gap_pct"] == 2
    assert state["auction_grade"] in {"B", "C", "D"}
    assert state["auction_grade"] != "A"


def test_missing_real_auction_fields_stay_none():
    module = _module()
    state = module._build_state(_record(), [{"timestamp": "2026-08-18T09:24:50+08:00", "rows": [{"code": "000001", "prev_close": 10, "auction_reference_price": 10.2}]}])
    assert state["auction_data_mode"] == "PARTIAL"
    assert state["auction_matched_volume"] is None
    assert state["score_components"]["auction_volume_strength"] is None


def test_coverage_and_confidence_formula():
    module = _module()
    scored = module._weighted_score({"gap_quality": 15, "auction_volume_strength": None, "late_auction_strength": None, "theme_resonance": None, "previous_setup": None, "leader_status": None, "risk_quality": None})
    assert scored["coverage_ratio"] == 0.15
    assert scored["normalized_score"] == 100
    assert scored["confidence_adjusted_score"] < 40


def test_hard_reject_overrides_high_score():
    module = _module()
    state = module._build_state(_record(is_limit_down=True), [_snapshot(module, price=10.2, matched=2000), _snapshot(module, price=10.25, matched=2500, timestamp="2026-08-18T09:24:50+08:00")])
    assert state["final_auction_score"] is not None
    assert "LIMIT_DOWN_AUCTION" in state["hard_reject_reasons"]
    assert state["auction_qualified"] is False
    assert state["auction_grade"] == "D"


def test_input_pool_uses_stage3_leader_when_stage4_watchlist_is_empty():
    module = _module()
    stage4 = {"next_day_watchlist": [], "weak_to_strong_states": []}
    stage4_pool = {"candidates": []}
    stage3 = {"market_leaders": [{"code": "000002", "name": "核心", "stock_role": "MARKET_LEADER", "leader_score": 88}]}
    records, meta = module._input_pool(stage4, stage4_pool, stage3)
    assert [item["code"] for item in records] == ["000002"]
    assert records[0]["stage4_watchlist_member"] is False
    assert meta["stage4_watchlist_count"] == 0


def test_input_pool_is_capped_at_fifteen():
    module = _module()
    stage3 = {"market_leaders": [{"code": str(i).zfill(6), "stock_role": "MARKET_LEADER", "leader_score": i} for i in range(20)]}
    records, _ = module._input_pool({"next_day_watchlist": [], "weak_to_strong_states": []}, {"candidates": []}, stage3)
    assert len(records) == 15


def test_watchlist_is_capped_at_five_and_excludes_unqualified():
    module = _module()
    states = []
    for i in range(6):
        state = _record(str(i).zfill(6))
        state.update({"auction_qualified": True, "auction_grade": "B", "final_auction_score": 75 - i})
        states.append(state)
    rejected = _record("000099", auction_qualified=False, auction_grade="D", final_auction_score=99)
    result = module._build_watchlist(states + [rejected])
    assert len(result) == 5
    assert all(item["code"] != "000099" for item in result)


def test_no_qualified_stock_is_allowed():
    module = _module()
    assert module._build_watchlist([_record(auction_qualified=False, auction_grade="D", final_auction_score=90)]) == []


def test_stage5_enrichment_keeps_stage4_candidate_order():
    module = _module()
    stage4_pool = {"candidates": [{"code": "000002", "name": "B"}, {"code": "000001", "name": "A"}]}
    states = {"000001": {"auction_qualified": True, "auction_grade": "B", "final_auction_score": 70, "auction_data_mode": "REAL_AUCTION"}}
    result = module._enrich_stage5(stage4_pool, states)
    assert [item["code"] for item in result["candidates"]] == ["000002", "000001"]
    assert result["candidates"][0]["auction_confirmation"]["auction_qualified"] is False
    assert result["candidates"][1]["auction_confirmation"]["auction_grade"] == "B"


def test_snapshot_file_supports_offline_history(tmp_path):
    module = _module()
    path = tmp_path / "auction_snapshot.json"
    path.write_text(json.dumps({"snapshots": [_snapshot(module), _snapshot(module, price=10.3, matched=2000, timestamp="2026-08-18T09:24:50+08:00")]}, ensure_ascii=False), encoding="utf-8")
    snapshots = module._load_snapshot_file(path)
    assert len(snapshots) == 2
    assert snapshots[-1]["rows"][0]["code"] == "000001"


def test_source_mode_distinguishes_real_proxy_and_unavailable():
    module = _module()
    real = module._build_state(_record(), [_snapshot(module)])
    proxy = module._build_state(_record("000002"), [])
    assert module._source_mode([real]) == "REAL_AUCTION"
    assert module._source_mode([module._build_state(_record(), [_proxy_snapshot(module)])]) == "QUOTE_PROXY"
    assert module._source_mode([proxy]) == "UNAVAILABLE"


def test_live_target_date_must_match_current_shanghai_date():
    module = _module()
    now = datetime.fromisoformat("2026-08-18T09:20:00+08:00")
    assert module._live_date_guard(date(2026, 8, 17), now) == "LIVE_DATE_MISMATCH"


def test_live_weekend_is_non_trading_day_without_a_request():
    module = _module()
    _fake_xshg(module)
    now = datetime.fromisoformat("2026-08-22T09:20:00+08:00")
    assert module._live_date_guard(date(2026, 8, 22), now) == "NON_TRADING_DAY"


def test_previous_trading_day_for_monday_is_friday():
    module = _module()
    _fake_xshg(module)
    assert module._previous_trading_day(date(2026, 8, 24)) == date(2026, 8, 21)


def test_stale_stage4_input_is_detected():
    module = _module()
    valid, source = module._validate_stage4_date(
        {"target_date": "20260820"}, {"target_date": "20260820"}, date(2026, 8, 21)
    )
    assert valid is False
    assert source == date(2026, 8, 20)


def test_snapshot_mode_requires_a_snapshot_file():
    module = _module()
    assert module._snapshot_mode_guard("snapshot", False) == "SNAPSHOT_FILE_REQUIRED"
    assert module._snapshot_mode_guard("snapshot", True) is None


def test_auction_schedule_at_0921_waits_for_remaining_targets():
    module = _module()
    missed, pending = module._snapshot_schedule(datetime.fromisoformat("2026-08-18T09:21:00+08:00"))
    assert missed == ["2026-08-18T09:20:05+08:00"]
    assert [item.strftime("%H:%M:%S") for item in pending] == ["09:23:00", "09:24:50"]


def test_auction_schedule_at_0924_waits_for_final_target():
    module = _module()
    missed, pending = module._snapshot_schedule(datetime.fromisoformat("2026-08-18T09:24:00+08:00"))
    assert [item.strftime("%H:%M:%S") for item in pending] == ["09:24:50"]
    assert len(missed) == 2


def test_final_snapshot_only_is_partial_and_grade_is_capped_at_c():
    module = _module()
    snapshots = [_snapshot(module, price=10.2, matched=2000)]
    state = module._build_state(_record(), snapshots, final_snapshot_only=True)
    assert state["final_snapshot_only"] is True
    assert state["late_auction_strength"] is None
    assert module._data_quality("FINAL_SNAPSHOT_ONLY", [state], [], final_snapshot_only=True, snapshots=snapshots, snapshot_file=False) == "partial"
    assert module.GRADE_ORDER[state["auction_grade"]] >= module.GRADE_ORDER["C"]


def test_outside_window_has_no_watchlist():
    module = _module()
    state = module._build_state(_record(), [])
    assert module._build_watchlist([state]) == []


def test_stage5_role_priority_upgrades_stage4_theme_leader_from_stage3_market_leader():
    module = _module()
    records, _ = module._input_pool(
        {"next_day_watchlist": [{"code": "603330", "stock_role": "THEME_LEADER", "leader_score": 83, "market_leader_rank": 3}]},
        {"candidates": []},
        {"market_leaders": [{"code": "603330", "stock_role": "MARKET_LEADER", "leader_score": 92, "market_leader_rank": 1}], "leaders": []},
    )
    result = records[0]
    assert result["stock_role"] == "MARKET_LEADER"
    assert result["leader_score"] == 92.0
    assert result["market_leader_rank"] == 1
    assert {item["source"] for item in result["stock_role_sources"]} >= {"stage4_watchlist", "stage3_market_leaders"}


def test_stage5_merge_metrics_and_role_are_monotonic():
    module = _module()
    records = {}
    module._merge_record(records, {"code": "000001", "stock_role": "MARKET_LEADER", "leader_score": 92, "market_leader_rank": 1}, source="stage3_market_leaders")
    module._merge_record(records, {"code": "000001", "stock_role": "THEME_LEADER", "leader_score": 80, "market_leader_rank": 3}, source="stage4_state")
    result = records["000001"]
    assert result["stock_role"] == "MARKET_LEADER"
    assert result["leader_score"] == 92.0
    assert result["market_leader_rank"] == 1


def test_stage5_front_core_cannot_be_overwritten_by_follower():
    module = _module()
    records = {}
    module._merge_record(records, {"code": "000002", "stock_role": "FRONT_CORE"}, source="stage3_leaders")
    module._merge_record(records, {"code": "000002", "stock_role": "FOLLOWER"}, source="stage4_state")
    assert records["000002"]["stock_role"] == "FRONT_CORE"


def test_stage5_603330_keeps_market_leader_score_weight_source():
    module = _module()
    records, _ = module._input_pool(
        {
            "next_day_watchlist": [{"code": "603330", "name": "天洋新材", "stock_role": "THEME_LEADER", "leader_score": 83}],
            "weak_to_strong_states": [],
        },
        {"candidates": []},
        {
            "leaders": [{"code": "603330", "stock_role": "THEME_LEADER", "leader_score": 83}],
            "market_leaders": [{"code": "603330", "stock_role": "MARKET_LEADER", "leader_score": 92, "market_leader_rank": 1}],
        },
    )
    result = records[0]
    assert result["code"] == "603330"
    assert result["stock_role"] == "MARKET_LEADER"
    assert result["leader_score"] == 92.0
