student={

}


while True:
  print("===Studence Result Mangement System===")

  print("1.Enter Student Details\n2.Add Mark\n3.Display\n4.Exit")

  n =int(input("Enter Your Choice:"))
  if n==1:
    print("===Enter Student Details===")
    roll=int(input("Enter Student Roll:"))
    name=input("Enter Student name:")
    clas=input("Enter Student Depertment:")


    student[roll]={
        "name": name,
        "class": clas,
        "marks": []

    }

  elif n==2:

      n=int(input("Enter Student Roll Number:"))

      if n in student:
        print("Student Fatch")

        m=int(input("Enter Python Mark:"))
        math=int(input("Enter Math mark:"))

        student[roll]["marks"].append(m)
        student[roll]["marks"].append(math)

        print("Mark Added Sucess")
      else:
        print("Student Not Found")


  elif n==3:
      n=int(input("Enter Student Roll Number:"))

      if n in student:
        print("Student Fatch")

        print("===Student Details===")

        print(f"Student Name:{student[n]["name"]}")
        print(f"Student Department:{student[n]["class"]}")
        marks_list = student[roll]["marks"]
        if marks_list:
              total_sum = sum(marks_list)
              ave = total_sum / len(marks_list)
              print("Total Marks:", total_sum)
              print("Average Marks:", round(ave, 2))


      else:
        print("Student Not Found")


  elif n==4:
      break

  else:
    print("Invalid Input")




