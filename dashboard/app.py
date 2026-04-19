import os
import sys
from pathlib import Path

# add project root (parent of dashboard/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import streamlit as st

from src.data_loader import load_sales_data
from src.preprocessing import clean_data, add_features
from src.visualization import revenue_over_time, revenue_by_category, revenue_by_region


st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")
st.title("🛒 RetailPulse: E-Commerce Analytics")

DATA_PATH = Path("data/processed/sales_data.csv")


@st.cache_data
def load_and_prepare(path):
    df = load_sales_data(path)
    df = clean_data(df)
    df = add_features(df)
    return df


if not DATA_PATH.exists():
    st.warning("Dataset not found. Run `python data/generate_dataset.py` first.")
else:
    df = load_and_prepare(DATA_PATH)

    st.sidebar.header("Filters")
    regions = ["All"] + sorted(df["region"].unique().tolist())
    segments = ["All"] + sorted(df["customer_segment"].unique().tolist())

    region_filter = st.sidebar.selectbox("Region", regions)
    segment_filter = st.sidebar.selectbox("Customer Segment", segments)

    filtered = df.copy()
    if region_filter != "All":
        filtered = filtered[filtered["region"] == region_filter]
    if segment_filter != "All":
        filtered = filtered[filtered["customer_segment"] == segment_filter]

    total_revenue = filtered["net_revenue"].sum()
    total_orders = filtered["order_id"].nunique()
    unique_customers = filtered["customer_id"].nunique()
    aov = total_revenue / total_orders if total_orders else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", f"${total_revenue:,.0f}")
    c2.metric("Total Orders", f"{total_orders:,}")
    c3.metric("Unique Customers", f"{unique_customers:,}")
    c4.metric("Average Order Value", f"${aov:,.2f}")

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue Over Time")
        fig_time = revenue_over_time(filtered)
        st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        st.subheader("Revenue by Category")
        fig_cat = revenue_by_category(filtered)
        st.plotly_chart(fig_cat, use_container_width=True)

    st.subheader("Revenue by Region")
    fig_region = revenue_by_region(filtered)
    st.plotly_chart(fig_region, use_container_width=True)
