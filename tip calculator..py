def tip_calculator():
    print("""
Welcome to the Tip Calculator!
------------------------------
Features:
1. Enter your bill amount.
2. Choose a tip percentage (e.g., 10%, 15%, or 20%).
3. Split the bill among multiple people (optional).
4. Get the total amount each person needs to pay, including the tip.
""")
    try:
        bill_amount = float(input("Enter the total bill amount: ₹"))
        while bill_amount <= 0:
            print("Bill amount must be greater than 0.")
            bill_amount = float(input("Enter the total bill amount: ₹"))

        print("\nTip Options:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        tip_choice = int(input("Choose a tip percentage (1, 2, or 3): "))

        if tip_choice == 1:
            tip_percentage = 0.10
        elif tip_choice == 2:
            tip_percentage = 0.15
        elif tip_choice == 3:
            tip_percentage = 0.20
        else:
            print("Invalid choice! Defaulting to 10% tip.")
            tip_percentage = 0.10

        tip_amount = bill_amount * tip_percentage
        total_amount = bill_amount + tip_amount

        split_choice = input("\nDo you want to split the bill? (yes/no): ").strip().lower()
        if split_choice == "yes":
            num_people = int(input("Enter the number of people: "))
            while num_people <= 0:
                print("Number of people must be greater than 0.")
                num_people = int(input("Enter the number of people: "))
            amount_per_person = total_amount / num_people
            print(f"\nTotal Bill Amount (including tip): ₹{total_amount:.2f}")
            print(f"Each person should pay: ₹{amount_per_person:.2f}")
        else:
            print(f"\nTotal Bill Amount (including tip): ₹{total_amount:.2f}")
            print(f"You should pay: ₹{total_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

tip_calculator()
