"""Focused tests for sentiment prototype integration."""

from __future__ import annotations

import unittest

from data.news_adapter import NewsAdapter
from strategies.sentiment_analyzer import SentimentAnalyzer


class SentimentPrototypeTests(unittest.TestCase):
    def test_analyze_text_returns_positive_and_negative_labels(self) -> None:
        analyzer = SentimentAnalyzer()
        self.assertEqual(analyzer.analyze_text("Strong bullish rally and adoption")["label"], "positive")
        self.assertEqual(analyzer.analyze_text("Market crash and decline risk")["label"], "negative")

    def test_news_adapter_adds_sentiment_labels(self) -> None:
        analyzer = SentimentAnalyzer()
        adapter = NewsAdapter()
        posts = [{"title": "Bitcoin breakout", "summary": "Institutional growth continues"}]

        labeled_posts = adapter.with_sentiment_labels(posts, sentiment_analyzer=analyzer)

        self.assertEqual(len(labeled_posts), 1)
        self.assertIn("sentiment", labeled_posts[0])
        self.assertEqual(labeled_posts[0]["sentiment"]["label"], "positive")


if __name__ == "__main__":
    unittest.main()
