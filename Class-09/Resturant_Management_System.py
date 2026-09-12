restaurant = {}
order = {}

def add_menu() :
    print("-----ADD MENU-----")
    item_id = input("ENTER ITEM ID")
    item_name = input("ENTER NAME OF THE ITEM")
    price = int(input("ENTER PRICE OF THE ITEM"))
    restaurant[item_id] = {"item_name": item_name, "price" : price}
    print("ITEM ADDED SUCCESSFULLY")

def view_menu() :
  if len(restaurant) == 0:
        print("NO ITEMS IN MENU")
  else:
    print("-----VIEW MENU-----")
    for item_id, details in restaurant.items():
      print("Item ID:",item_id)
      print(f"{details['item_name']}: {details['price']}")


def order_menu() :
    print("-----ORDER MENU-----")
    if len(restaurant) == 0:
        print("NO ITEMS IN MENU")
        return
    else :

        print("-----ORDER MENU-----")
        item_id = input("ENTER ITEM ID")
        if item_id in restaurant:
            quantity = int(input("ENTER QUANTITY: "))
            order[item_id] = quantity
            print("ORDER PLACED SUCCESSFULLY")
        else:
            print("INVALID ITEM ID! THIS ITEM DOES NOT EXIST.")
def bill():
  for item_id, details in restaurant.items():
    print("-----BILL-----")
    total_bill = 0
    for item_id, quantity in order.items():
        item_details = restaurant[item_id]
        item_name = item_details["item_name"]
        price = item_details["price"]
        item_total = price * quantity
        total_bill += item_total

        print(f"{item_name} x {quantity} = ${item_total}")

    print("--------------------")
    print(f"TOTAL AMOUNT: {total_bill}")

while True :
    print("-----RESTAURANT MANAGEMENT SYSTEM-----")
    print("1. ADD MENU")
    print("2. VIEW MENU")
    print("3. ORDER MENU")
    print("4. BILL")
    print("5. EXIT")
    choice = input("ENTER YOUR CHOICE")
    if choice == "1":
        add_menu()
    elif choice == "2":
        view_menu()
    elif choice == "3":
        order_menu()
    elif choice == "4":
        bill()
    elif choice == "5":
        print("THANK YOU FOR VISITING US")
        break
    else :
        print("INVALID CHOICE")
