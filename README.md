# AI Hedge Fund Project

> **Status**: 🚀 Initialization Complete
> **Architecture**: Multi-Agent Quantitative Trading System
> **Stack**: Python, Pandas, Scikit-Learn, PyTorch (Optional)

## Project Goal
Build an autonomous AI-driven hedge fund that uses multiple specialized agents to analyze markets, manage risk, and execute trades.

## System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                   Alpha Generator Agent                    │
│  - Market Data Ingestion                                   │
│  - Factor Analysis (Momentum, Value, Volatility)           │
│  - Signal Generation                                       │
└───────────────────────────┬────────────────────────────────┘
                            │ Signals
┌───────────────────────────▼────────────────────────────────┐
│                   Risk Management Agent                    │
│  - Portfolio Optimization (Markowitz, Black-Litterman)     │
│  - Drawdown Control & Stop-Loss                            │
│  - Position Sizing (Kelly Criterion)                       │
└───────────────────────────┬────────────────────────────────┘
                            │ Allocations
┌───────────────────────────▼────────────────────────────────┐
│                   Execution Agent                          │
│  - Broker API Integration                                  │
│  - Order Routing (VWAP/TWAP)                               │
│  - Slippage & Cost Analysis                                │
└────────────────────────────────────────────────────────────┘
```

## Directory Structure

- `data/`: Raw market data, factors, and cached results
- `src/`: Core logic (agents, strategies, utils)
- `tests/`: Unit and integration tests
- `docs/`: Architecture diagrams, research notes
- `scripts/`: Data pipelines, backtesting runners
- `output/`: Reports, logs, performance metrics

## Getting Started

1.  **Environment**: Python 3.10+
2.  **Setup**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Data**: Run `python scripts/download_data.py` to fetch historical data.

## Agent Workflow
Each agent operates independently but shares state via a centralized `StateManager`.
- Agents communicate via structured JSON messages.
- Backtesting uses historical replay.
- Live mode connects to broker API.
