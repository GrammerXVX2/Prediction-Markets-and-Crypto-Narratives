"""News data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class NewsAdapter(DataAdapter):
    """Collects and normalizes headlines from crypto and macro news feeds."""

    def fetch_latest(self) -> List[Dict]:
        """Placeholder implementation for future RSS/news provider integration."""
        return []
