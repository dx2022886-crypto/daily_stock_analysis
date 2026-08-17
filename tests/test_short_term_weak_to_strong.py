"""Pure-rule tests for stage-4 weak-to-strong observation logic."""

from __future__ import annotations

import importlib
import sys
import types
from datetime import date


def _module():
    try:
        import akshare  # noqa: F401
    except ModuleNotFoundError:
        sys.modules["akshare"] = types.ModuleType("akshare")
    try:
        import exchange_calendars  # noqa: F401
    except ModuleNotFoundError:
        sys.modules["exchange_calendars"] = types.ModuleType("exchange_calendars")
    try:
        import pandas  # noqa: F401
    except ModuleNotFoundError:
        pandas = types.ModuleType("pandas")
        pandas.Timestamp = type("Timestamp", (), {})
        sys.modules["pandas"] = pandas
    return importlib.import_module("scripts.run_short_term_weak_to_strong")


def _record(**overrides):
    base = {
        "code": "000001",
        "name": "核心股",
        "primary_theme": "机器人",
        "primary_theme_rank": 1,
        "primary_theme_score": 82,
        "primary_theme_role": "MAIN",
        "stock_role": "THEME_LEADER",
        "leader_score": 80,
        "market_leader_rank": None,
        "resonance_count": 3,
        "is_limit_up": False,
        "is_broken_board": True,
        "is_limit_down": False,
        "board_count": 3,
        "break_count": 1,
        "current_change_pct": -1.0,
        "open_pct": 3.0,
        "high_pct": 8.0,
        "low_pct": -2.0,
        "close_pct": -1.0,
        "turnover_rate": 8.0,
        "amount": 300000000,
        "volume_ratio_5d": 1.2,
        "close_position": 0.6,
        "pct_change_1d": -1.0,
        "pct_change_2d": 2.0,
        "pct_change_3d": 5.0,
        "pct_change_5d": 12.0,
        "ma5": 10.0,
        "ma10": 9.8,
        "bias_ma5": 1.0,
        "bias_ma10": 2.0,
        "max_drawdown_3d": -5.0,
        "consecutive_up_days": 2,
        "recent_limit_up_count": 1,
        "recent_broken_board_count": 1,
        "hot_rank": 5,
    }
    base.update(overrides)
    return base


def test_leader_broken_board_scores_above_follower_broken_board():
    module = _module()
    leader = module._build_state(_record(stock_role="THEME_LEADER"), {}, 1, 1, "分歧")
    follower = module._build_state(_record(stock_role="FOLLOWER", primary_theme_role="ROTATION"), {}, 1, 1, "分歧")
    assert leader["final_weak_to_strong_score"] > follower["final_weak_to_strong_score"]


def test_limit_down_cannot_receive_grade_a():
    module = _module()
    state = module._build_state(_record(is_limit_down=True, current_change_pct=-10.0), {}, 1, 1, "分歧")
    assert state["setup_grade"] == "D"
    assert state["risk_penalties"]["LIMIT_DOWN"] == 30.0


def test_risky_a_grade_is_capped_at_c():
    module = _module()
    assert module._grade(80.0, {"BROKEN_TREND": 15.0}, {}) == "C"


def test_risky_b_grade_is_capped_at_c():
    module = _module()
    assert module._grade(70.0, {"FOLLOWER_ONLY": 12.0}, {}) == "C"


def test_d_grade_is_not_upgraded_by_c_cap():
    module = _module()
    assert module._grade(40.0, {"WEAK_THEME": 10.0}, {}) == "D"


def test_stage3_market_leader_upgrades_theme_leader_without_order_dependence():
    module = _module()
    records, _ = module._stage3_stock_maps(
        {"candidates": [{"code": "603330", "name": "天洋新材", "theme_analysis": {"stock_role": "THEME_LEADER", "leader_score": 80, "market_leader_rank": 3}}]},
        {
            "leaders": [{"code": "603330", "stock_role": "THEME_LEADER", "leader_score": 83, "market_leader_rank": 3}],
            "market_leaders": [{"code": "603330", "stock_role": "MARKET_LEADER", "leader_score": 92, "market_leader_rank": 1}],
        },
    )
    result = records["603330"]
    assert result["stock_role"] == "MARKET_LEADER"
    assert result["leader_score"] == 92.0
    assert result["market_leader_rank"] == 1
    assert {item["source"] for item in result["stock_role_sources"]} == {"stage3_candidate", "stage3_leaders", "stage3_market_leaders"}


def test_role_priority_never_downgrades_and_metrics_keep_best_values():
    module = _module()
    assert module._stronger_stock_role("MARKET_LEADER", "THEME_LEADER") == "MARKET_LEADER"
    assert module._stronger_stock_role("FRONT_CORE", "FOLLOWER") == "FRONT_CORE"
    record = {"leader_score": 80, "market_leader_rank": 3}
    module._merge_leader_metrics(record, 92, 1)
    assert record["leader_score"] == 92.0
    assert record["market_leader_rank"] == 1


def test_stage4_enrichment_exposes_strongest_role_for_603330():
    module = _module()
    stage3 = {
        "candidates": [{"code": "603330", "name": "天洋新材", "theme_analysis": {"stock_role": "THEME_LEADER", "leader_score": 83}}],
    }
    state = {
        "code": "603330",
        "stock_role": "MARKET_LEADER",
        "stock_role_source": "stage3_market_leaders",
        "stock_role_sources": [{"source": "stage3_market_leaders", "role": "MARKET_LEADER"}],
        "leader_score": 92.0,
        "market_leader_rank": 1,
        "weak_to_strong_score": 70,
        "risk_penalty_total": 0,
        "final_weak_to_strong_score": 70,
        "setup_grade": "B",
        "setup_type": "LEADER_DIVERGENCE",
        "weak_signals": [],
        "strength_foundation": [],
        "sentiment_adjustment": 0,
        "tomorrow_plan": None,
    }
    result = module._enrich_stage4(stage3, {"603330": state}, [])
    candidate = result["candidates"][0]
    assert candidate["stock_role"] == "MARKET_LEADER"
    assert candidate["theme_analysis"]["stock_role"] == "MARKET_LEADER"
    assert candidate["weak_to_strong_analysis"]["stock_role"] == "MARKET_LEADER"


def test_multi_day_decline_is_not_high_score():
    module = _module()
    state = module._build_state(_record(pct_change_5d=-25.0, max_drawdown_3d=-30.0, bias_ma10=-12.0, current_change_pct=-6.0, recent_limit_up_count=0), {}, 0, 0, "分歧")
    assert state["final_weak_to_strong_score"] < 65
    assert "MULTI_DAY_DECLINE" in state["risk_penalties"]


def test_main_leader_first_pullback_gets_divergence_quality():
    module = _module()
    state = module._build_state(_record(current_change_pct=-2.0, recent_limit_up_count=1, pct_change_5d=10.0), {}, 1, 0, "分歧")
    assert "FIRST_STRONG_PULLBACK" in state["weak_signals"]
    assert state["score_components"]["divergence_quality"] is not None


def test_climax_reduces_next_day_space_adjustment():
    module = _module()
    climax = module._build_state(_record(), {}, 1, 1, "高潮")
    divergence = module._build_state(_record(), {}, 1, 1, "分歧")
    assert climax["sentiment_adjustment"] < divergence["sentiment_adjustment"]
    assert climax["final_weak_to_strong_score"] < divergence["final_weak_to_strong_score"]


def test_divergence_environment_adds_core_priority():
    module = _module()
    state = module._build_state(_record(), {}, 1, 1, "分歧")
    assert state["sentiment_adjustment"] == 8.0


def test_retreat_environment_lowers_score():
    module = _module()
    retreat = module._build_state(_record(), {}, 1, 1, "退潮")
    recovery = module._build_state(_record(), {}, 1, 1, "修复")
    assert retreat["final_weak_to_strong_score"] < recovery["final_weak_to_strong_score"]


def test_stage4_candidate_order_is_preserved():
    module = _module()
    stage3 = {"candidates": [{"code": "000002", "name": "B"}, {"code": "000001", "name": "A"}]}
    state = {"000001": {"code": "000001", "final_weak_to_strong_score": 80, "setup_grade": "A", "setup_type": "LEADER_DIVERGENCE"}, "000002": {"code": "000002", "final_weak_to_strong_score": 60, "setup_grade": "C", "setup_type": "FIRST_PULLBACK"}}
    result = module._enrich_stage4(stage3, state, [{"rank": 1, "code": "000001"}])
    assert [item["code"] for item in result["candidates"]] == ["000002", "000001"]


def test_missing_history_data_stays_none():
    module = _module()
    metrics = module._history_metrics([], date(2026, 1, 2))
    assert metrics["ma5"] is None
    assert metrics["volume_ratio_5d"] is None
    assert metrics["max_drawdown_3d"] is None


def test_all_missing_components_do_not_create_pseudo_score():
    module = _module()
    record = _record(primary_theme_role=None, stock_role=None, resonance_count=None, is_broken_board=None, is_limit_up=None, board_count=None, current_change_pct=None, recent_limit_up_count=None, pct_change_5d=None, bias_ma5=None, bias_ma10=None, close_position=None, turnover_rate=None, volume_ratio_5d=None)
    state = module._build_state(record, {}, None, None, None)
    assert state["weak_to_strong_score"] is None
    assert state["final_weak_to_strong_score"] is None
    assert state["data_quality"] == "unavailable"


def test_risk_penalties_sum_correctly():
    module = _module()
    risks = module._risk_penalties(_record(is_limit_down=True, pct_change_5d=-25.0, max_drawdown_3d=-30.0, bias_ma10=-10.0))
    assert risks["LIMIT_DOWN"] == 30.0
    assert risks["A_SHAPE"] == 25.0
    assert sum(risks.values()) >= 70.0


def test_watchlist_is_capped_at_ten():
    module = _module()
    states = []
    for index in range(12):
        states.append({"code": f"000{index:03d}", "name": str(index), "setup_grade": "A" if index < 4 else "B", "setup_type": "FIRST_PULLBACK", "final_weak_to_strong_score": 90 - index, "primary_theme": "机器人", "primary_theme_role": "MAIN", "stock_role": "FRONT_CORE", "leader_score": 70, "weak_signals": ["FIRST_STRONG_PULLBACK"], "strength_foundation": ["MAIN题材"], "risk_penalties": {}, "tomorrow_plan": {}})
    watchlist = module._watchlist(states, {"max_watchlist_size": 12})
    assert len(watchlist) == 10
