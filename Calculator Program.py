import math

def display_menu():
    print("\n" + "=" * 40)
    print("           Welcome to Simple Calculator")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Exponentiation (^)")
    print("7. Exit")
    print("=" * 40)

def get_numbers(count):
    numbers = []
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return numbers

def calculator():
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-7): "))
            if choice == 7:
                print("Thank you for using Simple Calculator. Goodbye!")
                break
            elif choice not in range(1, 8):
                print("Invalid choice. Please select a valid option.")
                continue

            if choice in [1, 2, 3, 4]:
                count = int(input("How many numbers do you want to input? "))
                if count < 2:
                    print("You need at least 2 numbers for this operation.")
                    continue
                numbers = get_numbers(count)

                if choice == 1:
                    result = sum(numbers)
                    print("Result (Addition):", result)
                elif choice == 2:
                    result = numbers[0]
                    for num in numbers[1:]:
                        result -= num
                    print("Result (Subtraction):", result)
                elif choice == 3:
                    result = 1
                    for num in numbers:
                        result *= num
                    print("Result (Multiplication):", result)
                elif choice == 4:
                    result = numbers[0]
                    try:
                        for num in numbers[1:]:
                            result /= num
                        print("Result (Division):", result)
                    except ZeroDivisionError:
                        print("Error: Division by zero is not allowed.")

            elif choice == 5:
                num = float(input("Enter the number: "))
                if num < 0:
                    print("Error: Square root of negative numbers is not supported.")
                else:
                    print("Result (Square Root):", math.sqrt(num))

            elif choice == 6:
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print("Result (Exponentiation):", math.pow(base, exponent))

        except ValueError:
            print("Invalid input. Please enter numbers only.")


calculator()
