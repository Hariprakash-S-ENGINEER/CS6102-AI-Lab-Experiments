# Data cleaning, missing-value handling, and exploratory analysis
import pandas as pd

data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82],
}
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df.to_string(index=False))
print("\nMissing Values:")
print(df.isnull().sum().to_string())

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df.to_string(index=False))
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2).to_string())
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
