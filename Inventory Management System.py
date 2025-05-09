import json
import os

def instructions():
    print("""
Welcome to the Inventory Management System
------------------------------------------
Features and How to Use:
1. Admin:
   - Create and manage user profiles (Admin password required).
   - Add, view, update, or delete items in the inventory.
   - View the most sold category.
   - Check for items that need restocking (quantity < 100).
2. User:
   - Add details and update inventory quantities only.
3. All actions update and save the inventory file automatically.

Default Credentials:
- Admin: Username: admin, Password: admin123
- User: Username: user, Password: user123

Instructions:
- Admin can manage user accounts and have full access.
- Users can only modify existing inventory details.

Enjoy using the system!
""")

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            return json.load(file)
    return {}

def admin_login():
    password = input("Enter Admin Password: ")
    return password == "admin123"

def create_user(users):
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists!")
        return
    users[username] = {"role": "user", "password": "user123"}
    print(f"User '{username}' created with default password 'user123'.")
    save_users(users)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    return {"admin": {"role": "admin", "password": "admin123"}, "user": {"role": "user", "password": "user123"}}

def add_item(inventory):
    item_name = input("Enter item name: ").capitalize()
    category = input("Enter category: ").capitalize()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    if item_name in inventory:
        print("Item already exists. Use 'update quantity' instead.")
        return
    inventory[item_name] = {"category": category, "quantity": quantity, "price": price, "sold": 0}
    print(f"Item '{item_name}' added successfully.")
    save_inventory(inventory)

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        print(f"{item}: {details}")
    print()

def update_item(inventory):
    item_name = input("Enter the item name to update: ").capitalize()
    if item_name not in inventory:
        print("Item not found!")
        return
    quantity = int(input("Enter new quantity: "))
    inventory[item_name]["quantity"] = quantity
    print(f"Item '{item_name}' updated successfully.")
    save_inventory(inventory)

def most_sold_category(inventory):
    category_sales = {}
    for item, details in inventory.items():
        category = details["category"]
        category_sales[category] = category_sales.get(category, 0) + details["sold"]
    if category_sales:
        most_sold = max(category_sales, key=category_sales.get)
        print(f"The most sold category is '{most_sold}' with {category_sales[most_sold]} items sold.")
    else:
        print("No sales data available.")

def restock_reminder(inventory):
    print("\nRestock Reminder:")
    for item, details in inventory.items():
        if details["quantity"] < 100:
            print(f"Item '{item}' needs restocking (Current Quantity: {details['quantity']}).")

def admin_menu(inventory, users):
    while True:
        print("\nAdmin Menu")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Create User")
        print("5. Most Sold Category")
        print("6. Restock Reminder")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            create_user(users)
        elif choice == "5":
            most_sold_category(inventory)
        elif choice == "6":
            restock_reminder(inventory)
        elif choice == "7":
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice. Try again.")

def user_menu(inventory):
    while True:
        print("\nUser Menu")
        print("1. View Inventory")
        print("2. Update Item Quantity")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            print("Exiting User Menu.")
            break
        else:
            print("Invalid choice. Try again.")

def inventory_management_system():
    instructions()
    inventory = load_inventory()
    users = load_users()

    username = input("Enter username: ")
    if username not in users:
        print("Invalid username!")
        return
    password = input("Enter password: ")
    if password != users[username]["password"]:
        print("Incorrect password!")
        return

    if users[username]["role"] == "admin":
        if admin_login():
            admin_menu(inventory, users)
        else:
            print("Invalid admin password!")
    elif users[username]["role"] == "user":
        user_menu(inventory)

inventory_management_system()
