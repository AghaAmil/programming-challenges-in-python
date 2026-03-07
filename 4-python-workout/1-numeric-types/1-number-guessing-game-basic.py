"""
For this exercise:
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
        - Too high
        - Too low
        - Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.
"""

import random


def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input("What is your guess? "))
        if user_guess == answer:
            print(f"Right! The answer is {user_guess}")
            break
        if user_guess < answer:
            print(f"Your guess of {user_guess} is too low!")
        else:
            print(f"Your guess of {user_guess} is too high!")


guessing_game()
