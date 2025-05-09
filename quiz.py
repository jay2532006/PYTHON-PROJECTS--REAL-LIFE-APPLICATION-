import json

def display_menu():
    print("\n" + "=" * 40)
    print("           Welcome to the Quiz Game")
    print("=" * 40)
    print("1. Sports Quiz")
    print("2. Bollywood Quiz")
    print("3. View High Scores")
    print("4. Exit")
    print("=" * 40)

def load_questions(topic):
    try:
        with open(f"{topic}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Questions file not found.")
        return []

def save_high_score(name, score):
    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{name}: {score}\n")
    except Exception as e:
        print(f"Error saving high score: {e}")

def review_answers(questions, user_answers):
    correct = 0
    print("\nYour Quiz Review:")
    print("=" * 40)
    for i, question in enumerate(questions):
        print(f"Q{i+1}: {question['question']}")
        print(f"Your Answer: {user_answers[i]}")
        print(f"Correct Answer: {question['options'][question['answer'] - 1]}")
        if user_answers[i] == question['options'][question['answer'] - 1]:
            print("Result: Correct")
            correct += 1
        else:
            print("Result: Incorrect")
        print("-" * 40)
    return correct

def save_user_answers(username, questions, user_answers):
    try:
        with open(f"{username}_answers.txt", "w") as file:
            for i, question in enumerate(questions):
                file.write(f"Q{i+1}: {question['question']}\n")
                file.write(f"Your Answer: {user_answers[i]}\n")
                file.write(f"Correct Answer: {question['options'][question['answer'] - 1]}\n")
                file.write("-" * 40 + "\n")
    except Exception as e:
        print(f"Error saving user answers: {e}")

def quiz_game():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "4":
            print("Thank you for playing the Quiz Game. Goodbye!")
            break

        elif choice == "3":
            try:
                with open("high_scores.txt", "r") as file:
                    print("\nHigh Scores:")
                    print(file.read())
            except FileNotFoundError:
                print("No high scores available yet.")
            continue

        elif choice in ["1", "2"]:
            topic = "sports" if choice == "1" else "bollywood"
            questions = load_questions(topic)
            if not questions:
                continue

            username = input("Enter your name: ")
            user_answers = []
            print("\nStarting the Quiz...")
            print("=" * 40)
            
            for i, question in enumerate(questions):
                print(f"Q{i+1}: {question['question']}")
                for j, option in enumerate(question['options'], start=1):
                    print(f"{j}. {option}")

                while True:
                    try:
                        answer = int(input("Your choice (1-4): "))
                        if answer not in range(1, 5):
                            raise ValueError
                        user_answers.append(question['options'][answer - 1])
                        break
                    except ValueError:
                        print("Invalid choice. Please select a number between 1 and 4.")

            correct_answers = review_answers(questions, user_answers)
            save_user_answers(username, questions, user_answers)
            save_high_score(username, correct_answers)

            print(f"\nQuiz Complete! {username}, you got {correct_answers}/{len(questions)} correct.")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    quiz_game()
