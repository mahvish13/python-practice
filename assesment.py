import os
class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.roll_no},{self.name},{self.age},{self.course}"

FILE_NAME = "students.txt"

def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    student = Student(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )
                    students.append(student)

    except FileNotFoundError:
        print("\nNo student record found. New file will be created.")

    return students

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(str(student) + "\n")

def add_student():
    students = load_students()

    roll = input("Enter Roll Number: ")

    for student in students:
        if student.roll_no == roll:
            print("Roll Number already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students.append(Student(roll, name, age, course))

    save_students(students)

    print("Student Added Successfully.")

def view_students():
    students = load_students()

    if not students:
        print("No Records Found.")
        return

    print("\n------ Student Records ------")

    for student in students:
        print("---------------------------")
        print("Roll No :", student.roll_no)
        print("Name    :", student.name)
        print("Age     :", student.age)
        print("Course  :", student.course)

def search_student():
    students = load_students()

    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student.roll_no == roll:
            print("\nStudent Found")
            print("Roll No :", student.roll_no)
            print("Name    :", student.name)
            print("Age     :", student.age)
            print("Course  :", student.course)
            return

    print("Student Not Found.")

def update_student():
    students = load_students()

    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student.roll_no == roll:
            student.name = input("Enter New Name: ")
            student.age = input("Enter New Age: ")
            student.course = input("Enter New Course: ")

            save_students(students)

            print("Student Updated Successfully.")
            return

    print("Student Not Found.")

def delete_student():
    students = load_students()

    roll = input("Enter Roll Number to Delete: ")

    updated_students = []

    found = False

    for student in students:
        if student.roll_no == roll:
            found = True
        else:
            updated_students.append(student)

    if found:
        save_students(updated_students)
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")

def menu():

    while True:

        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your Choice: ")

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
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")
menu()