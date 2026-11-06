"""Basic sales analysis using pandas."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
file_path = ROOT / "data" / "sales_cleaned.csv"
if not file_path.exists():
    raise SystemExit("Run clean_data.py first to create data/sales_cleaned.csv")

df = pd.read_csv(file_path, parse_dates=["order_date"])
print("Total sales:", df["sales_amount"].sum())
print("\\nTop 5 products by sales:")
print(df.groupby("product_name")["sales_amount"].sum().sort_values(ascending=False).head(5))
print("\\nSales by region:")
print(df.groupby("region")["sales_amount"].sum().sort_values(ascending=False))
df["month"] = df["order_date"].dt.to_period("M").astype(str)
print("\\nMonthly sales:")
print(df.groupby("month")["sales_amount"].sum())
