import random

from artworks import HANGMAN_STAGES, LOGO
from words_database import WORDS


def get_random_word():
    word = random.choice(WORDS)
    return word


def display_guessing_word(random_word, guessed_letters, wrong_letters, user_lives):

    print("\n" + "=" * 50)
    print(HANGMAN_STAGES[user_lives])
    print("=" * 50)

    word_placeholder = ""

    for letter in random_word:
        if letter == guessed_letters:
            word_placeholder += guessed_letters + " "
        else:
            word_placeholder += "_ "

    print(f"\nWord: {word_placeholder}")
    print(f"Live: {user_lives}/6")
    print(f"Wrong Guessed Letters: {', '.join(sorted(wrong_letters)) if wrong_letters else '-'}")
    print(f"Guessed Letter: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")


def get_user_guess(guessed_letters):

    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter only one letter")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try a different letter.")
        else:
            return guess


def play_hangman():
    # Main game logic
    # decoration
    print(f"{LOGO}")
    print("\n" + "=" * 50)
    print("              WELCOME TO HANGMAN!")
    print("=" * 50)
    print("\nGuess the word one letter at a time.")
    print("You have 6 lives or wrong guesses before you lose!")

    random_word = get_random_word()
    guessed_letters = set()
    wrong_letters = set()
    user_lives = 6

    while user_lives != 0:
        print(random_word)
        display_guessing_word(random_word, guessed_letters, wrong_letters, user_lives)

        # check if the user guessed all the letters correctly
        if all(letter in guessed_letters for letter in random_word):
            print("\n" + "=" * 50)
            print(f"🎉 CONGRATULATIONS! You won! The word was: {random_word}")
            print("=" * 50)
            return True

        # get player's guess
        user_guess = get_user_guess(guessed_letters)
        guessed_letters.add(user_guess)

        if user_guess in random_word:
            print(f"Correct Guess! {user_guess} is in the hidden word!")
        else:
            print(f"Sorry! {user_guess} is not in the hidden word.")
            wrong_letters.add(user_guess)
            user_lives -= 1

    # game-over state
    display_guessing_word(random_word, guessed_letters, wrong_letters)
    print("\n" + "=" * 50)
    print("💀 GAME OVER! You ran out of guesses.")
    print(f"The word was: {random_word}")
    print("=" * 50)
    return False


def main():

    while True:
        play_hangman()

        # Ask if the player wants to play again
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
