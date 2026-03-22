import pandas as pd

# Student DataFrame 
data = {
    "name": ["Rahul", "Anjali", "Rohit", "Priya"],
    "age": [20, 21, 22, 20],
    "marks": [85, 92, 78, 88],
    "city": ["Delhi", "Mumbai", "Jaipur", "Pune"]
}

# Custom index with student IDs
df = pd.DataFrame(data, index=["S101", "S102", "S103", "S104"])

# Full DataFrame print
print("=== Full Student DataFrame ===")
print(df)

# loc - label se row access
print("\n=== Student S103 ki details (loc) ===")
print(df.loc["S103"])

# iloc - index number se row access
print("\n=== Pehle student ki details (iloc) ===")
print(df.iloc[0])

# Extra 
print("\n=== Sirf Names aur Marks ===")
print(df[["name", "marks"]])

print("\n=== 85 se zyada marks wale students ===")
print(df[df["marks"] > 85])