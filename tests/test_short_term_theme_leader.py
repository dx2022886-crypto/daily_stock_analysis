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


def _source(function, source="eastmoney", status="success", rows=0):
    result = {"function": function, "source": source, "status": status, "rows": rows, "attempts": 1, "params": {}}
    if status != "success":
        result["error"] = {"type": "RuntimeError", "message": f"{function} unavailable"}
    return result


def _market(module, limit_up=None, broken=None, hot=None, *, limit_up_ok=True, broken_ok=True, hot_ok=True):
    limit_up = limit_up or []
    broken = broken or []
    hot = hot or []
    return {
        "date": "20260817",
        "limit_up": limit_up,
        "broken_board": broken,
        "hot": hot,
        "limit_up_source": _source("stock_zt_pool_em", rows=len(limit_up), status="success" if limit_up_ok else "failed"),
        "broken_board_source": _source("stock_zt_pool_zbgc_em", rows=len(broken), status="success" if broken_ok else "failed"),
        "hot_source": _source("stock_hot_rank_em", rows=len(hot), status="success" if hot_ok else "failed"),
    }


def _fake_universe_fetch(monkeypatch, module, responses):
    module._API_CACHE.clear()
    module._API_STATS.update(requests=0, cache_hits=0)
    functions = {
        "stock_board_concept_name_em", "stock_board_concept_cons_em", "stock_board_concept_hist_em",
        "stock_board_industry_name_em", "stock_board_industry_cons_em",
        "stock_board_concept_name_ths", "stock_board_concept_index_ths",
        "stock_board_concept_cons_ths", "stock_board_cons_ths",
        "stock_board_industry_name_ths", "stock_board_industry_index_ths",
        "stock_board_industry_summary_ths", "stock_board_industry_cons_ths",
    }
    monkeypatch.setattr(module, "ak", types.SimpleNamespace(**{name: object() for name in functions}), raising=False)

    def fake_fetch(function, *, source="akshare", **kwargs):
        value = responses.get((function, source), responses.get(function, []))
        if isinstance(value, tuple):
            rows, status = value
        else:
            rows, status = value, "success"
        rows = rows if isinstance(rows, list) else []
        return rows, _source(function, source, status, len(rows))

    monkeypatch.setattr(module, "_fetch", fake_fetch)


def test_score_exposes_coverage_and_confidence_adjustment(monkeypatch):
    module = _module()
    scored = module._score_components({"a": 10, "b": None}, {"a": 10, "b": 30})
    assert scored["coverage_ratio"] == 0.25
    assert scored["normalized_score"] == 100
    assert scored["confidence_adjusted_score"] == 50


def test_endpoint_cache_calls_same_endpoint_and_params_once(monkeypatch):
    module = _module()
    calls = []

    def endpoint(**kwargs):
        calls.append(kwargs)
        return [{"代码": "000008"}]

    module._API_CACHE.clear()
    module._API_STATS.update(requests=0, cache_hits=0)
    monkeypatch.setattr(module, "ak", types.SimpleNamespace(stock_hot_rank_em=endpoint), raising=False)
    first, first_meta = module._fetch("stock_hot_rank_em", source="eastmoney", date="20260817")
    second, second_meta = module._fetch("stock_hot_rank_em", source="eastmoney", date="20260817")
    assert first == second == [{"代码": "000008"}]
    assert len(calls) == 1
    assert first_meta.get("cache_hit") is not True
    assert second_meta["cache_hit"] is True
    assert module._API_STATS == {"requests": 1, "cache_hits": 1}


def test_em_theme_universe_is_normalized(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": [{"板块名称": "机器人", "板块代码": "BK001"}],
        "stock_board_concept_cons_em": [{"代码": "000001", "名称": "甲"}],
        "stock_board_concept_hist_em": [{"涨跌幅": 3.2}],
        "stock_board_industry_name_em": [{"行业名称": "机械设备", "行业代码": "I001"}],
        "stock_board_industry_cons_em": [{"代码": "000001", "所属行业": "机械设备"}],
    }
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", _market(module), {"000001": {"code": "000001"}})
    assert universe["source_mode"] == "FULL_EASTMONEY"
    assert universe["themes"]["机器人"]["theme_type"] == "CONCEPT"
    assert universe["stock_to_themes"]["000001"] == ["机器人", "机械设备"]


def test_ths_concept_fallback_is_used_when_em_concepts_fail(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": ([], "failed"),
        "stock_board_concept_name_ths": [{"名称": "新能源", "代码": "T001"}],
        "stock_board_concept_cons_ths": [{"代码": "000002", "名称": "乙"}],
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": [{"名称": "电力设备", "代码": "I002"}],
        "stock_board_industry_cons_ths": [{"代码": "000002", "行业": "电力设备"}],
    }
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", _market(module), {"000002": {"code": "000002"}})
    assert universe["source_mode"] == "FULL_THS"
    assert universe["themes"]["新能源"]["source"] == "ths"
    assert "000002" in universe["stock_to_themes"]


def test_ths_industry_fallback_supplies_industry_mapping(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": [{"板块名称": "算力", "板块代码": "C001"}],
        "stock_board_concept_cons_em": [{"代码": "000003"}],
        "stock_board_concept_hist_em": [{"涨跌幅": 1.0}],
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": [{"名称": "通信", "代码": "I003"}],
        "stock_board_industry_cons_ths": [{"代码": "000003", "行业": "通信"}],
    }
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", _market(module), {"000003": {"code": "000003"}})
    assert universe["data_coverage"]["industry_available"] is True
    assert "通信" in universe["stock_to_industries"]["000003"]


def test_pool_industry_cluster_is_used_when_both_concept_sources_fail(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": ([], "failed"),
        "stock_board_concept_name_ths": ([], "failed"),
        "stock_board_concept_index_ths": ([], "failed"),
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": ([], "failed"),
        "stock_board_industry_index_ths": ([], "failed"),
        "stock_board_industry_summary_ths": ([], "failed"),
    }
    market = _market(module, [{"代码": "000004", "名称": "丁", "所属行业": "芯片", "连板数": 3}])
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", market, {"000004": {"code": "000004"}})
    assert universe["source_mode"] == "INDUSTRY_DEGRADED"
    assert universe["themes"]["芯片"]["is_degraded"] is True
    assert universe["themes"]["芯片"]["source"] == "limit_up_industry_cluster"


def test_source_failures_keep_function_source_attempts_and_error(monkeypatch):
    module = _module()
    responses = {"stock_board_concept_name_em": ([], "failed")}
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", _market(module), {})
    failure = next(item for item in universe["source_failures"] if item["function"] == "stock_board_concept_name_em")
    assert failure["source"] == "eastmoney"
    assert failure["attempts"] == 1
    assert failure["error"]["type"] == "RuntimeError"


def test_market_only_leaders_survive_without_any_theme(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": ([], "failed"),
        "stock_board_concept_name_ths": ([], "failed"),
        "stock_board_concept_index_ths": ([], "failed"),
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": ([], "failed"),
        "stock_board_industry_index_ths": ([], "failed"),
        "stock_board_industry_summary_ths": ([], "failed"),
    }
    market = _market(module, [{"代码": "000005", "名称": "戊", "连板数": 4, "首次封板时间": "09:35"}], hot=[{"代码": "000005", "当前排名": 2}])
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", market, {})
    assert universe["source_mode"] == "MARKET_ONLY"
    records = module._build_stock_records({}, universe["stock_to_themes"], universe["stock_to_industries"], {}, market)
    leaders, market_leaders = module._build_leaders(records, {})
    assert leaders and market_leaders
    assert market_leaders[0]["leader_source_mode"] == "market_only"


def test_unavailable_market_has_no_fabricated_market_leaders(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": ([], "failed"),
        "stock_board_concept_name_ths": ([], "failed"),
        "stock_board_concept_index_ths": ([], "failed"),
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": ([], "failed"),
        "stock_board_industry_index_ths": ([], "failed"),
        "stock_board_industry_summary_ths": ([], "failed"),
    }
    _fake_universe_fetch(monkeypatch, module, responses)
    market = _market(module, limit_up_ok=False, broken_ok=False, hot_ok=False)
    universe = module._fetch_theme_universe("20260817", market, {"000006": {"code": "000006"}})
    assert universe["source_mode"] == "UNAVAILABLE"
    assert universe["data_quality"] == "unavailable"


def test_degraded_theme_can_be_main_only_with_visible_pool_strength():
    module = _module()
    metrics = {"is_degraded": True, "limit_up_count": 8, "highest_board": 4, "coverage_ratio": 0.8}
    assert module._theme_role(65, 1, metrics, 65) == "MAIN"
    assert metrics["is_degraded_main"] is True


def test_low_coverage_theme_cannot_be_main():
    module = _module()
    assert module._theme_role(95, 1, {"coverage_ratio": 0.25}, 95) == "ROTATION"


def test_missing_sector_momentum_stays_missing():
    module = _module()
    components = module._theme_components({"limit_up_count": 2, "member_count": 10, "board_change_pct": None, "average_change_pct": 2})
    assert components["sector_momentum"] is None


def test_theme_mapping_is_deduplicated_and_sources_are_retained(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": [{"板块名称": "机器人", "板块代码": "C001"}],
        "stock_board_concept_cons_em": [{"代码": "000007"}],
        "stock_board_concept_hist_em": [{"涨跌幅": 2}],
        "stock_board_industry_name_em": [{"名称": "机械", "代码": "I001"}],
        "stock_board_industry_cons_em": [{"代码": "000007", "行业": "机械"}],
    }
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", _market(module), {"000007": {"code": "000007"}})
    assert universe["stock_to_themes"]["000007"] == ["机器人", "机械"]
    assert set(universe["theme_sources"]["000007"]["sources"]) == {"eastmoney"}


def test_incident_style_pool_failure_still_builds_degraded_themes_and_leaders(monkeypatch):
    module = _module()
    responses = {
        "stock_board_concept_name_em": ([], "failed"),
        "stock_board_concept_name_ths": ([], "failed"),
        "stock_board_concept_index_ths": ([], "failed"),
        "stock_board_industry_name_em": ([], "failed"),
        "stock_board_industry_name_ths": ([], "failed"),
        "stock_board_industry_index_ths": ([], "failed"),
        "stock_board_industry_summary_ths": ([], "failed"),
    }
    rows = [{"代码": f"0000{i:02d}", "名称": f"股{i}", "所属行业": "通信", "连板数": 5 if i == 1 else 1, "首次封板时间": "09:35"} for i in range(1, 13)]
    candidates = {"000001": {"code": "000001", "resonance_count": 3}, "000002": {"code": "000002", "resonance_count": 2}}
    market = _market(module, rows, hot=rows[:3])
    _fake_universe_fetch(monkeypatch, module, responses)
    universe = module._fetch_theme_universe("20260817", market, candidates)
    metrics = module._build_theme_metrics(universe["themes"], candidates, universe["stock_to_themes"], market)
    records = module._build_stock_records(candidates, universe["stock_to_themes"], universe["stock_to_industries"], metrics, market)
    _, market_leaders = module._build_leaders(records, metrics)
    ranked = sorted(metrics.values(), key=module._theme_sort_key)
    assert universe["source_mode"] == "INDUSTRY_DEGRADED"
    assert ranked and ranked[0]["theme_role"] == "MAIN"
    assert market_leaders
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
