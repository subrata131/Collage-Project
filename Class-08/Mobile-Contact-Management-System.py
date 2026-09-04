contact={

}

while True:
  print("===Mobile Contact and Call Management System===")
  print("1.Add \n2.View\n3.Search\n4.Update\n5.Remove\n6.Exit")
  n=int(input("Enter Your Choice:"))

  if n==1:
    print("===Add Student===")

    m=input("Enter Contact name:").islower()
    nu=int(input("Enter Number:"))
    contact[m]={
        "number":nu
    }

    print("===Contact Added Sucess===")

  elif n==2:
    n=input("Enter Contact Name:").islower()

    if n in contact:
      print("Contact Found")

      print("===Contact Details===")
      print(f"Contact Name:{contact[name]}")
      print(f"Contact Number:{contact[name]["number"]}")
    else:
      print("Contact Not Found")


  elif n==3:
      if n in contact:
        print("Contact Found")

        print("===Contact Details===")
        print(f"Contact Name:{contact[name]}")
        print(f"Contact Number:{contact[name]["number"]}")
      else:
        print("Contact Not Found")

  elif n==4:
      if n in contact:
        print("Contact Found")

        print("===Update Details===")
        editname=input("Enter Update Name:").islower()
        edit=int(input("Enter Update Number:"))
        contact[name]=editname
        contact[name]["number"]=edit
        print("UPdate Sucess")
      else:
       print("Contact Not Found")

  elif n==5:

      if n in contact:
         print("Contact Found")



      else:
       print("Contact Not Found")


  elif n==6:
    break

  else:
    print("Invaild Input")









