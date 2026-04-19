import numpy as np
import pandas as pd


def clean_data(df):
    df = df.copy()

    df.drop_duplicates(subset=["order_id"], inplace=True)

    numeric_cols = df.select_dtypes(include=["number"]).columns
    for col in numeric_cols:
        if df[col].isna().any():
            df[col].fillna(df[col].median(), inplace=True)

    df["unit_price"] = df["unit_price"].clip(lower=0)
    df["quantity"] = df["quantity"].clip(lower=1)
    df["net_revenue"] = df["net_revenue"].clip(lower=0)

    return df


def add_features(df):
    df = df.copy()

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()
    df["day_of_week"] = df["order_date"].dt.day_name()

    df["aov"] = df["net_revenue"] / df["quantity"].replace(0, np.nan)

    df.sort_values("order_date", inplace=True)
    df.set_index("order_date", inplace=True)

    return df
