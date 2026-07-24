fixed=50
while True:
    name=input("Enter User ID:")
    n=int(input("Enter units:"))
    print("User ID is:",name)

    if n<=100:
        t=n*1.5
        print(f"Rate is {t}+{fixed}={t+fixed}")
    elif (100<n<=200):
        t=((100*1.5)+((n-100)*2.5))
        print(f"Rate is {t}+{fixed}={t+fixed}")
    elif (200<n<=300):
        t=((100*1.5)+(100*2.5)+((n-200)*4.0))
        print(f"Rate is {t}+{fixed}={t+fixed}")
    else:
        t=((100*1.5)+(100*2.5)+(100*4.0)+((n-300)*6.0))
        print(f"Rate is {t}+{fixed}={t+fixed}")

        if t>1000:
            discount=n*0.1
            t=t-discount
            print(f"your Discount Is:{discount}")
            print(f"Total Bill is:{t}")
  