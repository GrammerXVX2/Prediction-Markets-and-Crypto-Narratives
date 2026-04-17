"""Entry point for the Prediction Markets and Crypto Narratives agent scaffold."""

from core.agent import PredictionNarrativeAgent, aggregate_quotes_and_news
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

    event_quotes = []
    news_posts = []
    for adapter in agent.data_adapters:
        if isinstance(adapter, PolymarketAdapter):
            event_quotes.extend(adapter.fetch_event_quotes())
        if isinstance(adapter, NewsAdapter):
            news_posts.extend(
                adapter.fetch_latest_posts_by_keywords(
                    keywords=["bitcoin", "ethereum"],
                    limit=10,
                )
            )

    decision_payload = aggregate_quotes_and_news(event_quotes=event_quotes, news_posts=news_posts)
    log_event("first_integration_payload_ready", decision_payload)

    decision = agent.decide(context)
    log_event("decision_made", decision)


if __name__ == "__main__":
    run_workflow()
