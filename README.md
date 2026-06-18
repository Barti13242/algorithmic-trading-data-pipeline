# Autonomous Algorithmic Trading Data Pipeline

An automated data engineering pipeline built in Python that fetches market data from Wall Street, executes historical backtesting (Grid Search) to optimize trading parameters, and generates actionable Business Intelligence reports.

---

## 🚀 Key Features

* **Automated Data Ingestion:** Connects directly to the Yahoo Finance API (`yfinance`) to fetch live and historical market data.
* **Hyperparameter Optimization (Grid Search):** Evaluates multiple Simple Moving Average (SMA) windows (ranging from 5 to 30 days) on historical data to mathematically select the most profitable strategy.
* **Vectorized Backtesting:** Leverages high-performance `Pandas` techniques (`.shift()`, `.pct_change()`, `.cumprod()`) for efficient historical simulation, completely avoiding slow Python loops.
* **Automated File I/O:** Outputs a structured, clean Business Intelligence report directly to the local storage, enabling decoupled downstream data consumption.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Data Manipulation & Analysis:** Pandas, NumPy
* **API Integration:** yfinance
* **Development Methodology:** Clean Code, Vectorized Computation, Automated File I/O, ETL Architecture.

---

## 📊 Pipeline Architecture (ETL Workflow)

The system is architected around a standard **ETL (Extract, Transform, Load)** data pipeline pattern:

### 1. Extract
The pipeline programmatically connects to financial markets and extracts 1 year of daily historical closing prices for a configurable portfolio of high-volume assets (e.g., `MSFT`, `TSLA`, `GOOGL`, `META`).

### 2. Transform
* Computes daily log/percentage returns for each asset.
* Generates shifting historical arrays to prevent "look-ahead bias" (data leakage).
* Runs an automated optimization engine that evaluates 6 different mathematical models per asset to discover the historical sweet spot for risk-adjusted returns.
* Evaluates the final day's position to trigger operational `BUY` or `HOLD` trading signals.

### 3. Load
The refined, high-value data is structured into an analytical report and safely loaded into a permanent flat-file system (`finalny_raport_bota.txt`), serving as a production-ready data source for external dashboard tools or automated trading execution scripts.

---

## 📈 Sample Output Report

When executed, the pipeline automatically writes the following clean data matrix to the disk:

```text
=== RESTRUKTURYZOWANY RAPORT ANALITYCZNY BI ===
Wygenerowano automatycznie przez: Python Data Pipeline

[MSFT] Najlepsze okno: SMA 15 (Zysk hist: 32.10%). Decyzja na dziś: KUPUJ! 📈
[TSLA] Najlepsze okno: SMA 10 (Zysk hist: 14.50%). Decyzja na dziś: CZEKAJ / SPRZEDAJ 📉
[GOOGL] Najlepsze okno: SMA 25 (Zysk hist: 22.40%). Decyzja na dziś: KUPUJ! 📈
[META] Najlepsze okno: SMA 5 (Zysk hist: 41.20%). Decyzja na dziś: KUPUJ! 📈
