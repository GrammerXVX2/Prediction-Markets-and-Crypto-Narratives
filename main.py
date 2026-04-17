"""Entry point for the Prediction Markets and Crypto Narratives agent scaffold."""

from core.agent import PredictionNarrativeAgent
from data.news_adapter import NewsAdapter
from data.onchain_dex_adapter import OnChainDexAdapter
from data.polymarket_adapter import PolymarketAdapter
from data.reddit_adapter import RedditAdapter
from data.twitter_adapter import TwitterAdapter
from strategies.edge_calc import EdgeCalculator
from strategies.market_scoring import MarketScoringStrategy
from strategies.risk_management import RiskManagementStrategy
from strategies.sentiment import SentimentStrategy
from tools.logging_utils import log_event


def build_agent() -> PredictionNarrativeAgent:
    """Construct a scaffolded agent with placeholder components."""
    adapters = [
        TwitterAdapter(),
        RedditAdapter(),
        NewsAdapter(),
        OnChainDexAdapter(),
        PolymarketAdapter(),
    ]
    return PredictionNarrativeAgent(
        data_adapters=adapters,
        market_scoring=MarketScoringStrategy(),
        sentiment=SentimentStrategy(),
        edge_calculator=EdgeCalculator(),
        risk_manager=RiskManagementStrategy(),
    )


def run_workflow() -> None:
    """Example workflow: collect new info -> analyze -> make decision."""
    agent = build_agent()

    updates = agent.collect_information()
    log_event("data_collected", {"items": len(updates)})

    context = agent.analyze(updates)
    log_event("analysis_complete", context)

    decision = agent.decide(context)
    log_event("decision_made", decision)


if __name__ == "__main__":
    run_workflow()
