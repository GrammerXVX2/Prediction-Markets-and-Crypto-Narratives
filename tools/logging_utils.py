"""Logging helper utilities."""

from __future__ import annotations

from typing import Any


def log_event(event_name: str, payload: Any) -> None:
    """Simple stdout logger used by the architecture scaffold."""
    print(f"[event] {event_name}: {payload}")
