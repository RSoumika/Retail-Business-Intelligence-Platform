import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df.to_csv("../data/superstore_cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")