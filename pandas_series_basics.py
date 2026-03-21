# pandas_series_basics.py

"""
Pandas Series Practice

This script demonstrates:
- Creating a Pandas Series
- Custom indexing
- Updating values
- Accessing data using .loc
- Filtering data using conditions
"""

import pandas as pd

# -------------------------------
# Example 1: Creating Series
# -------------------------------

data = [100, 22, 220]

series = pd.Series(data, index=("a", "b", "c"))

# Update value
series.loc["a"] = 200

print("Updated Series:")
print(series)

print("\nValue at index 'a':")
print(series.loc["a"])

print("\nValues greater than or equal to 200:")
print(series[series >= 200])


# -------------------------------
# Example 2: Dictionary to Series
# -------------------------------

calories = {
    "Day 1": 1200,
    "Day 2": 3600,
    "Day 3": 6700
}

series = pd.Series(calories)

# Modify value
series.loc["Day 3"] += 5000

print("\nUpdated Calories Series:")
print(series)

print("\nCalories on Day 1:")
print(series.loc["Day 1"])

print("\nDays with calories > 1800:")
print(series[series > 1800])
