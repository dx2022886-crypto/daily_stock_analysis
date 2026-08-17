"""Pure-rule tests for the stage-3 theme and leader layer."""

from __future__ import annotations

import importlib
import sys
import types


def _module():
    # Keep the tests runnable in a minimal checkout while CI still installs the
    # project's real AKShare/pandas dependencies.
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
    return importlib.import_module("scripts.run_short_term_theme_leader")


def test_empty_limit_up_data_is_not_fabricated_into_full_theme_score():
    module = _module()
    metrics = {
        "limit_up_count": 0,
        "broken_board_count": 0,
        "member_count": 20,
        "highest_board": 0,
        "candidate_count": 0,
        "candidate_resonance_sum": 0,
        "average_change_pct": 0,
        "board_change_pct": 0,
        "hot_stock_count": 0,
        "ladder_counts": {"1": 0, "2": 0, "3_plus": 0},
    }
    scored = module._score_components(module._theme_components(metrics), module.THEME_WEIGHTS)
    assert scored["data_quality"] == "complete"
    assert scored["normalized_score"] < 100


def test_multiple_themes_are_preserved_and_primary_theme_uses_score():
    module = _module()
    metrics = {
        "Alpha": {"theme_score": 60, "theme_role": "SECONDARY", "limit_up_count": 2},
        "Beta": {"theme_score": 80, "theme_role": "MAIN", "limit_up_count": 1},
    }
    assert module._select_primary_theme(["Alpha", "Beta"], metrics) == "Beta"


def test_primary_theme_tie_breaks_role_before_board_count():
    module = _module()
    metrics = {
        "Alpha": {"theme_score": 70, "theme_role": "SECONDARY", "limit_up_count": 10},
        "Beta": {"theme_score": 70, "theme_role": "MAIN", "limit_up_count": 1},
    }
    assert module._select_primary_theme(["Alpha", "Beta"], metrics) == "Beta"


def test_highest_board_gets_market_leader_role():
    module = _module()
    stocks = {
        "000001": {"code": "000001", "name": "A", "themes": ["机器人"], "primary_theme": "机器人", "primary_theme_role": "MAIN", "is_limit_up": True, "is_broken_board": False, "board_count": 4, "first_limit_time": "09:35", "break_count": 0, "hot_rank": 3, "resonance_count": 3, "candidate": True},
        "000002": {"code": "000002", "name": "B", "themes": ["机器人"], "primary_theme": "机器人", "primary_theme_role": "MAIN", "is_limit_up": True, "is_broken_board": False, "board_count": 2, "first_limit_time": "10:30", "break_count": 0, "hot_rank": 30, "resonance_count": 1, "candidate": False},
    }
    theme_metrics = {"机器人": {"theme_role": "MAIN", "theme_score": 80, "board_change_pct": 3, "average_change_pct": 2, "limit_up_count": 2}}
    _, market_leaders = module._build_leaders(stocks, theme_metrics)
    assert market_leaders[0]["code"] == "000001"
    assert market_leaders[0]["stock_role"] == "MARKET_LEADER"


def test_broken_board_is_penalized_against_same_stock_without_breaks():
    module = _module()
    common = {"themes": ["机器人"], "primary_theme": "机器人", "primary_theme_role": "MAIN", "board_count": 2, "first_limit_time": "09:35", "hot_rank": 5, "resonance_count": 2, "candidate": True}
    intact = {"code": "000001", "name": "A", **common, "is_limit_up": True, "is_broken_board": False, "break_count": 0}
    broken = {"code": "000002", "name": "B", **common, "is_limit_up": False, "is_broken_board": True, "break_count": 3}
    theme_metrics = {"机器人": {"theme_role": "MAIN", "theme_score": 80, "board_change_pct": 3, "average_change_pct": 2, "limit_up_count": 2}}
    stocks = {"000001": intact, "000002": broken}
    leaders, _ = module._build_leaders(stocks, theme_metrics)
    scores = {item["code"]: item["leader_score"] for item in leaders}
    assert scores["000001"] > scores["000002"]
    assert stocks["000002"]["stock_role"] == "BROKEN_CORE"


def test_missing_popularity_component_is_normalized_without_zero_fill():
    module = _module()
    components = {"limit_up_strength": 25, "board_height": 15, "candidate_resonance": 15, "sector_momentum": 15, "popularity": None, "seal_quality": 10, "ladder_quality": 10}
    scored = module._score_components(components, module.THEME_WEIGHTS)
    assert scored["data_quality"] == "partial"
    assert scored["available_weight"] == 90
    assert scored["normalized_score"] == 100


def test_missing_sector_momentum_component_is_normalized_without_zero_fill():
    module = _module()
    components = {"limit_up_strength": 25, "board_height": 15, "candidate_resonance": 15, "sector_momentum": None, "popularity": 10, "seal_quality": 10, "ladder_quality": 10}
    scored = module._score_components(components, module.THEME_WEIGHTS)
    assert scored["data_quality"] == "partial"
    assert scored["normalized_score"] == 100


def test_candidate_pool_enrichment_keeps_original_order():
    module = _module()
    payload = {"candidates": [{"code": "000002", "name": "B"}, {"code": "000001", "name": "A"}]}
    stocks = {
        "000001": {"themes": ["Beta"], "industry": "行业A", "primary_theme_rank": 1, "leader_score": 70, "stock_role": "THEME_LEADER", "leader_reasons": []},
        "000002": {"themes": ["Alpha"], "industry": "行业B", "primary_theme_rank": 2, "leader_score": 60, "stock_role": "FRONT_CORE", "leader_reasons": []},
    }
    themes = {"Alpha": {"theme_score": 60, "theme_role": "SECONDARY"}, "Beta": {"theme_score": 80, "theme_role": "MAIN"}}
    result = module._enrich_candidates(payload, stocks, themes)
    assert [item["code"] for item in result["candidates"]] == ["000002", "000001"]


def test_score_normalization_uses_available_weight():
    module = _module()
    scored = module._score_components({"a": 5, "b": None}, {"a": 5, "b": 5})
    assert scored["score_raw"] == 5
    assert scored["available_weight"] == 5
    assert scored["normalized_score"] == 100


def test_all_missing_components_do_not_become_zero():
    module = _module()
    scored = module._score_components({key: None for key in module.THEME_WEIGHTS}, module.THEME_WEIGHTS)
    assert scored["data_quality"] == "unavailable"
    assert scored["score_raw"] is None
    assert scored["normalized_score"] is None
