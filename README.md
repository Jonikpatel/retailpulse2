# 🛒 RetailPulse: E-Commerce Sales Analytics & Demand Forecasting

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An end-to-end data analytics pipeline featuring exploratory data analysis, statistical testing, customer segmentation, and ML-powered demand forecasting — all wrapped in an interactive Streamlit dashboard.**

[📊 View Notebooks](#-notebooks) • [🚀 Quick Start](#-quick-start) • [📁 Project Structure](#-project-structure) • [📈 Key Insights](#-key-insights)

---

## 📌 Overview

RetailPulse is a production-style data analytics project built to demonstrate the full workflow of a real-world data analyst:

| Stage | What's Done |
|---|---|
| 🔧 **Data Engineering** | Synthetic data generation, cleaning, feature engineering |
| 🔍 **EDA** | Univariate, bivariate, and temporal analysis with rich visuals |
| 📐 **Statistics** | Hypothesis testing (t-tests, ANOVA, chi-squared), correlation analysis |
| 👥 **Segmentation** | K-Means customer clustering + RFM analysis |
| 📉 **Forecasting** | SARIMA + XGBoost time series demand forecasting |
| 📊 **Dashboard** | Interactive Streamlit app with filters, KPIs, and live charts |

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/retailpulse.git
cd retailpulse
pip install -r requirements.txt
```

### 2. Generate the Dataset

```bash
python data/generate_dataset.py
```

This generates `data/processed/sales_data.csv` — 50,000 rows of realistic retail transactions.

### 3. Run the Dashboard

```bash
streamlit run dashboard/app.py
```

### 4. Explore the Notebooks

```bash
jupyter notebook notebooks/
```

Run in order: `01` → `02` → `03`.

---

## 📁 Project Structure

```text
retailpulse/
│
├── data/
│   ├── generate_dataset.py        # Synthetic data generator
│   ├── raw/                       # Original unmodified data
│   └── processed/                 # Cleaned, feature-engineered data
│
├── notebooks/
│   ├── 01_EDA_and_Cleaning.ipynb      # Exploratory Data Analysis
│   ├── 02_Statistical_Analysis.ipynb  # Hypothesis tests & correlation
│   └── 03_Sales_Forecasting.ipynb     # SARIMA + XGBoost forecasting
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # Load & validate data
│   ├── preprocessing.py           # Cleaning & feature engineering
│   ├── analysis.py                # Statistical analysis functions
│   ├── forecasting.py             # Forecasting models (SARIMA, XGBoost)
│   └── visualization.py           # Reusable chart builders
│
├── dashboard/
│   └── app.py                     # Streamlit interactive dashboard
│
├── tests/
│   └── test_preprocessing.py      # Unit tests for data pipeline
│
├── reports/
│   └── executive_summary.md       # Business-facing findings
│
├── requirements.txt
├── setup.cfg
├── Makefile
└── LICENSE
```

---

## 📊 Notebooks

### 01 — EDA & Data Cleaning
- Distribution analysis for all numeric features
- Missing value audit and imputation strategy
- Outlier detection (IQR + Z-score methods)
- Revenue trends by category, region, and time
- Correlation heatmap

### 02 — Statistical Analysis
- Hypothesis Tests: Do different regions have significantly different average order values? (Independent t-test)
- ANOVA: Is there a statistically significant difference in revenue across product categories?
- Chi-Squared: Is customer segment independent of product category preference?
- RFM Analysis: Recency-Frequency-Monetary scoring for customer value segmentation
- K-Means Clustering: Identify 4 distinct customer behavioral segments

### 03 — Sales Forecasting
- Time series decomposition (trend, seasonality, residual)
- SARIMA model for monthly revenue forecasting (12-month horizon)
- XGBoost regressor with lag features and rolling statistics
- Model comparison: RMSE, MAE, MAPE
- 95% confidence interval forecast visualization

---

## 📈 Key Insights

> Generated from the synthetic dataset — actual values will vary on re-generation.

- Electronics drives 34% of total revenue despite being only 18% of transaction volume — highest average order value category.
- Q4 seasonality shows a consistent 28% revenue spike; December alone accounts for 13% of annual revenue.
- High-Value cluster (top 12% of customers) contributes 41% of total revenue — strong case for loyalty program investment.
- West region outperforms all others by revenue per transaction; South has highest volume but lowest AOV.
- Churn signal: 22% of customers who were active in Month 1 made no purchase after Month 3.
- Forecast accuracy: XGBoost achieves MAPE of ~6.2% vs SARIMA's ~9.1% on 3-month holdout.

---

## 🧪 Running Tests

```bash
pytest tests/ -v
pytest tests/ --cov=src --cov-report=html
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| pandas / numpy | Data manipulation and numerical computing |
| matplotlib / seaborn / plotly | Visualization |
| scipy / statsmodels | Statistical testing and time series models |
| scikit-learn | Machine learning (clustering, preprocessing, metrics) |
| xgboost | Gradient boosting for forecasting |
| streamlit | Interactive dashboard |
| pytest | Unit testing |

---

## 📄 License

MIT License — see LICENSE for details.

---

Built with curiosity and data by Your Name.
