
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(self.roll, self.name, self.marks)


class StudentManagement:
    def add_student(self):
        roll = input("Enter roll: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as f:
            f.write(roll + "," + name + "," + marks + "\n")

        print("Student added!")

    def display_students(self):
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    student = Student(data[0], data[1], data[2])
                    student.display()
        except FileNotFoundError:
            print("No records found!")

    def search_student(self):
        roll = input("Enter roll to search: ")

        try:
            with open("students.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if data[0] == roll:
                        Student(data[0], data[1], data[2]).display()
                        return

            print("Student not found!")

        except FileNotFoundError:
            print("No records found!")


s = StudentManagement()

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        s.add_student()
    elif choice == "2":
        s.display_students()
    elif choice == "3":
        s.search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

