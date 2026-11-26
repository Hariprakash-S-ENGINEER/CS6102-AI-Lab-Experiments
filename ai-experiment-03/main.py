# Menu-driven student information management
students = {}

def add_student(roll, name, department):
    students[roll] = {"Name": name, "Department": department}

def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, record in students.items():
        print(f"Roll No: {roll} | Name: {record['Name']} | Department: {record['Department']}")

def search_student(roll):
    record = students.get(roll)
    print(record if record else "Student not found.")

def delete_student(roll):
    if students.pop(roll, None) is None:
        print("Student not found.")
    else:
        print("Student deleted successfully.")

while True:
    print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_student(input("Enter Roll No: "), input("Enter Name: "), input("Enter Department: "))
        print("Student added successfully.")
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student(input("Enter Roll No to search: "))
    elif choice == "4":
        delete_student(input("Enter Roll No to delete: "))
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
