import random

def game_instructions():
    print("""
Welcome to the Hangman Game!
----------------------------
How the Game Works:
1. A word will be selected based on the difficulty level you choose.
2. You have to guess the word by suggesting letters.
3. For every wrong guess, a part of the hangman is drawn.
4. The game ends if you either guess the word correctly or the hangman is fully drawn.

Difficulty Levels:
- Easy: Words are shorter and you have more chances.
- Moderate: Words are longer with moderate chances.
- Hard: Words are difficult and you have fewer chances.

Commands:
- Enter a single letter to guess.
- You can enter the full word if you're confident.

Win Condition:
- Guess the word before the hangman is fully drawn.

Good luck, and have fun!
""")

def choose_word(difficulty):
    easy_words = ["cat", "dog", "sun", "fish", "milk"]
    moderate_words = ["python", "flower", "castle", "rocket", "planet"]
    hard_words = ["xylophone", "drought", "zeppelin", "algorithm", "quizzical"]
    
    if difficulty == "easy":
        return random.choice(easy_words)
    elif difficulty == "moderate":
        return random.choice(moderate_words)
    elif difficulty == "hard":
        return random.choice(hard_words)

def display_hangman(wrong_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[wrong_guesses])

def play_hangman():
    game_instructions()
    difficulty = input("\nSelect a difficulty level (easy/moderate/hard): ").lower()
    while difficulty not in ["easy", "moderate", "hard"]:
        print("Invalid choice. Please choose 'easy', 'moderate', or 'hard'.")
        difficulty = input("Select a difficulty level: ").lower()

    word = choose_word(difficulty)
    word_length = len(word)
    guessed_word = ["_"] * word_length
    wrong_guesses = 0
    guessed_letters = []
    max_attempts = 6  # Maximum wrong guesses allowed

    print(f"\nThe word has {word_length} letters. Good luck!")
    while wrong_guesses < max_attempts and "_" in guessed_word:
        display_hangman(wrong_guesses)
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Enter a letter or the full word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word:
                print(f"Good job! '{guess}' is in the word.")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                guessed_letters.append(guess)
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                wrong_guesses += 1
                guessed_letters.append(guess)
        elif len(guess) == word_length:
            if guess == word:
                guessed_word = list(word)
                break
            else:
                print("Incorrect guess!")
                wrong_guesses += 1
        else:
            print("Invalid input. Please enter a single letter or the full word.")

    display_hangman(wrong_guesses)
    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
    else:
        print(f"Game over! The correct word was: {word}")

play_hangman()
