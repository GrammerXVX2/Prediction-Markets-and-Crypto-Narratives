"""Core AI agent orchestration primitives."""

from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Dict, List

from data.base import DataAdapter
from strategies.edge_calc import EdgeCalculator
from strategies.market_scoring import MarketScoringStrategy
from strategies.risk_management import RiskManagementStrategy
from strategies.sentiment import SentimentStrategy


@dataclass
class AgentContext:
    """Container with normalized artifacts produced during one workflow run."""

    raw_updates: List[Dict]
    market_scores: Dict
    sentiment_scores: Dict
    edge_assessment: Dict


class PredictionNarrativeAgent:
    """Coordinates data collection, analysis and decision-making steps."""

    def __init__(
        self,
        data_adapters: List[DataAdapter],
        market_scoring: MarketScoringStrategy,
        sentiment: SentimentStrategy,
        edge_calculator: EdgeCalculator,
        risk_manager: RiskManagementStrategy,
    ) -> None:
        self.data_adapters = data_adapters
        self.market_scoring = market_scoring
        self.sentiment = sentiment
        self.edge_calculator = edge_calculator
        self.risk_manager = risk_manager

    def collect_information(self) -> List[Dict]:
        """Collect fresh data from all configured external adapters."""
        updates: List[Dict] = []
        for adapter in self.data_adapters:
            updates.extend(adapter.fetch_latest())
        return updates

    def analyze(self, updates: List[Dict]) -> AgentContext:
        """Run analysis strategies over newly collected updates."""
        market_scores = self.market_scoring.score(updates)
        sentiment_scores = self.sentiment.evaluate(updates)
        edge_assessment = self.edge_calculator.calculate(market_scores, sentiment_scores)
        return AgentContext(
            raw_updates=updates,
            market_scores=market_scores,
            sentiment_scores=sentiment_scores,
            edge_assessment=edge_assessment,
        )

    def decide(self, context: AgentContext) -> Dict:
        """Return a placeholder action decision using risk controls."""
        return self.risk_manager.build_decision(context)


def aggregate_quotes_and_news(event_quotes: List[Dict], news_posts: List[Dict]) -> Dict:
    """Build a decision input payload from market quotes and narrative signals."""
    return {
        "event_quotes": event_quotes,
        "news_posts": news_posts,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "prototype_no_business_logic",
    }
