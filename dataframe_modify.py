import pandas as pd

# Base DataFrame
data = {
    "Name": ["Rahul", "Anjali", "Rohit"],
    "Age": [20, 21, 22],
    "City": ["Delhi", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data, index=["Student 1", "Student 2", "Student 3"])

print("=== Original DataFrame ===")
print(df)

# Add new column
df["Course"] = ["Python", "Java", "C++"]

print("\n=== After adding new column  ===")
print(df)

# Add new rows 
new_rows = pd.DataFrame(
    [
        {"Name": "Priya",  "Age": 23, "City": "Pune",    "Course": "AI"},
        {"Name": "Karan",  "Age": 24, "City": "Chennai", "Course": "Web Dev"}
    ],
    index=["Student 4", "Student 5"]
)

df = pd.concat([df, new_rows])

print("\n=== After adding new rows ===")
print(df)

# info check
print("\n=== DataFrame Info ===")
print(df.shape)  
print(df.dtypes)  #data type of column