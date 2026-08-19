"""Offline tests for the static short-term decision dashboard."""

from __future__ import annotations

import json
from pathlib import Path

from dashboard.build_dashboard import STAGE_FILES, build_dashboard


def _write_stage(reports_root: Path, stage: str, payloads: dict[str, dict]) -> None:
    latest = reports_root / f"latest_{stage}"
    latest.mkdir(parents=True, exist_ok=True)
    for filename in STAGE_FILES[stage]:
        if filename.endswith(".json"):
            payload = payloads.get(filename, {})
            (latest / filename).write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        else:
            (latest / filename).write_text(f"# {filename}\n", encoding="utf-8")
    (latest / "metadata.json").write_text(
        json.dumps({"stage": stage, "target_date": "20260819", "generated_at": "2026-08-19T10:00:00+08:00"}),
        encoding="utf-8",
    )


def _seed_all_stages(reports_root: Path, *, poor_stage5: bool = False, empty_watchlist: bool = False) -> None:
    _write_stage(
        reports_root,
        "stage1",
        {"candidate_pool.json": {"candidates": [
            {"rank": index, "code": f"{index:06d}", "name": f"股票{index}", "resonance_count": 2 if index == 1 else 1, "strategies": ["volume_breakout"], "average_score": 70 + index}
            for index in range(1, 36)
        ]}},
    )
    _write_stage(
        reports_root,
        "stage2",
        {"market_sentiment.json": {
            "target_date": "20260819",
            "data_quality": "complete",
            "current": {
                "date": "20260819", "sentiment_phase": "启动", "sentiment_phase_code": "START",
                "sentiment_score": 72, "limit_up_count": 80, "limit_down_count": 4,
                "broken_board_count": 12, "broken_board_rate": 0.13, "highest_board": 5,
                "yesterday_premium_median": 2.4,
            },
        }, "candidate_pool_enriched.json": {"candidates": []}},
    )
    _write_stage(
        reports_root,
        "stage3",
        {"theme_leader.json": {
            "main_themes": [{"rank": 1, "theme": "AI算力", "theme_role": "MAIN", "theme_score": 88, "confidence_adjusted_score": 84, "coverage_ratio": 0.7}],
            "market_leaders": [{"code": "600001", "name": "龙头一号", "primary_theme": "AI算力", "stock_role": "MARKET_LEADER", "leader_score": 92, "market_leader_rank": 1}],
            "leaders": [{"code": "600002", "name": "前排二号", "primary_theme": "AI算力", "stock_role": "FRONT_CORE", "leader_score": 80}],
        }, "candidate_pool_stage3.json": {"candidates": []}},
    )
    _write_stage(
        reports_root,
        "stage4",
        {"weak_to_strong.json": {
            "target_date": "20260819",
            "next_day_watchlist": [] if empty_watchlist else [{"rank": 1, "code": "600001", "name": "龙头一号", "primary_theme": "AI算力", "stock_role": "MARKET_LEADER", "setup_type": "LEADER_DIVERGENCE", "final_weak_to_strong_score": 78, "setup_grade": "B"}],
            "weak_to_strong_states": [{"code": "600002", "name": "前排二号", "primary_theme": "AI算力", "stock_role": "FRONT_CORE", "setup_type": "FIRST_PULLBACK", "final_weak_to_strong_score": 63, "setup_grade": "C"}],
        }, "candidate_pool_stage4.json": {"candidates": []}},
    )
    _write_stage(
        reports_root,
        "stage5",
        {"auction_confirmation.json": {
            "target_date": "20260820",
            "data_quality": "partial",
            "source_mode": "QUOTE_PROXY",
            "snapshot_quality": {"quality": "POOR" if poor_stage5 else "GOOD", "captured_count": 2, "independent_request_count": 1, "cache_reused_count": 1 if poor_stage5 else 0},
            "auction_watchlist": [{"rank": 1, "code": "600001", "name": "龙头一号", "primary_theme": "AI算力", "stock_role": "MARKET_LEADER", "final_auction_score": 66, "auction_grade": "C", "auction_data_mode": "QUOTE_PROXY", "coverage_ratio": 0.5, "hard_reject_reasons": [], "auction_qualified": True}],
        }, "candidate_pool_stage5.json": {"candidates": []}},
    )


def test_all_stages_generate_complete_static_dashboard(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    output = tmp_path / "docs"
    _seed_all_stages(reports)

    data = build_dashboard(reports_root=reports, output_dir=output)

    assert data["market"]["sentiment_phase"] == "启动"
    assert data["pipeline_status"]["current_stage"] == "stage5"
    assert len(data["stage1_candidates"]) == 30
    assert len(data["leaders"]) == 2
    assert len(data["stage5"]["candidates"]) == 1
    assert (output / "index.html").is_file()
    assert (output / "dashboard_data.json").is_file()
    assert "A股短线决策中心" in (output / "index.html").read_text(encoding="utf-8")


def test_missing_stage5_is_non_fatal_and_explicitly_unavailable(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    output = tmp_path / "docs"
    _seed_all_stages(reports)
    for path in (reports / "latest_stage5").iterdir():
        path.unlink()
    (reports / "latest_stage5").rmdir()

    data = build_dashboard(reports_root=reports, output_dir=output)

    assert data["stage5"]["available"] is False
    assert data["pipeline_status"]["stages"]["stage5"] is False
    assert data["decision_state"] == "盘后候选已完成，等待下一交易日集合竞价"


def test_empty_stage4_watchlist_does_not_fabricate_candidates(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    _seed_all_stages(reports, empty_watchlist=True)

    data = build_dashboard(reports_root=reports, output_dir=tmp_path / "docs")

    assert data["stage4_watchlist"] == []
    assert [item["code"] for item in data["stage4_core_states"]] == ["600002"]


def test_main_themes_use_theme_field_and_unknown_phase_is_preserved(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    _seed_all_stages(reports)
    sentiment_path = reports / "latest_stage2" / "market_sentiment.json"
    sentiment = json.loads(sentiment_path.read_text(encoding="utf-8"))
    sentiment["current"]["sentiment_phase"] = "UNKNOWN"
    sentiment_path.write_text(json.dumps(sentiment), encoding="utf-8")

    data = build_dashboard(reports_root=reports, output_dir=tmp_path / "docs")

    assert data["themes"][0]["theme"] == "AI算力"
    assert data["market"]["sentiment_phase"] == "UNKNOWN"


def test_poor_stage5_quality_sets_warning_and_keeps_data(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    _seed_all_stages(reports, poor_stage5=True)

    data = build_dashboard(reports_root=reports, output_dir=tmp_path / "docs")

    assert data["stage5"]["snapshot_quality_label"] == "POOR"
    assert data["stage5"]["quality_warning"] is True
    assert data["stage5"]["candidates"][0]["data_mode"] == "QUOTE_PROXY"


def test_missing_all_latest_dirs_still_generates_utf8_page_and_complete_shape(tmp_path):
    output = tmp_path / "docs"

    data = build_dashboard(reports_root=tmp_path / "reports" / "short_term", output_dir=output)

    assert data["pipeline_status"]["current_stage"] is None
    assert data["decision_state"] == "暂无最新数据，等待阶段结果生成"
    assert set(data) >= {"generated_at", "market", "themes", "leaders", "stage1_candidates", "stage4_watchlist", "stage4_core_states", "stage5", "pipeline_status", "decision_state"}
    html = (output / "index.html").read_text(encoding="utf-8")
    assert "A股短线决策中心" in html
    assert "dashboard_data.json" in html


def test_candidate_pool_and_leaders_are_capped_for_mobile_dashboard(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    _seed_all_stages(reports)

    data = build_dashboard(reports_root=reports, output_dir=tmp_path / "docs")

    assert len(data["stage1_candidates"]) <= 30
    assert len(data["leaders"]) <= 10


def test_dashboard_data_json_has_required_top_level_fields(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    output = tmp_path / "docs"
    _seed_all_stages(reports)

    build_dashboard(reports_root=reports, output_dir=output)
    persisted = json.loads((output / "dashboard_data.json").read_text(encoding="utf-8"))

    assert set(persisted) >= {"generated_at", "market", "themes", "leaders", "stage1_candidates", "stage4_watchlist", "stage4_core_states", "stage5", "pipeline_status"}


def test_stage5_missing_state_has_waiting_message_in_static_template(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    output = tmp_path / "docs"
    _seed_all_stages(reports)
    for path in (reports / "latest_stage5").iterdir():
        path.unlink()
    (reports / "latest_stage5").rmdir()

    build_dashboard(reports_root=reports, output_dir=output)
    html = (output / "index.html").read_text(encoding="utf-8")

    assert "等待下一交易日集合竞价确认" in html


def test_poor_quality_warning_is_present_in_static_template(tmp_path):
    reports = tmp_path / "reports" / "short_term"
    output = tmp_path / "docs"
    _seed_all_stages(reports, poor_stage5=True)

    build_dashboard(reports_root=reports, output_dir=output)
    html = (output / "index.html").read_text(encoding="utf-8")

    assert "竞价数据质量不足，请降低结果可信度" in html
