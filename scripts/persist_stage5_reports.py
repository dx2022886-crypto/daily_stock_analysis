#!/usr/bin/env python3
"""Persist a successful Stage5 result as a stable latest and dated snapshot."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPORT_FILES = (
    "auction_confirmation.json",
    "auction_confirmation.md",
    "candidate_pool_stage5.json",
    "candidate_pool_stage5.md",
)
FATAL_STATUSES = {
    "LIVE_DATE_MISMATCH",
    "NON_TRADING_DAY",
    "STALE_STAGE4_INPUT",
    "SNAPSHOT_FILE_REQUIRED",
    "BEFORE_AUCTION",
    "OUTSIDE_WINDOW",
}


def _load_result(source_dir: Path) -> dict[str, Any]:
    result_path = source_dir / "auction_confirmation.json"
    if not result_path.is_file():
        raise ValueError(f"missing {result_path}")
    payload = json.loads(result_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("auction_confirmation.json must contain an object")
    if payload.get("error"):
        raise ValueError(f"Stage5 result contains fatal error: {payload['error']}")
    if payload.get("auction_status") in FATAL_STATUSES:
        raise ValueError(f"Stage5 result has fatal status: {payload['auction_status']}")
    target_date = str(payload.get("target_date") or "")
    if len(target_date) != 8 or not target_date.isdigit():
        raise ValueError("Stage5 result must contain target_date in YYYYMMDD format")
    for filename in REPORT_FILES:
        path = source_dir / filename
        if not path.is_file():
            raise ValueError(f"missing {path}")
    return payload


def _metadata(payload: dict[str, Any], generated_at: str | None = None) -> dict[str, Any]:
    return {
        "stage": "stage5",
        "target_date": payload["target_date"],
        "generated_at": generated_at or payload.get("generated_at") or datetime.now(timezone.utc).isoformat(),
        "stage4_source_run_id": payload.get("stage4_source_run_id"),
        "stage4_source_date": payload.get("stage4_source_date"),
        "auction_status": payload.get("auction_status"),
        "data_quality": payload.get("data_quality"),
        "final_snapshot_only": bool(payload.get("final_snapshot_only", False)),
    }


def _same_file(left: Path, right: Path) -> bool:
    if not left.is_file() or not right.is_file():
        return False
    return left.read_bytes() == right.read_bytes()


def _copy_tree(source_dir: Path, destination_dir: Path, metadata: dict[str, Any]) -> bool:
    destination_dir.mkdir(parents=True, exist_ok=True)
    changed = False
    for filename in REPORT_FILES:
        source = source_dir / filename
        destination = destination_dir / filename
        if not _same_file(source, destination):
            shutil.copy2(source, destination)
            changed = True
    metadata_path = destination_dir / "metadata.json"
    metadata_text = json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if not metadata_path.is_file() or metadata_path.read_text(encoding="utf-8") != metadata_text:
        metadata_path.write_text(metadata_text, encoding="utf-8")
        changed = True
    return changed


def persist_reports(source_dir: Path, latest_dir: Path, history_root: Path) -> tuple[dict[str, Any], bool]:
    """Validate first, then update latest and the target-date history snapshot."""
    payload = _load_result(source_dir)
    target_date = payload["target_date"]
    latest_metadata_path = latest_dir / "metadata.json"
    generated_at: str | None = None
    source_unchanged = all(_same_file(source_dir / filename, latest_dir / filename) for filename in REPORT_FILES)
    if source_unchanged and latest_metadata_path.is_file():
        try:
            existing_metadata = json.loads(latest_metadata_path.read_text(encoding="utf-8"))
            if isinstance(existing_metadata, dict) and existing_metadata.get("generated_at"):
                generated_at = str(existing_metadata["generated_at"])
        except (OSError, ValueError, TypeError):
            generated_at = None
    metadata = _metadata(payload, generated_at=generated_at)
    latest_dir.parent.mkdir(parents=True, exist_ok=True)
    history_dir = history_root / target_date
    staging_root = Path(tempfile.mkdtemp(prefix=".stage5-persist-", dir=str(latest_dir.parent)))
    try:
        staged_latest = staging_root / "latest_stage5"
        staged_history = staging_root / "history"
        _copy_tree(source_dir, staged_latest, metadata)
        _copy_tree(source_dir, staged_history, metadata)

        changed = False
        latest_dir.mkdir(parents=True, exist_ok=True)
        history_dir.mkdir(parents=True, exist_ok=True)
        for filename in (*REPORT_FILES, "metadata.json"):
            latest_source = staged_latest / filename
            latest_destination = latest_dir / filename
            history_source = staged_history / filename
            history_destination = history_dir / filename
            if not _same_file(latest_source, latest_destination):
                os.replace(latest_source, latest_destination)
                changed = True
            if not _same_file(history_source, history_destination):
                os.replace(history_source, history_destination)
                changed = True
        return payload, changed
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Persist successful Stage5 reports.")
    parser.add_argument("--source-dir", default="reports/short_term", type=Path)
    parser.add_argument("--latest-dir", default="reports/short_term/latest_stage5", type=Path)
    parser.add_argument("--history-root", default="reports/short_term/history/stage5", type=Path)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    try:
        payload, changed = persist_reports(args.source_dir, args.latest_dir, args.history_root)
    except Exception as exc:
        print(f"Stage5 reports were not persisted: {exc}")
        return 1
    print(f"Stage5 reports target_date={payload['target_date']} changed={str(changed).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
