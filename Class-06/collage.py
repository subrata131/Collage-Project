emp=[]

while True:
    print("====Employee Management System====")
    print("1.Add Employee\n2.View Employee\n3.Search Employee\n4.Delete Employee\n5.Exit\n")
    n=int(input("Enter Your choice:"))

    if n==1:
        m=int(input("\nEnter Employee ID:"))
        name=input("Enter Employee Name:")
        salary=int(input("Enter Employee Salary:"))
        emp1=(m,name,salary)
        emp.append(emp1)
        print("Employee Added Successfully!!")
    elif n==2:
        print("====Employee Detials====")
        if len(emp)==0:
            print("No record Found")
        else:
            for i in emp:
                print(f"Employee ID: {i[0]}\nEmployee Name:{i[1]}\nEmployee Salary: {i[2]}\n")

    elif n==3:
        m=int(input("Enter Employee ID :"))

        found=False

        for i in emp:
            if i[0]==m:
                print(f"Employee ID: {i[0]}\nEmployee Name:{i[1]}\nEmployee Salary: {i[2]}\n")
                found=True

        if not found:
            print("No Record Found!!")

    elif n==4:
        m=int(input("Enter Employee ID :"))
        
        found=False
        
        for i in emp:
            if i[0]==m:
                emp.remove(i)
                found= True
                print("Remove Sucessfull")

        if not found:
            print("No Record Found")

    elif n==5:
        print("Exiting...")
        break
    else:
        print("Invalid Input")
            
            
                

                

        
