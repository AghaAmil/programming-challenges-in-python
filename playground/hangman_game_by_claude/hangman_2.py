#!/usr/bin/env python3
"""
Simple Hangman Word Guessing Game
Run this script to play Hangman in the terminal
"""

import random
import string

# Word bank for the game
WORD_LIST = [
    "python",
    "hangman",
    "computer",
    "programming",
    "developer",
    "algorithm",
    "function",
    "variable",
    "keyboard",
    "monitor",
    "software",
    "hardware",
    "internet",
    "database",
    "network",
]

# Hangman ASCII art stages
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]


def get_random_word():
    """Select a random word from the word list"""
    return random.choice(WORD_LIST).upper()


def display_game_state(word, guessed_letters, wrong_guesses):
    """Display the current state of the game"""
    print("\n" + "=" * 50)
    print(HANGMAN_STAGES[len(wrong_guesses)])
    print("=" * 50)

    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"\nWord: {display_word}")
    print(f"\nWrong guesses ({len(wrong_guesses)}/6): {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")


def get_guess(guessed_letters):
    """Get a valid letter guess from the player"""
    while True:
        guess = input("\nEnter a letter: ").upper().strip()

        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess not in string.ascii_uppercase:
            print("Please enter a valid letter (A-Z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_hangman():
    """Main game logic"""
    print("\n" + "=" * 50)
    print("        WELCOME TO HANGMAN!")
    print("=" * 50)
    print("\nGuess the word one letter at a time.")
    print("You have 6 wrong guesses before you lose!")

    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = set()
    max_wrong = 6

    while len(wrong_guesses) < max_wrong:
        display_game_state(word, guessed_letters, wrong_guesses)

        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print(f"🎉 CONGRATULATIONS! You won! The word was: {word}")
            print("=" * 50)
            return True

        # Get player's guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if guess is correct
        if guess in word:
            print(f"✓ Good guess! '{guess}' is in the word!")
        else:
            print(f"✗ Sorry, '{guess}' is not in the word.")
            wrong_guesses.add(guess)

    # Game over - player lost
    display_game_state(word, guessed_letters, wrong_guesses)
    print("\n" + "=" * 50)
    print("💀 GAME OVER! You ran out of guesses.")
    print(f"The word was: {word}")
    print("=" * 50)
    return False


def main():
    """Main function to run the game with replay option"""
    while True:
        play_hangman()

        # Ask if player wants to play again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ["yes", "y"]:
                break
            elif play_again in ["no", "n"]:
                print("\nThanks for playing Hangman! Goodbye! 👋")
                return
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
