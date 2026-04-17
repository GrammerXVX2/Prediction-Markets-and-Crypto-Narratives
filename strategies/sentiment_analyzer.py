"""Primitive sentiment analyzer prototype."""

from __future__ import annotations

from typing import Dict, List


class SentimentAnalyzer:
    """Very lightweight sentiment analyzer for text snippets."""

    POSITIVE_KEYWORDS = {"bullish", "growth", "surge", "rally", "adoption", "breakout"}
    NEGATIVE_KEYWORDS = {"bearish", "drop", "crash", "decline", "risk", "selloff"}

    def analyze_text(self, text: str) -> Dict:
        """Placeholder sentiment analysis for one text input."""
        # TODO: Replace with a real NLP/LLM model and calibrated confidence scoring.
        lowered_text = text.lower()
        positive_hits = sum(1 for keyword in self.POSITIVE_KEYWORDS if keyword in lowered_text)
        negative_hits = sum(1 for keyword in self.NEGATIVE_KEYWORDS if keyword in lowered_text)

        if positive_hits > negative_hits:
            return {"label": "positive", "score": 0.7}
        if negative_hits > positive_hits:
            return {"label": "negative", "score": 0.7}
        return {"label": "neutral", "score": 0.5}

    def analyze_batch(self, texts: List[str]) -> List[Dict]:
        """Analyze a batch of texts."""
        return [self.analyze_text(text) for text in texts]
