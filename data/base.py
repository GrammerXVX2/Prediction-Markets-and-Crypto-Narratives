"""Shared interfaces for data adapters."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class DataAdapter(ABC):
    """Contract for all source adapters used by the agent."""

    @abstractmethod
    def fetch_latest(self) -> List[Dict]:
        """Fetch and normalize the latest events from the upstream source."""
        raise NotImplementedError
