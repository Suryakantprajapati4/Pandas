import pandas as pd

# Load CSV
df = pd.read_csv("data/students.csv")

print("=== Full DataFrame ===")
print(df.to_string())

# ========== Single Condition Filtering ==========

print("\n=== Students Above Age 21 (>) ===")
adult = df[df["age"] > 21]
print(adult.to_string())

print("\n=== Students Exactly Age 21 (==) ===")
exact_age = df[df["age"] == 21]
print(exact_age.to_string())

print("\n=== Students Age 20 or Below (<=) ===")
young = df[df["age"] <= 20]
print(young.to_string())

# ========== OR Condition Filtering ==========

print("\n=== City is Delhi OR Course is AI (|) ===")
city_or_course = df[(df["city"] == "Delhi") |
                    (df["course"] == "AI")]
print(city_or_course.to_string())

# ========== AND Condition Filtering ==========

print("\n=== City is Delhi AND Course is Python (&) ===")
city_and_course = df[(df["city"] == "Delhi") &
                     (df["course"] == "Python")]
print(city_and_course.to_string())

# ========== Bonus ==========

print("\n=== Students NOT from Mumbai (~) ===")
not_mumbai = df[~(df["city"] == "Mumbai")]
print(not_mumbai.to_string())