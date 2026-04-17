"""Polymarket data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class PolymarketAdapter(DataAdapter):
    """Collects and normalizes market prices and metadata from Polymarket."""

    def fetch_latest(self) -> List[Dict]:
        """Placeholder implementation for future Polymarket API integration."""
        return []
