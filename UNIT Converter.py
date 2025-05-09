def convert_length():
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")
    choice = int(input("Choose conversion type: "))
    value = float(input("Enter value to convert: "))
    
    if choice == 1:
        print(f"{value} miles is equal to {value * 1.60934} kilometers.")
    elif choice == 2:
        print(f"{value} kilometers is equal to {value / 1.60934} miles.")
    else:
        print("Invalid choice.")

def convert_weight():
    print("1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    choice = int(input("Choose conversion type: "))
    value = float(input("Enter value to convert: "))
    
    if choice == 1:
        print(f"{value} pounds is equal to {value * 0.453592} kilograms.")
    elif choice == 2:
        print(f"{value} kilograms is equal to {value / 0.453592} pounds.")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Choose conversion type: "))
    value = float(input("Enter value to convert: "))
    
    if choice == 1:
        print(f"{value} Celsius is equal to {(value * 9/5) + 32} Fahrenheit.")
    elif choice == 2:
        print(f"{value} Fahrenheit is equal to {(value - 32) * 5/9} Celsius.")
    else:
        print("Invalid choice.")

def unit_converter():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        category = int(input("Choose category to convert: "))
        
        if category == 1:
            convert_length()
        elif category == 2:
            convert_weight()
        elif category == 3:
            convert_temperature()
        elif category == 4:
            print("Exiting the unit converter.")
            break
        else:
            print("Invalid choice.")

unit_converter()
