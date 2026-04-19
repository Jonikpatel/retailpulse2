import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def generate_sales_data(n_rows=50000, random_state=42):
    rng = np.random.default_rng(random_state)

    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=int(x)) for x in rng.integers(0, 365, size=n_rows)]

    categories = ["Electronics", "Apparel", "Home & Kitchen", "Beauty", "Sports"]
    regions = ["North", "South", "East", "West"]
    segments = ["Low-Value", "Mid-Value", "High-Value", "Premium"]

    category_choices = rng.choice(categories, size=n_rows, p=[0.18, 0.25, 0.27, 0.15, 0.15])
    region_choices = rng.choice(regions, size=n_rows)
    segment_choices = rng.choice(segments, size=n_rows, p=[0.45, 0.30, 0.20, 0.05])

    base_price_map = {
        "Electronics": 220.0,
        "Apparel": 45.0,
        "Home & Kitchen": 80.0,
        "Beauty": 35.0,
        "Sports": 70.0,
    }

    prices = []
    for cat in category_choices:
        mean = base_price_map[cat]
        price = rng.normal(loc=mean, scale=0.2 * mean)
        prices.append(max(5.0, round(price, 2)))

    quantities = rng.integers(1, 6, size=n_rows)
    discounts = rng.choice([0, 5, 10, 15, 20], size=n_rows, p=[0.40, 0.25, 0.20, 0.10, 0.05])

    df = pd.DataFrame(
        {
            "order_id": np.arange(1, n_rows + 1),
            "order_date": dates,
            "customer_id": rng.integers(1000, 1000 + 5000, size=n_rows),
            "region": region_choices,
            "customer_segment": segment_choices,
            "product_category": category_choices,
            "unit_price": prices,
            "quantity": quantities,
            "discount_pct": discounts,
        }
    )

    df["gross_revenue"] = df["unit_price"] * df["quantity"]
    df["net_revenue"] = df["gross_revenue"] * (1 - df["discount_pct"] / 100.0)

    return df


def main():
    processed_dir = os.path.join(os.path.dirname(__file__), "processed")
    os.makedirs(processed_dir, exist_ok=True)
    output_path = os.path.join(processed_dir, "sales_data.csv")

    df = generate_sales_data()
    df.to_csv(output_path, index=False)
    print("Saved synthetic dataset to", output_path)


if __name__ == "__main__":
    main()
