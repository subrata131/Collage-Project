student = {}


def add_student():
    print("==== ADD STUDENT ====")

    roll = int(input("Enter Student Roll Number: "))
    name = input("Enter Student Name: ")
    dept = input("Enter Student Dept: ")

    student[roll] = {
        "Name": name,
        "Department": dept,
        "Attendance": []
    }

    print("==== STUDENT ADDED SUCCESSFULLY ====")


def mark_attendance():
    print("==== MARK ATTENDANCE ====")

    n = int(input("Enter Roll Number to Find Student: "))

    if n in student:
        print("Student Found")

        status = input("Mark Attendance (P/A): ").upper()

        if status == "P" or status == "A":
            student[n]["Attendance"].append(status)

            print("Attendance Added Successfully")

        else:
            print("Invalid Attendance")

    else:
        print("Student Not Found")


def view():
    print("==== ATTENDANCE RECORDS ====")

    if len(student) == 0:
        print("No Student Found")

    else:
        for roll, details in student.items():

            attendance = details["Attendance"]

            print("\nRoll:", roll)
            print("Name:", details["Name"])
            print("Department:", details["Department"])
            print("Attendance:", attendance)

            if attendance:
                p = attendance.count("P")
                n = len(attendance)

                percent = (p / n) * 100

                print("Attendance Percentage:",
                      round(percent, 2), "%")

            else:
                print("Attendance Percentage: 0%")


def search_student():
    print("\n=== SEARCH STUDENT ===")

    roll = int(input("Enter Roll Number to Find Student: "))

    if roll in student:
        print("\nStudent Found")

        print("Roll:", roll)
        print("Name:", student[roll]["Name"])
        print("Department:", student[roll]["Department"])
        print("Attendance:", student[roll]["Attendance"])

    else:
        print("Student Not Found")


def attendance_percentage():
    print("\n=== ATTENDANCE PERCENTAGE ===")

    roll = int(input("Enter Roll Number: "))

    if roll in student:

        attendance = student[roll]["Attendance"]

        if attendance:
            p = attendance.count("P")
            total = len(attendance)

            percent = (p / total) * 100

            print("Student Name:", student[roll]["Name"])
            print("Total Classes:", total)
            print("Present:", p)
            print("Absent:", attendance.count("A"))
            print("Attendance Percentage:",
                  round(percent, 2), "%")

            if percent < 75:
                print("Low Attendance")

        else:
            print("No Attendance Record Found")

    else:
        print("Student Not Found")


print("==== STUDENT ATTENDANCE MANAGEMENT SYSTEM ====")

while True:

    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Student")
    print("4. Search Student")
    print("5. Attendance Percentage")
    print("6. Exit")

    n = int(input("\nEnter Your Choice: "))

    if n == 1:
        add_student()

    elif n == 2:
        mark_attendance()

    elif n == 3:
        view()

    elif n == 4:
        search_student()

    elif n == 5:
        attendance_percentage()

    elif n == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Input")
