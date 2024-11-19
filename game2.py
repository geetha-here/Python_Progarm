import random

def choose_difficulty():
    """Let the player choose the difficulty level."""
    print("Choose difficulty level:")
    print("1. Easy (1 to 20) - 10 attempts")
    print("2. Medium (1 to 50) - 7 attempts")
    print("3. Hard (1 to 100) - 5 attempts")
   
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return 20, 10
            elif choice == 2:
                return 50, 7
            elif choice == 3:
                return 100, 5
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1/2/3).")

def number_guessing_game():
    """The main game function."""
    print("Welcome to the Enhanced Number Guessing Game!")

    # Choose difficulty
    upper_limit, max_attempts = choose_difficulty()

    # Computer selects a random number between 1 and the upper limit
    number_to_guess = random.randint(1, upper_limit)
    attempts = 0
    guessed = False
    incorrect_guesses = 0

    print(f"\nI have selected a number between 1 and {upper_limit}. You have {max_attempts} attempts.")
   
    while attempts < max_attempts and not guessed:
        try:
            player_guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        incorrect_guesses += 1

        # Check the player's guess
        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            guessed = True
       
        # Give a hint after 3 incorrect guesses
        if incorrect_guesses == 3:
            if number_to_guess % 2 == 0:
                print("Hint: The number is even!")
            else:
                print("Hint: The number is odd!")
            incorrect_guesses = 0

    if not guessed:
        print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
