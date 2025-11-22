import json
import os

DATA_FILE = "students.json"


# ------------------------------
# Load Data from JSON File
# ------------------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# ------------------------------
# Save Data to JSON File
# ------------------------------
def save_data(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


# ------------------------------
# Add a New Student
# ------------------------------
def add_student():
    students = load_data()
    
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(student)
    save_data(students)
    print("Student added successfully!\n")


# ------------------------------
# View All Students
# ------------------------------
def view_students():
    students = load_data()
    
    if not students:
        print("No student records found.\n")
        return
    
    print("\n--- Student Records ---")
    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print("--------------------------")
    print()


# ------------------------------
# Search for a Student
# ------------------------------
def search_student():
    students = load_data()
    search_id = input("Enter Student ID to search: ")
    
    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print()
            return
    
    print("Student not found.\n")


# ------------------------------
# Update Student Data
# ------------------------------
def update_student():
    students = load_data()
    update_id = input("Enter Student ID to update: ")
    
    for student in students:
        if student["id"] == update_id:
            print("\nEnter new details (leave blank to keep previous):")
            name = input(f"New Name ({student['name']}): ") or student['name']
            age = input(f"New Age ({student['age']}): ") or student['age']
            course = input(f"New Course ({student['course']}): ") or student['course']
            
            student["name"] = name
            student["age"] = age
            student["course"] = course
            
            save_data(students)
            print("Student updated successfully!\n")
            return
    
    print("Student not found.\n")


# ------------------------------
# Delete a Student
# ------------------------------
def delete_student():
    students = load_data()
    delete_id = input("Enter Student ID to delete: ")
    
    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            save_data(students)
            print("Student deleted successfully!\n")
            return
    
    print("Student not found.\n")


# ------------------------------
# Main Menu
# ------------------------------
def main():
    while True:
        print("====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
