# -*- coding: utf-8 -*-
"""Request-scoped caches and performance counters for short-term runs.

This module is orchestration-only.  It does not change screening formulas or
strategy configuration; it prevents identical provider requests from being
repeated by several strategies in one Stage1 process.
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
import os
from pathlib import Path
import threading
import time
from typing import Any, Callable, Iterator
import logging

import pandas as pd

logger = logging.getLogger(__name__)


class ShortTermRunContext:
    """Shared, request-scoped state for Stage1's four strategy calls."""

    def __init__(self, *, market: str = "cn", target_date: str | None = None) -> None:
        self.market = market
        self.target_date = _normalize_date(target_date) or datetime.now().strftime("%Y%m%d")
        self.snapshot: pd.DataFrame | None = None
        self.snapshot_source = ""
        self.snapshot_fetched_at = ""
        self.history_cache: dict[tuple[Any, ...], pd.DataFrame] = {}
        self.realtime_cache: dict[str, tuple[float, dict[str, Any]]] = {}
        self._lock = threading.RLock()
        self._source_health: dict[str, dict[str, Any]] = {}
        self._timers: dict[str, float] = {}
        self._metrics: dict[str, float] = {}
        self._counters: dict[str, int] = {
            "snapshot_fetches": 0,
            "snapshot_reused": 0,
            "history_hits": 0,
            "history_misses": 0,
            "quote_hits": 0,
            "quote_misses": 0,
            "cache_reused_count": 0,
        }
        self._source_stats: dict[str, dict[str, Any]] = {}

    @staticmethod
    def history_cache_key(
        *,
        market: str,
        stock_code: str,
        start_date: str,
        end_date: str,
        adjustment: str = "qfq",
    ) -> tuple[str, str, str, str, str, str]:
        return (
            str(market or "cn").lower(),
            _normalize_code(stock_code),
            _normalize_date(start_date),
            _normalize_date(end_date),
            str(adjustment or "").lower(),
            "daily",
        )

    def load_snapshot(self, loader: Callable[[], pd.DataFrame]) -> pd.DataFrame:
        """Load the market snapshot once and return the same data version."""
        with self._lock:
            if self.snapshot is not None:
                self._counters["snapshot_reused"] += 1
                self._counters["cache_reused_count"] += 1
                return self.snapshot
            started = time.perf_counter()
            try:
                frame = loader()
                if not isinstance(frame, pd.DataFrame) or frame.empty:
                    raise ValueError("shared snapshot is empty")
                self.snapshot = frame
                self.snapshot_source = str(frame.attrs.get("snapshot_source", ""))
                self.snapshot_fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
                self._counters["snapshot_fetches"] += 1
                logger.info(
                    "Stage1 shared snapshot loaded rows=%s source=%s fetched_at=%s",
                    len(frame),
                    self.snapshot_source or "unknown",
                    self.snapshot_fetched_at,
                )
                return frame
            finally:
                self._metrics["snapshot_fetch_seconds"] = (
                    self._metrics.get("snapshot_fetch_seconds", 0.0)
                    + time.perf_counter() - started
                )

    def get_history(
        self,
        stock_code: str,
        *,
        lookback_days: int,
        source: str,
        loader: Callable[[], pd.DataFrame],
        start_date: str | None = None,
        end_date: str | None = None,
        adjustment: str = "qfq",
    ) -> pd.DataFrame:
        end = _normalize_date(end_date) or self.target_date
        start = _normalize_date(start_date)
        if not start:
            end_dt = datetime.strptime(end, "%Y%m%d").date()
            start = (end_dt - timedelta(days=max(int(lookback_days) * 2, 90))).strftime("%Y%m%d")
        key = self.history_cache_key(
            market=self.market,
            stock_code=stock_code,
            start_date=start,
            end_date=end,
            adjustment=adjustment,
        )
        with self._lock:
            cached = self.history_cache.get(key)
            if cached is not None:
                self._counters["history_hits"] += 1
                self._counters["cache_reused_count"] += 1
                return cached
            self._counters["history_misses"] += 1
            started = time.perf_counter()
            try:
                frame = loader()
                if not isinstance(frame, pd.DataFrame) or frame.empty:
                    raise ValueError(f"history is empty for {stock_code}")
                self.history_cache[key] = frame
                return frame
            finally:
                self._metrics["history_fetch_seconds"] = (
                    self._metrics.get("history_fetch_seconds", 0.0)
                    + time.perf_counter() - started
                )

    def get_realtime_quote(
        self,
        stock_code: str,
        loader: Callable[[], dict[str, Any]],
        *,
        ttl_seconds: float = 30.0,
    ) -> dict[str, Any]:
        code = _normalize_code(stock_code)
        now = time.monotonic()
        with self._lock:
            cached = self.realtime_cache.get(code)
            if cached is not None and now - cached[0] <= max(float(ttl_seconds), 0.0):
                self._counters["quote_hits"] += 1
                self._counters["cache_reused_count"] += 1
                return dict(cached[1])
            self._counters["quote_misses"] += 1
            started = time.perf_counter()
            try:
                payload = loader()
                value = dict(payload) if isinstance(payload, dict) else {}
                self.realtime_cache[code] = (time.monotonic(), value)
                return dict(value)
            finally:
                self._metrics["realtime_quote_seconds"] = (
                    self._metrics.get("realtime_quote_seconds", 0.0)
                    + time.perf_counter() - started
                )

    def record_source_success(self, source: str, *, rows: int | None = None) -> None:
        with self._lock:
            state = self._source_health.setdefault(source, {"failures": 0, "skip_count": 0})
            state["failures"] = 0
            state["successes"] = int(state.get("successes", 0)) + 1
            if rows is not None:
                state["last_rows"] = int(rows)
            self._source_stats.setdefault(source, {}).update({"success": True, "rows": rows})

    def record_source_failure(self, source: str, error: object, *, threshold: int = 3) -> bool:
        """Record a failure and return whether the run-level circuit opened."""
        with self._lock:
            state = self._source_health.setdefault(source, {"failures": 0, "skip_count": 0})
            state["failures"] = int(state.get("failures", 0)) + 1
            state["last_error"] = " ".join(str(error).split())
            opened = state["failures"] >= max(int(threshold), 1) and not state.get("opened")
            if opened:
                state["opened"] = True
                state["opened_at"] = time.time()
            self._source_stats.setdefault(source, {}).update({"success": False, "error": state["last_error"]})
            return bool(opened)

    def source_disabled_reason(self, source: str) -> str | None:
        with self._lock:
            state = self._source_health.get(source)
            if not state or not state.get("opened"):
                return None
            state["skip_count"] = int(state.get("skip_count", 0)) + 1
            return f"run-level circuit open; skip_count={state['skip_count']}"

    @contextmanager
    def timer(self, name: str) -> Iterator[None]:
        started = time.perf_counter()
        try:
            yield
        finally:
            self._metrics[name] = self._metrics.get(name, 0.0) + time.perf_counter() - started

    def metrics(self) -> dict[str, Any]:
        with self._lock:
            source_health = {key: dict(value) for key, value in self._source_health.items()}
            return {
                **{key: round(value, 6) for key, value in self._metrics.items()},
                "cache_stats": {
                    **self._counters,
                    "history_entries": len(self.history_cache),
                    "realtime_entries": len(self.realtime_cache),
                },
                "data_source_stats": {
                    "snapshot": {
                        "source": self.snapshot_source,
                        "rows": int(len(self.snapshot)) if self.snapshot is not None else 0,
                        "fetched_at": self.snapshot_fetched_at,
                        "fetches": self._counters["snapshot_fetches"],
                        "reused": self._counters["snapshot_reused"],
                    },
                    "history": source_health,
                    "sources": {key: dict(value) for key, value in self._source_stats.items()},
                },
            }


def _normalize_code(value: object) -> str:
    text = str(value or "").strip().upper()
    digits = "".join(char for char in text if char.isdigit())
    return digits.zfill(6)[-6:] if digits else text


def _normalize_date(value: object) -> str:
    text = str(value or "").strip().replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""
