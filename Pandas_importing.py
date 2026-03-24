import pandas as pd

# ========== CSV File ==========

df_csv = pd.read_csv("data/students.csv")

print("=== CSV - Pehli 5 Rows ===")
print(df_csv.head())         

print("\n=== CSV - Poora Data ===")
print(df_csv.to_string())

print("\n=== CSV - Basic Info ===")
print(df_csv.shape)           
print(df_csv.columns.tolist()) # column names

# ========== JSON File ==========

df_json = pd.read_json("data/students.json")

print("\n=== JSON - Pehli 5 Rows ===")
print(df_json.head())

print("\n=== JSON - Poora Data ===")
print(df_json.to_string())    

print("\n=== JSON - Basic Info ===")
print(df_json.shape)
print(df_json.columns.tolist())
