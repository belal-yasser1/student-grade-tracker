import pandas as pd

students = []

def add_student(name, grade):
    student = {"name": name, "grade": grade}
    students.append(student)

def save_students():
    df = pd.DataFrame(students)
    df.to_csv("students.csv", index=False)
    print("Saved!")

def load_students():
    global students
    df = pd.read_csv("students.csv")
    students = df.to_dict("records")
    print("Loaded!")

def view_students():
    if not students:
        print("No students yet!")
        return
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}")
        if student["grade"] >= 60:
            print(f"{student['name']} has passed ✅")
        else:
            print(f"{student['name']} has failed ❌")

def show_stats():
    if not students:
        print("No students yet!")
        return
    grades = [student["grade"] for student in students]
    print(f"Average grade: {sum(grades)/len(grades):.2f}")
    print(f"Highest grade: {max(grades)}")
    print(f"Lowest grade: {min(grades)}")

def menu():
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Show Statistics")
        print("4. Save Students")
        print("5. Load Students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)
        elif choice == 2:
            view_students()
        elif choice == 3:
            show_stats()
        elif choice == 4:
            save_students()
        elif choice == 5:
            load_students()
        elif choice == 6:
            print("Goodbye!")
            break

menu()