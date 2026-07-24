
while True:
  print("===Bank Management System===")
  print("\n1.Creat Account\n2.Money Deposite\n3.Withdraw Amount\n4.Exit\n")
  n=int(input("Enter Your Choice:"))
  if n==1:
    n=int(input("Enter Account Number:"))
    # data.append(n)
    print("Your Account Number is:",n)
  elif n==2:
    n=int(input("Enter Amount To deposite:"))
    amount=n
    print("Deposite Sucessfull")
    print("Available Balance is:",amount)
  elif n==3:
    n=int(input("Enter Amount To Withdraw:"))
    if n<=amount:
      # print("Withdraw Unsucessful")
      # continue
      net=amount-n
      print("Withdraw Sucessful")
      print("Available balance is:",net)
    else:
      print("Withdraw Unsucessful")
      print("Available Balance is:",amount)


    # net=amount-n
    # print("Withdraw Sucessful")
    # print("Available balance is:",net)
  elif n==4:
    break
  else:
    print("Invalid Input")
