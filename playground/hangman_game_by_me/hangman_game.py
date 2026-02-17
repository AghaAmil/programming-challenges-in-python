import random

from word_database import WORDS

LIVES = 6


# computer chosen word
chosen_word = random.choice(WORDS)


print("\nWELCOME TO HANGMAN")
print("==================================================")

# to check
print(chosen_word)
print()


# user guessed letters as an empty set
# set is used as it removes the duplicate letters
guessed_letters = set()


while True:
    # display the word with the guessed letters
    displayed_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"

    print(f"Word: {displayed_word}")
    print(f"Number Wrong Guesses: {LIVES}")

    user_guess = input("Enter a letter: ").lower()

    guessed_letters.add(user_guess)

    if user_guess not in chosen_word:
        print("Wrong letter is guessed")
        LIVES -= 1
    else:
        print("Nice Job")

    if displayed_word == chosen_word:
        print("You Win!")
        break

    if LIVES == 0:
        print("You Lost!")
        break
