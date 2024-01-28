# practice from 2 to 40
inventory = {}

def add_item(item, quantity):
    if item in inventory:
        quantity = + quantity
    else:
        quantity == quantity

def view_inventory():
    for x, y in inventory:
        print("name", "quantity")

def update_item(item, quantity):
    if item in inventory:
        quantity = + quantity
    elif item not in inventory:
        print("it;s not found")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
        if choice == "1":
            print(input("Enter an item name and quantity"))
            add_item
        elif choice == "2":
            view_inventory
        elif choice == "3":
            print(input("Enter an item name and new quantity"))
            update_item
        elif choice == "4":
            break
        else:
            print("Error message, please try it again") 
manage_inventory()

# improvement from 44 to 95 

inventory = {}


def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity  # 库存数量更新 # 字典中用[]来访问keys and values
    else:
        inventory[item] = quantity  # 添加进库存
    print(f"Added{quantity} {item}(s).")


def view_inventory():
    for item, quantity in inventory.items():  # .items()用于访问key and value
        # 如果item和quantity 加了“” 只能打印出item 和quantity这两个词
        print(f"{item}:{quantity}")


def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated{item} quantity to {quantity}.")
    else:                         # elif 是错误的，因为if已经包括了所有的情况
        print(f"{item} not found in inventory.")  # print(f"{} {}")


def manage_inventory():
    while True:
        print("\nInventory Management System")  # \n 换行用法 \n\n
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("Enter an item name: ")
            quantity = int(input("Enter an item quantity: "))
            add_item(item, quantity)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            item = input("Enter an item name: ")
            quantity = int(input("Enter the new quantity: "))
            update_item(item, quantity)
        elif choice == "4":
            print("Exiting Inventory Management Inventory.")
            break
        else:
            print("Error message, please try it again")


manage_inventory()
