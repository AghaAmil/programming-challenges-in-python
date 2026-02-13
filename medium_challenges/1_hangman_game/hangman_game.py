import random

from artworks import HANGMAN_STAGES, LOGO
from words_database import WORDS


def game_start_message():
    # """Display welcome banner and instructions to the user."""
    print(f"{LOGO}\n")
    print("=" * 50)
    print(" Welcome to the Hangman Guessing Game")
    print("=" * 50)


def word_selection():
    word = random.choice(WORDS)
    return word


def main():
    game_start_message()

    guessing_word = word_selection()
    # testing purposes
    print(guessing_word)

    word_placeholder = ""
    for letter in guessing_word:
        word_placeholder += "- "

    print(f"Word to Guess: {word_placeholder}")

    user_guess = input("Guess a letter: ").strip().lower()


if __name__ == "__main__":
    main()
