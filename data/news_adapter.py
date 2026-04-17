"""News data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class NewsAdapter(DataAdapter):
    """Collects and normalizes headlines from crypto and macro news feeds."""

    def fetch_latest_posts_by_keywords(self, keywords: List[str], limit: int = 20) -> List[Dict]:
        """Prototype for retrieving recent news posts by keyword list."""
        _ = (keywords, limit)
        return []

    def fetch_latest(self) -> List[Dict]:
        """DataAdapter compatibility hook for generic collection flow."""
        return self.fetch_latest_posts_by_keywords([])
