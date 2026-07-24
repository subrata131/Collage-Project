account={
         }

while True:
   print("===Bank Management System===")
   print("\n1.Creat Account\n2.Money Deposite\n3.Withdraw Amount\n4.Exit\n")
   n=int(input("Enter Your Choice:"))
   if n==1:
    n=int(input("Enter Your Account Number:"))
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    type_ac=input("Enter Account Type:")
    amo=int(input("Enter Amount to Deposite:"))
    account[n]={
        "name":name,
        "age":age,
        "Account_Type":type_ac,
        "Amount":amo

    }
    print("Account Creat Sucessfully")
   elif n==2:
    n=int(input("Enter Account number:"))
    if n in account:
      print("Account Fatch Sucessful")
      print("===Account Details===")
      # for i ,j in account:
      #   print(i,"=",j) \
      m=int(input("Enter Amount To Deposite:"))
      account[n]["Amount"]=(m+amo)
      print("Deposite Sucessfully")
      print("Avaliable Balance:",account[n]["Amount"])
    else:
      print("Not Found")
   elif n==3:
    n=int(input("Enter Account number:"))
    if n in account:
      print("Account Fatch Sucessful")
      m=int(input("Enter Amount To Withdraw:"))
      net=account[n]["Amount"]-m
      print("Withdraw Sucessfully")
      print("Avaliable Balance is:",net)
    else:
      print("not Found")
   elif n==4:
    break
   else:
    print("Invalid Input")
