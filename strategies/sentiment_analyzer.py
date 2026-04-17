"""Primitive sentiment analyzer prototype."""

from __future__ import annotations

import re
from typing import List, TypedDict


class SentimentResult(TypedDict):
    """Structured output for sentiment analysis results."""

    label: str
    score: float


class SentimentAnalyzer:
    """Very lightweight sentiment analyzer for text snippets."""

    POSITIVE_KEYWORDS = ("bullish", "growth", "surge", "rally", "adoption", "breakout")
    NEGATIVE_KEYWORDS = ("bearish", "drop", "crash", "decline", "risk", "selloff")
    POSITIVE_PATTERNS = [re.compile(rf"\b{re.escape(keyword)}\b") for keyword in POSITIVE_KEYWORDS]
    NEGATIVE_PATTERNS = [re.compile(rf"\b{re.escape(keyword)}\b") for keyword in NEGATIVE_KEYWORDS]
    NEUTRAL_SCORE = 0.5

    @staticmethod
    def _count_keyword_hits(text: str, patterns: List[re.Pattern[str]]) -> int:
        """Count full-word keyword matches in input text."""
        return sum(1 for pattern in patterns if pattern.search(text))

    def analyze_text(self, text: str) -> SentimentResult:
        """Placeholder sentiment analysis for one text input.

        Score is centered at 0.5 and shifted by keyword hit balance in 0.1 steps,
        then clamped to [0.1, 0.9] to keep prototype outputs bounded.
        """
        # TODO: Replace with a real NLP/LLM model and calibrated confidence scoring.
        lowered_text = text.lower()
        positive_hits = self._count_keyword_hits(lowered_text, self.POSITIVE_PATTERNS)
        negative_hits = self._count_keyword_hits(lowered_text, self.NEGATIVE_PATTERNS)
        score = max(0.1, min(0.9, self.NEUTRAL_SCORE + 0.1 * (positive_hits - negative_hits)))

        if positive_hits > negative_hits:
            return {"label": "positive", "score": score}
        if negative_hits > positive_hits:
            return {"label": "negative", "score": score}
        return {"label": "neutral", "score": self.NEUTRAL_SCORE}

    def analyze_batch(self, texts: List[str]) -> List[SentimentResult]:
        """Analyze a batch of texts."""
        return [self.analyze_text(text) for text in texts]
