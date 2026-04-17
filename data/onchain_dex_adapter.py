"""On-chain and DEX data adapter skeleton."""

from __future__ import annotations

from typing import Dict, List

from data.base import DataAdapter


class OnChainDexAdapter(DataAdapter):
    """Collects and normalizes wallet flows, liquidity, and trading activity."""

    def fetch_latest(self) -> List[Dict]:
        """Placeholder implementation for future on-chain indexer integration."""
        return []
