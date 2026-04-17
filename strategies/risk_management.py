"""Risk management strategy skeleton."""

from __future__ import annotations

from typing import Dict


class RiskManagementStrategy:
    """Applies portfolio and exposure controls before any action is taken."""

    def build_decision(self, context: object) -> Dict:
        """Placeholder decision gate returning a hold action."""
        return {
            "action": "hold",
            "reason": "Risk rules are placeholders; execution is disabled in scaffold.",
        }
