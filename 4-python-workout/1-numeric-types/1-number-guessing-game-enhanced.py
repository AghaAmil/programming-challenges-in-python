import random


def random_number_generator():
    """
    Generate the random number

    :return:
        int: random number
    """
    number = random.randint(0, 100)
    return number


def game_difficulty():
    """
    game difficulty selection by the user
    easy: 10 attempts to guess the number
    hard: 5 attempts to guess the number

    :return:
        int: number of attempts
    """
    EASY_ATTEMPTS = 10
    HARD_ATTEMPTS = 5

    while True:
        # convert user's difficulty to lowercase and remove extra spaces with lower() and strip()
        difficulty = input("\nChoose the game difficulty (easy/hard): ").lower().strip()

        # with error handling
        if difficulty == "easy":
            return EASY_ATTEMPTS
        elif difficulty == "hard":
            return HARD_ATTEMPTS
        else:
            print('Invalid Input! Enter "easy" or "hard" explicitly.')


def guessing_game():
    """
    The main function for our game
    """
    # store the random generated number
    random_number = random_number_generator()

    # game introduction
    print("=" * 50)
    print("*** Welcome To Number Guessing Game ***")
    print("\nA random number between 0 and 100 (inclusive) has been selected. Guess the number to win the game.")
    print("You can choose your difficulty.")
    print("easy: You have 10 attempts to guess the number.")
    print("hard: You have only 5 attempts to guess the number.")
    print("=" * 50)

    # user's attempts
    attempts = game_difficulty()

    # keep getting user's input till the user guess the number within the limit based on difficulty
    while attempts > 0:
        print(f"\n    {attempts} Guess(es) Remained!")
        user_guess = int(input("    Guess the chosen number: "))

        if user_guess == random_number:
            print(f"Guessed Correctly! The Random Number is {random_number}")
            break

        if user_guess < 0 or user_guess > 100:
            print("Out of Range! Enter a correct integer between 0 and 100.")
        elif user_guess > random_number:
            print("Too high. Try again!")
            attempts -= 1
        elif user_guess < random_number:
            print("Too low. Try again!")
            attempts -= 1
        else:
            print("Invalid Input! Enter a correct integer between 0 and 100.")

    print("\nYou couldn't guess within the limit. You lose.")
    print(f"The number was '{random_number}'")


# run the main game
guessing_game()
