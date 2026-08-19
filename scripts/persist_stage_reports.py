#!/usr/bin/env python3
"""Persist successful short-term Stage1-Stage4 reports.

The stage runners continue to write their normal reports directory.  This
small adapter copies only validated outputs into stable ``latest_stageX``
directories and dated history snapshots so consumers such as the dashboard do
not depend on an Actions workspace or artifact name.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SHANGHAI = ZoneInfo("Asia/Shanghai")

STAGE_SPECS: dict[str, tuple[str, ...]] = {
    "stage1": ("candidate_pool.json", "candidate_pool.md"),
    "stage2": (
        "market_sentiment.json",
        "market_sentiment.md",
        "candidate_pool_enriched.json",
        "candidate_pool_enriched.md",
    ),
    "stage3": (
        "theme_leader.json",
        "theme_leader.md",
        "candidate_pool_stage3.json",
        "candidate_pool_stage3.md",
    ),
    "stage4": (
        "weak_to_strong.json",
        "weak_to_strong.md",
        "candidate_pool_stage4.json",
        "candidate_pool_stage4.md",
    ),
}


def _stage_number(stage: str) -> str:
    normalized = stage.strip().lower()
    if normalized.startswith("stage"):
        normalized = normalized[5:]
    if normalized not in {"1", "2", "3", "4"}:
        raise ValueError(f"unsupported stage: {stage}")
    return normalized


def _stage_key(stage: str) -> str:
    return f"stage{_stage_number(stage)}"


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain an object")
    return payload


def _target_date(payload: dict[str, Any]) -> str:
    for key in ("target_date", "date", "market_ecology_date"):
        value = payload.get(key)
        if value is not None and str(value).strip():
            text = str(value).replace("-", "").replace("/", "")
            if len(text) == 8 and text.isdigit():
                return text
    current = payload.get("current")
    if isinstance(current, dict):
        value = current.get("date")
        if value is not None:
            text = str(value).replace("-", "").replace("/", "")
            if len(text) == 8 and text.isdigit():
                return text
    return datetime.now(SHANGHAI).strftime("%Y%m%d")


def _metadata(stage: str, payload: dict[str, Any], generated_at: str | None = None) -> dict[str, Any]:
    return {
        "stage": stage,
        "target_date": _target_date(payload),
        "generated_at": generated_at or datetime.now(SHANGHAI).isoformat(timespec="seconds"),
        "data_quality": payload.get("data_quality"),
        "phase": payload.get("phase"),
    }


def _same_file(left: Path, right: Path) -> bool:
    return left.is_file() and right.is_file() and left.read_bytes() == right.read_bytes()


def _validate_source(stage: str, source_dir: Path) -> tuple[dict[str, Any], tuple[str, ...]]:
    files = STAGE_SPECS[stage]
    json_name = next(filename for filename in files if filename.endswith(".json"))
    payload = _read_json(source_dir / json_name)
    missing = [filename for filename in files if not (source_dir / filename).is_file()]
    if missing:
        raise ValueError(f"{stage} missing required reports: {', '.join(missing)}")
    if payload.get("error") and stage != "stage1":
        raise ValueError(f"{stage} result contains error: {payload['error']}")
    return payload, files


def _copy_validated(
    stage: str,
    source_dir: Path,
    latest_dir: Path,
    history_root: Path,
) -> tuple[dict[str, Any], bool]:
    payload, files = _validate_source(stage, source_dir)
    latest_metadata_path = latest_dir / "metadata.json"
    generated_at: str | None = None
    if all(_same_file(source_dir / filename, latest_dir / filename) for filename in files) and latest_metadata_path.is_file():
        try:
            existing = _read_json(latest_metadata_path)
            generated_at = str(existing.get("generated_at") or "") or None
        except ValueError:
            generated_at = None
    metadata = _metadata(stage, payload, generated_at=generated_at)
    date_key = metadata["target_date"]
    history_dir = history_root / date_key

    latest_dir.parent.mkdir(parents=True, exist_ok=True)
    staging_root = Path(tempfile.mkdtemp(prefix=f".{stage}-persist-", dir=str(latest_dir.parent)))
    changed = False
    try:
        staged_latest = staging_root / "latest"
        staged_history = staging_root / "history"
        for destination in (staged_latest, staged_history):
            destination.mkdir(parents=True, exist_ok=True)
            for filename in files:
                shutil.copy2(source_dir / filename, destination / filename)
            (destination / "metadata.json").write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

        latest_dir.mkdir(parents=True, exist_ok=True)
        history_dir.mkdir(parents=True, exist_ok=True)
        for filename in (*files, "metadata.json"):
            for source, destination in (
                (staged_latest / filename, latest_dir / filename),
                (staged_history / filename, history_dir / filename),
            ):
                if not _same_file(source, destination):
                    os.replace(source, destination)
                    changed = True
        return payload, changed
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)


def persist_reports(
    stages: list[str] | tuple[str, ...],
    *,
    source_dir: Path,
    reports_root: Path,
) -> dict[str, Any]:
    """Validate and persist all requested stages, returning change details.

    Validation happens before any requested stage is copied.  A failed stage
    therefore cannot replace a previously valid latest snapshot.
    """

    normalized = [_stage_key(stage) for stage in stages]
    if not normalized:
        raise ValueError("at least one stage is required")
    if len(set(normalized)) != len(normalized):
        raise ValueError("duplicate stage requested")
    validated: list[tuple[str, dict[str, Any]]] = []
    for stage in normalized:
        payload, _ = _validate_source(stage, source_dir)
        validated.append((stage, payload))

    results: dict[str, Any] = {"changed": False, "stages": {}}
    for stage, _ in validated:
        payload, changed = _copy_validated(
            stage,
            source_dir,
            reports_root / f"latest_{stage}",
            reports_root / "history" / stage,
        )
        results["changed"] = bool(results["changed"] or changed)
        results["stages"][stage] = {
            "changed": changed,
            "target_date": _target_date(payload),
        }
    return results


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Persist successful Stage1-Stage4 reports.")
    parser.add_argument("--stages", nargs="+", required=True, choices=tuple(STAGE_SPECS), help="Stages to persist.")
    parser.add_argument("--source-dir", type=Path, default=PROJECT_ROOT / "reports" / "short_term")
    parser.add_argument("--reports-root", type=Path, default=PROJECT_ROOT / "reports" / "short_term")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    try:
        result = persist_reports(args.stages, source_dir=args.source_dir, reports_root=args.reports_root)
    except Exception as exc:
        print(f"Short-term reports were not persisted: {exc}")
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
