# TODO / Roadmap

## Stage 0 — Scaffold hardening (current)
- [x] Add `.gitignore` and remove generated artifacts from version control.
- [ ] Introduce project config (`.env.example`, runtime settings schema).
- [ ] Define normalized internal event model for adapters.

**Milestone:** deterministic local run with clean repository state and stable data contracts.

## Stage 1 — First priority integration: Polymarket (read-only)
- [ ] Implement Polymarket data client in `data/polymarket_adapter.py`.
- [ ] Normalize market payloads (question, outcomes, implied probability, liquidity, timestamp).
- [ ] Add retry, timeout, and data freshness checks.
- [ ] Add adapter-level tests for payload normalization.

**Milestone:** agent ingests real Polymarket markets and logs normalized updates.

## Stage 2 — Baseline scoring and risk gate
- [ ] Implement basic market scoring strategy from implied probabilities/liquidity.
- [ ] Add conservative risk policy (max exposure, cooldown, confidence threshold).
- [ ] Keep execution disabled; decision remains advisory (`hold`/`watchlist`).
- [ ] Add deterministic fixtures for scoring and risk unit tests.

**Milestone:** reproducible advisory decisions based on real market data.

## Stage 3 — Narrative enrichment (Twitter/Reddit/News)
- [ ] Integrate first social source (X or Reddit) with minimal rate-limit-safe polling.
- [ ] Implement baseline sentiment aggregation and confidence score.
- [ ] Join narrative features with Polymarket events by entity/topic matching.
- [ ] Add feature logging for later backtesting.

**Milestone:** combined market + narrative context per event.

## Stage 4 — Backtesting and paper trading
- [ ] Store historical snapshots (DuckDB/Parquet).
- [ ] Implement simple backtest loop for threshold strategies.
- [ ] Track metrics: hit rate, max drawdown, Sharpe-like proxy, turnover.
- [ ] Add paper-trading mode and reporting.

**Milestone:** strategy quality measured before any live execution.

## Nearest tasks (next 1–2 iterations)
1. Implement Polymarket adapter (read-only) + normalization schema.
2. Add adapter tests and fixtures.
3. Add conservative risk gating for advisory decisions.
4. Prepare one evaluation notebook/script for quick quality checks.

## Next move summary
The immediate next move is to deliver **Stage 1 (Polymarket read-only integration)**, because it unlocks real input data for all downstream sentiment, edge, and risk logic while keeping operational risk minimal.
