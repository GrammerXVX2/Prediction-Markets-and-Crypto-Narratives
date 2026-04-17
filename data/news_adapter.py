"""News data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter
from strategies.sentiment_analyzer import SentimentAnalyzer


class NewsAdapter(DataAdapter):
    """Collects and normalizes headlines from crypto and macro news feeds."""

    def fetch_latest_posts_by_keywords(self, keywords: List[str], limit: int = 20) -> List[Dict]:
        """Prototype for retrieving recent news posts by keyword list."""
        if not keywords:
            return []

        prototype_posts = [
            {
                "source": "news_stub",
                "title": "Bitcoin rally continues as institutional adoption grows",
                "summary": "Market participants report stronger demand after ETF inflows.",
            },
            {
                "source": "news_stub",
                "title": "Ethereum faces short-term risk amid macro uncertainty",
                "summary": "Analysts mention volatility and possible decline in risk assets.",
            },
        ]

        normalized_keywords = {keyword.lower() for keyword in keywords}
        filtered_posts = [
            post
            for post in prototype_posts
            if any(keyword in f"{post['title']} {post['summary']}".lower() for keyword in normalized_keywords)
        ]
        return filtered_posts[:limit]

    def attach_sentiment_labels(self, posts: List[Dict], analyzer: SentimentAnalyzer) -> List[Dict]:
        """Attach sentiment labels to each post using a primitive analyzer."""
        labeled_posts: List[Dict] = []
        for post in posts:
            text = f"{post.get('title', '')} {post.get('summary', '')}".strip()
            sentiment = analyzer.analyze_text(text=text)
            labeled_posts.append({**post, "sentiment": sentiment})
        return labeled_posts

    def fetch_latest(self) -> List[Dict]:
        """DataAdapter compatibility hook for generic collection flow."""
        return self.fetch_latest_posts_by_keywords([])
