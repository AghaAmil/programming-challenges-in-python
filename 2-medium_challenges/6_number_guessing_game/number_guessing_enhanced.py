import os
import random

from art import LOGO

"""
1. generate a random number between 1 and 100
2. select the game difficulty - easy: 10 / hard: 5
3. guessed value higher than the selected number: Too High
4. guessed value lower than the selected number: Too Low
5. winner if can guess the number before the limit
6. lose if can't guess the number within the limit

"""


def clear_screen():
    """
    Clear the terminal screen between rounds.

    """
    # 'nt' is for Windows, others are typically Unix-based (Linux, macOS)
    os.system("cls" if os.name == "nt" else "clear")


def number_generation():
    """
    generate a random number between 1 and 100

    :return:
        int: random number
    """
    number = random.randint(1, 100)
    return number


def game_difficulty():
    """
    game difficulty selection by the user
    easy: 10 attempts to guess the number
    hard: 5 attempts to guess the number

    :return:
        int: number of attempts
    """

    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("⚠️Invalid Input Inserted")


def game_engine(number, guess, attempts):
    if guess > 100 or guess < 1:
        print("⚠️Out of range! Only select a number between 1 and 100")
    elif guess > number:
        print("⬆️Too high!")
        print("Try a lower number!")
        return attempts - 1
    elif guess < number:
        print("⬇️Too low!")
        print("Try a higher number!")
        return attempts - 1
    else:
        print(f"\n🎉🎊Hooray! You've guessed the chosen number. The number was {number}!")

    return None


def play_game():
    """

    :return:
    """

    # game welcome message
    print(LOGO)
    print("\n" + "=" * 36)
    print("Welcome to the Number Guessing Game!")
    print("=" * 36)

    print("\nA number between 1 and 100 was chosen randomly. Guess the number!")

    # random chosen number & game difficulty
    selected_number = number_generation()

    # choosing game difficulty and user's attempts
    user_attempts = game_difficulty()

    print(selected_number)

    while True:
        print(f"\nYou have {user_attempts} attempts remaining to guess the number!")
        user_guess = int(input("    Guess the number: "))

        user_attempts = game_engine(selected_number, user_guess, user_attempts)

        if user_guess == selected_number:
            return None

        if user_attempts == 0:
            print("\n⚠️You couldn't guess the number within the limit! You Lost 😢")
            print(f"The number was {selected_number}")
            return None


def main():
    play_game()

    while True:
        play_again = input('\nDo you want to play a game of Blackjack? type "y" or "n" : ').strip().lower()
        if play_again == "y":
            clear_screen()
            play_game()
        elif play_again == "n":
            print("\nThank you for playing Blackjack with us! 🫶🏻")
            return
        else:
            print("Invalid input!! Please type 'y' or 'n' explicitly")


if __name__ == "__main__":
    main()
