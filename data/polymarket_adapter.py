"""Polymarket data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class PolymarketAdapter(DataAdapter):
    """Collects and normalizes market prices and metadata from Polymarket."""

    def fetch_event_quotes(self) -> List[Dict]:
        """Prototype for loading current market quotes from Polymarket."""
        return [
            {
                "source": "polymarket",
                "event_id": "stub-event",
                "question": "Will BTC close above $100k this year?",
                "yes_price": 0.0,
                "no_price": 1.0,
                "volume_usd": 0.0,
            }
        ]

    def fetch_betting_history(self, event_id: str, limit: int = 50) -> List[Dict]:
        """Prototype for loading historical trades for one market event."""
        _ = (event_id, limit)
        return []

    def fetch_latest(self) -> List[Dict]:
        """DataAdapter compatibility hook mapped to quote retrieval."""
        return self.fetch_event_quotes()
