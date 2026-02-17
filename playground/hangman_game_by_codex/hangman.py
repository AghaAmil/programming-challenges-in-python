import random

WORDS = [
    "python",
    "developer",
    "hangman",
    "terminal",
    "function",
    "variable",
    "computer",
    "keyboard",
    "program",
    "algorithm",
]

MAX_WRONG_GUESSES = 6


HANGMAN_STAGES = [
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


def choose_word() -> str:
    return random.choice(WORDS)


def display_progress(word: str, guessed_letters: set[str]) -> str:
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game() -> None:
    word = choose_word()
    guessed_letters: set[str] = set()
    wrong_guesses = 0

    print("\nWelcome to Hangman Guessing Word!\n")

    while True:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_progress(word, guessed_letters)}")

        wrong_letters = sorted(letter for letter in guessed_letters if letter not in word)
        print(f"Wrong letters: {' '.join(wrong_letters) if wrong_letters else '-'}")
        print(f"Remaining lives: {MAX_WRONG_GUESSES - wrong_guesses}\n")

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess!\n")
        else:
            print("Nice guess!\n")

        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"Word: {display_progress(word, guessed_letters)}")
            print(f"You won! The word was '{word}'.\n")
            break

        if wrong_guesses >= MAX_WRONG_GUESSES:
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"You lost! The word was '{word}'.\n")
            break


def main() -> None:
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
