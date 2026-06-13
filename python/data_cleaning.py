import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df[["Order Date", "Ship Date"]].head())

print("\nDate Types:")
print(df[["Order Date", "Ship Date"]].dtypes)
























# import pandas as pd
#
# df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")
#
# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])
#
# print("\nMissing Values:")
# print(df.isnull().sum())
#
# print("\nDuplicate Rows:")
# print(df.duplicated().sum())
#
# print("\nData Types:")
# print(df.dtypes)