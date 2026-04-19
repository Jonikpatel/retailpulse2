import plotly.express as px


def revenue_over_time(df):
    data = df.resample("M")["net_revenue"].sum().reset_index()
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
