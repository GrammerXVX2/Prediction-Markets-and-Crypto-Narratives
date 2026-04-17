"""Edge calculation strategy skeleton."""

from __future__ import annotations

from typing import Dict


class EdgeCalculator:
    """Estimates expected edge between agent view and market prices."""

    def calculate(self, market_scores: Dict, sentiment_scores: Dict) -> Dict:
        """Placeholder edge calculation entry point."""
        return {"edge": 0.0, "opportunity": False}
