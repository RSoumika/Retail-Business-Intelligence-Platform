import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

region_data = df.groupby("Region")[["Sales", "Profit"]].sum()

region_data.plot(kind="bar", figsize=(8,5))

plt.title("Revenue and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount")

plt.tight_layout()
plt.show()