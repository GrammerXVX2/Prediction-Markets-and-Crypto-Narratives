"""Reddit data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class RedditAdapter(DataAdapter):
    """Collects and normalizes Reddit posts and comments."""

    def fetch_latest(self) -> List[Dict]:
        """Placeholder implementation for future Reddit API integration."""
        return []
