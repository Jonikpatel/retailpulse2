import plotly.express as px


import pandas as pd
import plotly.express as px


def revenue_over_time(df):
    df = df.copy()

    # Case 1: date is a column
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"])
        df = df.set_index("order_date")

    # Case 2: date is already in the index
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Resample on the datetime index
    data = df["net_revenue"].resample("M").sum().reset_index()

    # After reset_index, the first column is the date
    date_col = data.columns[0]

    fig = px.line(data, x=date_col, y="net_revenue", title="Monthly Revenue")
    return fig

    fig = px.line(data, x="order_date", y="net_revenue", title="Monthly Revenue")
    return fig


def revenue_by_category(df):
    grouped = df.groupby("product_category")["net_revenue"].sum().reset_index()
    fig = px.bar(grouped, x="product_category", y="net_revenue", title="Revenue by Category")
    return fig


def revenue_by_region(df):
    grouped = df.groupby("region")["net_revenue"].sum().reset_index()
    fig = px.bar(grouped, x="region", y="net_revenue", title="Revenue by Region")
    return fig
