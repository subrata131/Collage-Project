cart = {}

while True:
    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Total Bill")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        cart[product] = (price, quantity)
        print("Product added.")

    elif choice == "2":
        if not cart:
            print("Cart is empty.")
        else:
            for product, (price, quantity) in cart.items():
                print(product, "Price:", price, "Quantity:", quantity)

    elif choice == "3":
        product = input("Enter product name: ")

        if product in cart:
            del cart[product]
            print("Product removed.")
        else:
            print("Product not found.")

    elif choice == "4":
        total = 0

        for product, (price, quantity) in cart.items():
            total += price * quantity

        print("Total Bill: ₹", total)

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")
