import plotly.express as px


def revenue_over_time(df):
    # Ensure order_date is datetime
    if df["order_date"].dtype != "datetime64[ns]":
        df = df.copy()
        df["order_date"] = pd.to_datetime(df["order_date"])

    # Resample on order_date as index
    data = (
        df.set_index("order_date")
          .resample("M")["net_revenue"]
          .sum()
          .reset_index()
    )

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
