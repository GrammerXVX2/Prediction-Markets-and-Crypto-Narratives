# Prediction Markets and Crypto Narratives Agent Scaffold

This repository contains a **starter architecture** for an AI agent that analyzes:

- Prediction Markets (e.g., Polymarket)
- Crypto narrative signals from social, news, and on-chain sources

The current version is intentionally a scaffold: interfaces and placeholder classes are in place, while business logic and API integrations are left for iterative implementation.

## Project structure

```text
.
├── core/
│   ├── __init__.py
│   └── agent.py
├── data/
│   ├── __init__.py
│   ├── base.py
│   ├── twitter_adapter.py
│   ├── reddit_adapter.py
│   ├── news_adapter.py
│   ├── onchain_dex_adapter.py
│   └── polymarket_adapter.py
├── strategies/
│   ├── __init__.py
│   ├── market_scoring.py
│   ├── sentiment.py
│   ├── edge_calc.py
│   └── risk_management.py
├── tools/
│   ├── __init__.py
│   └── logging_utils.py
├── main.py
├── requirements.txt
└── README.md
```

## Architecture layers

- **core/**: Agent orchestration and workflow coordination.
- **data/**: External data adapters (Twitter, Reddit, News, On-chain/DEX, Polymarket).
- **strategies/**: Analytical and decision strategies (market scoring, sentiment, edge calculation, risk management).
- **tools/**: Shared utility functions.
- **main.py**: Example entrypoint with a full placeholder workflow.

## Example workflow (stub)

The entrypoint (`main.py`) demonstrates one end-to-end path:

1. Collect new information from all data adapters.
2. Analyze inputs using strategy components.
3. Make a placeholder decision through risk management.

No trading or market actions are executed in this scaffold.

## Run

```bash
python main.py
```

## Future development directions

1. Implement concrete API clients in `data/` adapters.
2. Add feature engineering and model pipelines for sentiment and probability estimation.
3. Introduce backtesting and paper-trading modules.
4. Add persistent storage, metrics, and monitoring.
5. Expand risk controls and execution safeguards before enabling live actions.

## Base review of current scaffold

### What is already in place
- Clear modular structure by responsibility (`core/`, `data/`, `strategies/`, `tools/`).
- End-to-end placeholder workflow in `main.py` (collect → analyze → decide).
- Interface contract for data adapters (`DataAdapter`) and strategy stubs.
- Execution safety by default: only `hold` decision, no trading actions.

### Current gaps
- No real data integrations yet (all adapters return placeholders).
- No probability calibration/backtesting layer.
- No portfolio state persistence and no observability dashboard.
- No automated test suite yet.

## First integration: Polymarket + news adapter skeleton

This milestone now includes a first integration scaffold with explicit method contracts:

- `data/polymarket_adapter.py`
  - `fetch_event_quotes()`: quote snapshot prototype for market events.
  - `fetch_betting_history(event_id, limit)`: historical bets/trades prototype.
- `data/news_adapter.py`
  - `fetch_latest_posts_by_keywords(keywords, limit)`: keyword-based news extraction stub.
- `core/agent.py`
  - `aggregate_quotes_and_news(event_quotes, news_posts)`: prototype payload builder for decision input (no business logic).

These components are intentionally read-only stubs and keep the decision flow in safe `hold` mode.

## Candidate libraries and external APIs

### Core Python and validation
- **pydantic**: strict schemas for normalized market/social events and config validation.
- **httpx**: async/sync HTTP client for adapter integrations.
- **tenacity**: retries/backoff for flaky upstream APIs.

### Prediction market data
- **Polymarket API / Gamma API**: active markets, odds/probabilities, liquidity and metadata.
- **py-clob-client** (optional): typed client for Polymarket CLOB endpoints.

### Social/news narrative signal inputs
- **X (Twitter) API v2**: mentions, engagement, recency for narrative velocity features.
- **Reddit API (PRAW)**: subreddit/topic momentum and discussion intensity.
- **NewsAPI / GDELT / RSS feeds**: headline flow for event context and catalyst detection.

### Sentiment and NLP
- **transformers**: baseline sentiment/classification models.
- **vaderSentiment**: fast lexicon-based sentiment for lightweight baseline.
- **openai** (optional): LLM-based event summarization and probability rationale generation.

### Storage, analytics, and operations
- **pandas**: feature engineering and offline analysis.
- **duckdb**: local analytical storage for backtesting and quick experiments.
- **loguru** or stdlib `logging`: structured logs and traceability for agent decisions.
