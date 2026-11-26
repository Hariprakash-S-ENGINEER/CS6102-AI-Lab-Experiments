# Retail sales analysis and four Matplotlib charts
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([
    ["2026-01-05", "Laptop", "Electronics", "North", 3, 52000],
    ["2026-01-12", "Phone", "Electronics", "South", 8, 18000],
    ["2026-01-18", "Chair", "Furniture", "East", 6, 3500],
    ["2026-01-24", "Desk", "Furniture", "West", 4, 7200],
    ["2026-02-03", "Laptop", "Electronics", "East", 2, 52000],
    ["2026-02-10", "Phone", "Electronics", "South", 3, 18000],
], columns=["Date", "Product", "Category", "Region", "Units_Sold", "Unit_Price"])
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("----- RETAIL SALES DATASET -----")
print(df.head().to_string(index=False))
print("\nTotal Units Sold:", df["Units_Sold"].sum())
print("Total Revenue: Rs.", df["Revenue"].sum())

monthly = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
category = df.groupby("Category")["Revenue"].sum()
region = df.groupby("Region")["Revenue"].sum()
print("\n----- MONTHLY REVENUE -----\n", monthly.to_string())
print("\n----- CATEGORY-WISE REVENUE -----\n", category.to_string())
print("\n----- REGION-WISE REVENUE -----\n", region.to_string())

monthly.index = monthly.index.astype(str)
monthly.plot(marker="o", title="Monthly Retail Revenue")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

category.plot(kind="bar", title="Category-wise Revenue")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.close()

region.plot(kind="pie", autopct="%1.1f%%", title="Region-wise Revenue")
plt.ylabel("")
plt.tight_layout()
plt.savefig("region_revenue.png")
plt.close()

plt.scatter(df["Units_Sold"], df["Revenue"])
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("units_vs_revenue.png")
plt.close()
print("\nCharts saved: monthly_revenue.png, category_revenue.png, region_revenue.png, units_vs_revenue.png")
