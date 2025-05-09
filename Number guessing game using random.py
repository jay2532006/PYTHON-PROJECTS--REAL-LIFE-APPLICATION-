import random

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        return 10
    elif choice == "2":
        return 50
    else:
        return 100

def number_guessing_game():
    max_range = choose_difficulty()
    number_to_guess = random.randint(1, max_range)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input(f"Guess a number between 1 and {max_range}: "))
        attempts += 1

        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

number_guessing_game()
