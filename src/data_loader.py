from pathlib import Path

import pandas as pd


def load_sales_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path, parse_dates=["order_date"])

    required_cols = {
        "order_id",
        "order_date",
        "customer_id",
        "region",
        "customer_segment",
        "product_category",
        "unit_price",
        "quantity",
        "discount_pct",
        "gross_revenue",
        "net_revenue",
    }

    missing = required_cols.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
