# PLOTTING REVENUE Vs PROFIT

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

category_data = df.groupby("Category")[["Sales", "Profit"]].sum()

category_data.plot(kind="bar", figsize=(8,5))

plt.title("Revenue and Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.tight_layout()
plt.show()














# ONLY PLOTTING THE REVENUE
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")
#
# category_sales = df.groupby("Category")["Sales"].sum()
#
# plt.figure(figsize=(8,5))
# category_sales.plot(kind="bar")
#
# plt.title("Sales by Category")
# plt.xlabel("Category")
# plt.ylabel("Revenue")
#
# plt.tight_layout()
# plt.show()