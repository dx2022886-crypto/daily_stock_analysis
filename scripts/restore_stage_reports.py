#!/usr/bin/env python3
"""Restore validated latest Stage1-Stage4 reports for downstream workflows."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = PROJECT_ROOT / "reports" / "short_term"

STAGE_FILES: dict[str, tuple[str, ...]] = {
    "stage1": ("candidate_pool.json", "candidate_pool.md"),
    "stage2": ("market_sentiment.json", "market_sentiment.md", "candidate_pool_enriched.json", "candidate_pool_enriched.md"),
    "stage3": ("theme_leader.json", "theme_leader.md", "candidate_pool_stage3.json", "candidate_pool_stage3.md"),
    "stage4": ("weak_to_strong.json", "weak_to_strong.md", "candidate_pool_stage4.json", "candidate_pool_stage4.md"),
}


def _normalize_date(value: Any) -> str:
    text = str(value or "").strip().replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def _payload_date(payload: dict[str, Any], metadata: dict[str, Any]) -> str:
    for value in (
        payload.get("target_date"),
        payload.get("date"),
        (payload.get("current") or {}).get("date") if isinstance(payload.get("current"), dict) else None,
        metadata.get("target_date"),
    ):
        normalized = _normalize_date(value)
        if normalized:
            return normalized
    return ""


def restore_reports(stages: list[str], *, reports_root: Path, target_date: str = "") -> dict[str, Any]:
    source_root = reports_root
    restored: dict[str, Any] = {}
    expected = _normalize_date(target_date)
    if target_date and not expected:
        raise ValueError("target date must be YYYYMMDD")

    for stage in stages:
        key = stage.lower()
        if key not in STAGE_FILES:
            raise ValueError(f"unsupported stage: {stage}")
        latest = source_root / f"latest_{key}"
        metadata_path = latest / "metadata.json"
        if not latest.is_dir():
            raise FileNotFoundError(f"missing {latest}; run the upstream stage first")
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.is_file() else {}
            metadata = metadata if isinstance(metadata, dict) else {}
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid {metadata_path}") from exc

        json_file = next(name for name in STAGE_FILES[key] if name.endswith(".json"))
        payload = json.loads((latest / json_file).read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"{latest / json_file} must contain an object")
        actual = _payload_date(payload, metadata)
        if expected and actual and actual != expected:
            raise ValueError(f"{key} target_date={actual} does not match requested target_date={expected}")
        for filename in STAGE_FILES[key]:
            source = latest / filename
            if not source.is_file():
                raise FileNotFoundError(f"{latest} missing {filename}")
            shutil.copy2(source, source_root / filename)
        restored[key] = {"target_date": actual, "source": str(latest)}
    return restored


def main() -> int:
    parser = argparse.ArgumentParser(description="Restore latest short-term stage reports.")
    parser.add_argument("--stages", nargs="+", choices=tuple(STAGE_FILES), required=True)
    parser.add_argument("--target-date", default="")
    parser.add_argument("--reports-root", type=Path, default=REPORT_ROOT)
    args = parser.parse_args()
    try:
        result = restore_reports(args.stages, reports_root=args.reports_root, target_date=args.target_date)
    except Exception as exc:
        print(f"Unable to restore latest reports: {exc}")
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
