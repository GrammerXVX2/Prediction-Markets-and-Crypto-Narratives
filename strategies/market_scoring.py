"""Market scoring strategy skeleton."""

from __future__ import annotations

from typing import Dict, List


class MarketScoringStrategy:
    """Builds market-level confidence scores from normalized events."""

    def score(self, updates: List[Dict]) -> Dict:
        """Placeholder market scoring entry point."""
        return {"score": 0.0, "details": "not implemented"}
