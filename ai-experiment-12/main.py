# Generates technical notes and reusable Python templates from task specs
from pathlib import Path

tasks = [
    ("G101", "CSV Data Analysis", "Beginner Python student",
     "Create a Python function to average numeric values in a CSV column.",
     "Validate the column, ignore missing values, and round to two decimals."),
    ("G102", "Temperature Conversion", "Beginner Python student",
     "Generate a function to convert Celsius to Fahrenheit.",
     "Accept numeric input and use F = (C * 9/5) + 32."),
    ("G103", "Password Validation", "Intermediate Python student",
     "Generate a password-strength checker.",
     "Check length, uppercase, lowercase, digit, and special character."),
    ("G104", "List Statistics", "Beginner Python student",
     "Generate a function to find minimum, maximum, and range.",
     "Reject an empty list and return the three statistics."),
    ("G105", "Text Analysis", "Beginner Python student",
     "Generate a function to count total and unique words.",
     "Normalize case and remove punctuation before counting."),
]

templates = {
    "CSV Data Analysis": """import pandas as pd

def column_average(filename, column):
    data = pd.read_csv(filename)
    if column not in data.columns:
        raise ValueError("Column not found")
    values = pd.to_numeric(data[column], errors="coerce").dropna()
    if values.empty:
        raise ValueError("No numeric values")
    return round(values.mean(), 2)
""",
    "Temperature Conversion": """def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be numeric")
    return round(celsius * 9 / 5 + 32, 2)
""",
    "Password Validation": """def check_password(password):
    checks = [
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ]
    return all(checks)
""",
    "List Statistics": """def list_statistics(values):
    if not values:
        raise ValueError("List cannot be empty")
    return {
        "minimum": min(values),
        "maximum": max(values),
        "range": max(values) - min(values),
    }
""",
    "Text Analysis": """import string

def analyze_text(text):
    cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    return {"total_words": len(words), "unique_words": len(set(words))}
""",
}

output_dir = Path("generated_technical_content")
output_dir.mkdir(exist_ok=True)
print("----- TECHNICAL CONTENT AND PYTHON PROGRAM GENERATION -----")
for task_id, topic, audience, description, requirements in tasks:
    stem = task_id.lower()
    notes = (
        f"Topic: {topic}\n"
        f"Audience: {audience}\n"
        f"Task: {description}\n"
        f"Requirements: {requirements}\n"
        "Approach: validate inputs, process data and present a clear result."
    )
    (output_dir / f"{stem}.py").write_text(templates[topic], encoding="utf-8")
    (output_dir / f"{stem}_notes.txt").write_text(notes, encoding="utf-8")
    print(f"Saved: {stem}.py and {stem}_notes.txt")

print("\nTotal generated files:", len(list(output_dir.iterdir())))
print("Template-based generation completed. No external LLM is called.")
