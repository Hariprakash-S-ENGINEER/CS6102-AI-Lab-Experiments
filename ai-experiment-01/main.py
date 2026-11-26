# Student marks, percentage, grade, and academic performance
name = input("Enter student name: ").strip()
count = int(input("Enter number of subjects: "))
if count <= 0:
    raise ValueError("Number of subjects must be positive")

marks = [float(input(f"Enter mark for Subject {i}: ")) for i in range(1, count + 1)]
total = sum(marks)
percentage = total / count

if percentage >= 90:
    grade, performance = "A+", "Outstanding"
elif percentage >= 80:
    grade, performance = "A", "Excellent"
elif percentage >= 70:
    grade, performance = "B", "Very Good"
elif percentage >= 60:
    grade, performance = "C", "Good"
elif percentage >= 50:
    grade, performance = "D", "Average"
else:
    grade, performance = "F", "Needs Improvement"

print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Performance :", performance)
