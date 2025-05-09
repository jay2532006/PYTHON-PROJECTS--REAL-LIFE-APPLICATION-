import os
import json

def password_protect():
    password = "1234"
    user_password = input("Enter the password to access the Expense Tracker: ")
    if user_password != password:
        print("Incorrect password! Exiting...")
        exit()

def save_data(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_data():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return {}

def add_expense(expenses):
    category = input("Enter the category (e.g., Food, Transportation, etc.): ").capitalize()
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    if category not in expenses:
        expenses[category] = []
    expenses[category].append({"date": date, "amount": amount})
    print("Expense added successfully!")
    save_data(expenses)

def view_expenses(expenses):
    category = input("Enter the category to view expenses: ").capitalize()
    if category in expenses:
        print(f"\nExpenses for category: {category}")
        for expense in expenses[category]:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}")
    else:
        print("No expenses found for this category.")

def calculate_totals(expenses):
    print("\nTotal expenses by category:")
    for category, entries in expenses.items():
        total = sum(entry["amount"] for entry in entries)
        print(f"{category}: {total}")

def monthwise_review(expenses):
    month_totals = {}
    for category, entries in expenses.items():
        for expense in entries:
            month = expense["date"][:7]
            month_totals[month] = month_totals.get(month, 0) + expense["amount"]
    print("\nMonth-wise review:")
    for month, total in month_totals.items():
        print(f"{month}: {total}")

def yearwise_review(expenses):
    year_totals = {}
    for category, entries in expenses.items():
        for expense in entries:
            year = expense["date"][:4]
            year_totals[year] = year_totals.get(year, 0) + expense["amount"]
    print("\nYear-wise review:")
    for year, total in year_totals.items():
        print(f"{year}: {total}")

def most_spent_category(expenses):
    max_category = None
    max_amount = 0
    for category, entries in expenses.items():
        total = sum(entry["amount"] for entry in entries)
        if total > max_amount:
            max_category = category
            max_amount = total
    print(f"\nMost spent category: {max_category} with a total of {max_amount}.")

def reminder_to_save(expenses):
    total_expenses = sum(
        entry["amount"] for category, entries in expenses.items() for entry in entries
    )
    budget = float(input("\nEnter your monthly budget: "))
    if total_expenses > budget:
        print("You have exceeded your budget. Consider saving more!")
    else:
        print("You are within your budget. Keep saving!")

def savings_tracker():
    savings = float(input("Enter your total savings amount: "))
    goal = float(input("Enter your savings goal: "))
    if savings >= goal:
        print(f"Congratulations! You've reached your savings goal of {goal}.")
    else:
        print(f"You need {goal - savings} more to reach your savings goal. Keep saving!")

def expense_tracker():
    password_protect()
    expenses = load_data()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add an expense")
        print("2. View expenses by category")
        print("3. Calculate total expenses by category")
        print("4. Month-wise review")
        print("5. Year-wise review")
        print("6. Most spent category")
        print("7. Reminder to save money")
        print("8. Savings tracker")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_totals(expenses)
        elif choice == "4":
            monthwise_review(expenses)
        elif choice == "5":
            yearwise_review(expenses)
        elif choice == "6":
            most_spent_category(expenses)
        elif choice == "7":
            reminder_to_save(expenses)
        elif choice == "8":
            savings_tracker()
        elif choice == "9":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

expense_tracker()
