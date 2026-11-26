# Student records using lists, tuples, dictionaries, text files, and CSV
import csv

students = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78},
]
course = ("Python", 4)
print("Course Tuple:", course)

with open("students.txt", "w", encoding="utf-8") as text_file:
    for student in students:
        text_file.write(str(student) + "\n")

with open("students.csv", "w", newline="", encoding="utf-8") as csv_file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("\n--- Records from CSV ---")
with open("students.csv", newline="", encoding="utf-8") as csv_file:
    for row in csv.DictReader(csv_file):
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])
