def password(m):
    upper=False
    lower=False
    number=False
    spe=False

    if len(m)>=8:
        for i in m:
            if i.isupper():
                upper=True
            elif i.islower():
                lower=True
            elif i.isdigit():
                number=True
            else:
                spe=True

        if upper==True:
            if lower==True:
                if number==True:
                    if spe==True:
                        print("Strong")
                    else:
                        print("Medium")
                else:
                    print("Medium")
            else:
                print("Weak")
        else:
            print("Weak")

    else:
        print("Password should be 8 char")


n=input("Enter Your Password: ")
password(n)




