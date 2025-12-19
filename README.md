# Statistical Arbitrage Engine (Cointegration + Backtesting)

A research-to-production statistical arbitrage system that identifies cointegrated asset pairs or baskets, constructs stationary spreads, generates market-neutral trading signals, and evaluates performance using realistic backtesting and walk-forward validation.

---

## 📌 Overview

This project implements a **cointegration-based statistical arbitrage engine** designed to mirror how professional quant teams research, validate, and evaluate mean-reversion strategies. The system emphasizes **statistical rigor**, **realistic execution assumptions**, and **reproducibility**, making it suitable for both academic research and portfolio demonstration.

At a high level, the engine:

* Searches a universe of assets for cointegrated relationships
* Estimates hedge ratios to construct stationary spreads
* Generates z-score–based trading signals
* Backtests strategies under realistic market frictions
* Evaluates robustness via walk-forward validation

---

## 🧠 Core Concepts

* **Cointegration**: Identifies asset relationships where a linear combination of prices is stationary, enabling mean-reversion strategies.
* **Market Neutrality**: Long/short positioning using hedge ratios to minimize directional market exposure.
* **Stationary Spread**: The tradable signal derived from cointegrated assets.
* **Z-Score Normalization**: Standardizes spread deviations to enable consistent entry/exit rules.
* **Walk-Forward Validation**: Prevents overfitting by repeatedly retraining and testing across rolling time windows.

---

## 🧩 Features

### Pair & Basket Selection

* Universe-wide search for cointegrated pairs or baskets
* Support for multiple cointegration tests

### Hedge Ratio Estimation

* Ordinary Least Squares (OLS)
* Engle–Granger two-step method
* Johansen test for multivariate cointegration

### Signal Generation

* Stationary spread construction
* Z-score computation
* Rule-based trade entry, exit, and stop-loss logic

### Risk Management

* Volatility-aware position sizing
* Leverage and exposure constraints
* Capital allocation controls

### Backtesting Engine

* Transaction costs and commissions
* Slippage and execution delay modeling
* Borrow and shorting costs
* No look-ahead or survivorship bias

### Evaluation & Reporting

* Walk-forward (rolling window) validation
* Performance metrics (Sharpe, drawdown, win rate, turnover)
* Automated plots, tear sheets, and trade logs

---

## 🏗️ Project Structure

```
stat-arb-engine/
│
├── data/           # Raw and processed price data
├── research/       # Cointegration tests and exploratory analysis
├── signals/        # Spread construction and signal generation
├── strategies/     # Trading rules and risk management logic
├── backtest/       # Execution simulator and PnL engine
├── evaluation/     # Metrics, validation, and reporting
├── configs/        # Strategy and experiment configuration files
├── reports/        # Plots, tear sheets, logs
└── main.py         # End-to-end pipeline entry point
```

---

## 🚀 Workflow

1. **Select Universe** – Define the asset universe and data frequency
2. **Find Cointegration** – Test pairs or baskets for long-run relationships
3. **Estimate Hedge Ratios** – Fit cointegration vectors
4. **Construct Spread** – Build stationary spreads and compute z-scores
5. **Generate Trades** – Apply rule-based entry/exit logic
6. **Backtest** – Simulate execution with realistic costs
7. **Validate** – Perform walk-forward evaluation
8. **Report** – Export performance metrics and visualizations

---

## 📊 Example Strategy Logic

* Enter trade when |z-score| > entry threshold
* Long undervalued leg, short overvalued leg
* Exit when z-score reverts to mean
* Stop-loss if z-score exceeds risk threshold

---

## 🔬 Motivation

Many stat arb strategies fail not because the math is wrong, but because:

* Relationships are not truly stationary
* Costs and slippage are ignored
* Models are overfit to historical data

This project is built to explicitly address those issues and reflect **real-world quantitative trading constraints**.

---

## 🛠️ Future Extensions

* Live data ingestion
* Paper trading integration
* Portfolio-level optimization
* Regime detection and adaptive parameters
* Multi-frequency strategies

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. It does not constitute financial advice and is not intended for live trading without extensive additional risk controls and validation.

---

## 👤 Author

Nathan Chin-Lue
