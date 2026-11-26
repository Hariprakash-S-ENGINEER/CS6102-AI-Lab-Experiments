# Student data cleaning, analysis, and visualization
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([
    ["S101", "Aarav", "CSE", 92, 88, 91],
    ["S102", "Diya", "ECE", 85, 76, 82],
    ["S103", "Kavin", "CSE", 78, 81, 79],
    ["S104", "Meera", "IT", 96, 93, 95],
    ["S105", "Arjun", "ECE", None, 72, 75],
    ["S106", "Nila", "CSE", 88, None, 86],
    ["S101", "Aarav", "CSE", 92, 88, 91],
], columns=["Student_ID", "Name", "Department", "Attendance_Percentage",
            "Assignment_Score", "Exam_Score"])

print("----- ORIGINAL DATASET -----")
print(df.head().to_string(index=False))
print("\nDataset Shape:", df.shape)
print("\n----- MISSING VALUES -----")
print(df.isnull().sum().to_string())
print("\nDuplicate Records:", df.duplicated().sum())

numeric = ["Attendance_Percentage", "Assignment_Score", "Exam_Score"]
for column in numeric:
    df[column] = df[column].fillna(df[column].median())
df["Department"] = df["Department"].fillna(df["Department"].mode().iloc[0])
df = df.drop_duplicates().copy()
df["Average_Score"] = df[["Assignment_Score", "Exam_Score"]].mean(axis=1)
df["Performance"] = pd.cut(
    df["Average_Score"], [-1, 50, 70, 85, 100],
    labels=["Needs Improvement", "Average", "Good", "Excellent"]
)

print("\nCleaned Dataset Shape:", df.shape)
print("\nDepartment-wise average exam score:")
print(df.groupby("Department")["Exam_Score"].mean().round(2).to_string())
print("\nPerformance distribution:")
print(df["Performance"].value_counts(sort=False).to_string())

df.groupby("Department")["Exam_Score"].mean().plot(kind="bar", title="Department Average Exam Score")
plt.ylabel("Average exam score")
plt.tight_layout()
plt.savefig("department_average.png")
plt.close()

df["Performance"].value_counts(sort=False).plot(kind="bar", title="Student Performance Distribution")
plt.ylabel("Number of students")
plt.tight_layout()
plt.savefig("performance_distribution.png")
plt.close()
print("\nCharts saved: department_average.png, performance_distribution.png")
