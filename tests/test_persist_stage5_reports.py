"""Tests for stable Stage5 report persistence."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.persist_stage5_reports import REPORT_FILES, persist_reports


def _write_source(source: Path, *, target_date: str = "20260818", status: str = "AUCTION_WINDOW") -> None:
    source.mkdir(parents=True, exist_ok=True)
    payload = {
        "target_date": target_date,
        "auction_status": status,
        "data_quality": "complete",
        "final_snapshot_only": False,
        "stage4_source_run_id": "12345",
        "stage4_source_date": "20260817",
    }
    (source / "auction_confirmation.json").write_text(json.dumps(payload), encoding="utf-8")
    for filename in REPORT_FILES[1:]:
        (source / filename).write_text(f"{filename}\n", encoding="utf-8")


def test_success_copies_latest_history_and_metadata(tmp_path):
    source = tmp_path / "source"
    latest = tmp_path / "reports" / "short_term" / "latest_stage5"
    history = tmp_path / "reports" / "short_term" / "history" / "stage5"
    _write_source(source)

    payload, changed = persist_reports(source, latest, history)

    assert changed is True
    assert (latest / "auction_confirmation.json").is_file()
    assert (history / "20260818" / "candidate_pool_stage5.md").is_file()
    metadata = json.loads((latest / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["stage"] == "stage5"
    assert metadata["target_date"] == "20260818"
    assert metadata["stage4_source_run_id"] == "12345"
    assert payload["target_date"] == "20260818"


def test_failure_does_not_overwrite_latest(tmp_path):
    source = tmp_path / "source"
    latest = tmp_path / "latest_stage5"
    history = tmp_path / "history"
    _write_source(source)
    latest.mkdir(parents=True)
    sentinel = latest / "auction_confirmation.json"
    sentinel.write_text("previous-valid-result", encoding="utf-8")
    (source / "auction_confirmation.json").write_text(json.dumps({"target_date": "20260818", "error": {"code": "STALE_STAGE4_INPUT"}}), encoding="utf-8")

    try:
        persist_reports(source, latest, history)
    except ValueError:
        pass
    else:
        raise AssertionError("fatal Stage5 result must be rejected")
    assert sentinel.read_text(encoding="utf-8") == "previous-valid-result"


def test_repeating_same_day_is_safe_and_reports_no_changes(tmp_path):
    source = tmp_path / "source"
    latest = tmp_path / "latest_stage5"
    history = tmp_path / "history"
    _write_source(source)

    _, first_changed = persist_reports(source, latest, history)
    _, second_changed = persist_reports(source, latest, history)

    assert first_changed is True
    assert second_changed is False


def test_missing_target_date_is_rejected(tmp_path):
    source = tmp_path / "source"
    _write_source(source)
    (source / "auction_confirmation.json").write_text(json.dumps({"auction_status": "AUCTION_WINDOW"}), encoding="utf-8")

    try:
        persist_reports(source, tmp_path / "latest", tmp_path / "history")
    except ValueError as exc:
        assert "target_date" in str(exc)
    else:
        raise AssertionError("missing target_date must be rejected")
