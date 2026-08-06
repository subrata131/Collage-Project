email = input("Enter your email: ")

at = 0
dot = 0


for ch in email:
    if ch == "@":
        at += 1
    elif ch == ".":
        dot += 1


if at == 1 and dot >= 1:
    at_pos = email.find("@")
    dot_pos = email.rfind(".")

    if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
        print("Valid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")
