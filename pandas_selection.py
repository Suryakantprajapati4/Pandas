import pandas as pd

# Load CSV with name as index
df = pd.read_csv("data/students.csv", index_col="name")

print("=== Full DataFrame ===")
print(df.to_string())

# ========== Column Selection ==========

print("\n=== Single Column (Age) ===")
print(df["age"].to_string())

print("\n=== Multiple Columns (Age + City) ===")
print(df[["age", "city"]].to_string())

# ========== Row Selection ==========

print("\n=== Single Row by Label (loc) ===")
print(df.loc["Rahul"])

print("\n=== Row Range with Specific Columns ===")
print(df.loc["Rahul":"Priya", ["age", "city"]])

print("\n=== Single Row by Position (iloc) ===")
print(df.iloc[0])