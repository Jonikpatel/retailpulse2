import pandas as pd

from src.preprocessing import clean_data, add_features


def test_clean_and_add_features_basic():
    data = {
        "order_id": [1, 2, 2],
        "order_date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-02"]),
        "customer_id": [101, 102, 102],
        "region": ["North", "South", "South"],
        "customer_segment": ["Low-Value", "High-Value", "High-Value"],
        "product_category": ["Electronics", "Apparel", "Apparel"],
        "unit_price": [100.0, 50.0, 50.0],
        "quantity": [1, 2, 2],
        "discount_pct": [0, 10, 10],
        "gross_revenue": [100.0, 100.0, 100.0],
        "net_revenue": [100.0, 90.0, 90.0],
    }
    df = pd.DataFrame(data)

    cleaned = clean_data(df)
    assert cleaned["order_id"].nunique() == 2
    assert (cleaned["unit_price"] >= 0).all()
    assert (cleaned["quantity"] >= 1).all()

    featured = add_features(cleaned)
    assert {"order_year", "order_month", "day_of_week", "aov"}.issubset(featured.columns)
