import tkinter as tk
from tkinter import messagebox
import random

# Initialize the game
def start_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    guess_button.config(state=tk.NORMAL)
    entry_guess.config(state=tk.NORMAL)
    output_label.config(text="I'm thinking of a number between 1 and 100. Can you guess it?")
    start_button.config(state=tk.DISABLED)
    entry_guess.delete(0, tk.END)

# Process the guess
def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Input", "Please guess a number between 1 and 100.")
        elif guess < target_number:
            output_label.config(text="Too low! Try again.")
        elif guess > target_number:
            output_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Reset the game
def reset_game():
    guess_button.config(state=tk.DISABLED)
    entry_guess.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)
    output_label.config(text="Press 'Start Game' to begin!")
    entry_guess.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x300")

# Game instructions
instructions = tk.Label(window, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
instructions.pack(pady=10)

# Start button
start_button = tk.Button(window, text="Start Game", command=start_game, font=("Arial", 12))
start_button.pack(pady=5)

# Input for guesses
entry_guess = tk.Entry(window, state=tk.DISABLED, font=("Arial", 12))
entry_guess.pack(pady=5)

# Guess button
guess_button = tk.Button(window, text="Guess", command=check_guess, state=tk.DISABLED, font=("Arial", 12))
guess_button.pack(pady=5)

# Output label
output_label = tk.Label(window, text="Press 'Start Game' to begin!", font=("Arial", 12))
output_label.pack(pady=20)

# Reset button
reset_button = tk.Button(window, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=5)

# Run the application
window.mainloop()