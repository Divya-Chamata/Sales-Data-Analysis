"""Clean the synthetic sales CSV for practice."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data" / "sales_raw.csv"
output = ROOT / "data" / "sales_cleaned.csv"

df = pd.read_csv(source, parse_dates=["order_date"])
print("Rows before cleaning:", len(df))
print("Missing values by column:\\n", df.isna().sum())
df = df.drop_duplicates()
df = df.dropna(subset=["region"])
df["sales_amount"] = df["quantity"] * df["unit_price"]
df.to_csv(output, index=False)
print("Rows after cleaning:", len(df))
print("Saved:", output)
