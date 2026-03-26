import pandas as pd

# Load CSV with name as index
df = pd.read_csv("data/students.csv", index_col="name")

print("=== Full DataFrame ===")
print(df.to_string())

# ========== Advanced iloc Selection ==========

print("\n=== Every 2nd Row, First 3 Columns (iloc slicing) ===")
print(df.iloc[0:4:2, 0:3])

print("\n=== Last 2 Rows ===")
print(df.iloc[-2:])

print("\n=== First 3 Rows, Only Age & City ===")
print(df.iloc[0:3, 0:2])

# ========== User Input with Error Handling ==========

student = input("\nEnter Student Name: ")

try:
    print(f"\n=== {student}'s Details ===")
    print(df.loc[student])
except KeyError:
    print(f"'{student}' not found