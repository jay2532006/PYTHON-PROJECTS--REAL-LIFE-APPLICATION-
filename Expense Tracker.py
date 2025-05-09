import os

def main_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Save and Exit")
    print("5. Load Expenses from File")

def add_expense(expenses):
    description = input("Enter expense description: ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    expenses.append((description, amount))
    print("Expense added successfully.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
    else:
        print("\nExpenses:")
        for i, (description, amount) in enumerate(expenses, start=1):
            print(f"{i}. {description} - ${amount:.2f}")

def calculate_total(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def save_to_file(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for description, amount in expenses:
            file.write(f"{description},{amount}\n")
    print(f"Expenses saved to {filename}.")

def load_from_file(filename="expenses.txt"):
    expenses = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    description, amount = line.strip().split(",")
                    expenses.append((description, float(amount)))
                except ValueError:
                    print("Error reading line, skipping.")
    else:
        print(f"File {filename} not found.")
    return expenses

def main():
    expenses = load_from_file()
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            save_to_file(expenses)
            print("Exiting program. Goodbye!")
            break
        elif choice == "5":
            expenses = load_from_file()
            print("Expenses loaded successfully.")
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
