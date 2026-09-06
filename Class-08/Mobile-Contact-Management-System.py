contact = {}

while True:
    print("\n=== Mobile Contact and Call Management System ===")
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Remove")
    print("6. Exit")

    n = int(input("Enter Your Choice: "))


    if n == 1:
        print("\n=== Add Contact ===")

        name = input("Enter Contact Name: ").lower()
        number = input("Enter Number: ")

        contact[name] = {
            "number": number
        }

        print("=== Contact Added Successfully ===")


    elif n == 2:
        print("\n=== Contact List ===")

        if len(contact) == 0:
            print("No Contacts Found")
        else:
            for name, i in contact.items():
                print(f"Contact Name: {name}")
                print(f"Contact Number: {i['number']}")
                print("----------------------")


    elif n == 3:
        print("\n=== Search Contact ===")

        name = input("Enter Contact Name: ").lower()

        if name in contact:
            print("Contact Found")
            print("=== Contact Details ===")
            print(f"Contact Name: {name}")
            print(f"Contact Number: {contact[name]['number']}")
        else:
            print("Contact Not Found")


    elif n == 4:
        print("\n=== Update Contact ===")

        name = input("Enter Contact Name: ").lower()

        if name in contact:
            print("Contact Found")

            editname = input("Enter New Contact Name: ").lower()
            editnumber = input("Enter New Number: ")

            contact[editname] = {
                "number": editnumber
            }

            if editname != name:
                del contact[name]

            print("Contact Updated Successfully")
        else:
            print("Contact Not Found")

    elif n == 5:
        print("\n=== Remove Contact ===")

        name = input("Enter Contact Name: ").lower()

        if name in contact:
            print("Contact Found")

            del contact[name]

            print("Contact Removed Successfully")
        else:
            print("Contact Not Found")


    elif n == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Input")
