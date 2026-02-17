import random

user_wins = 0
computer_wins = 0


def game_engine(user, computer):
    user = user.lower()
    computer = computer.lower()

    global user_wins, computer_wins

    if user == computer:
        return 'Draw!'
    elif user == 'paper' and computer == 'rock' or user == 'scissors' and computer == 'paper' or user == 'rock' and computer == 'scissors':
        user_wins += 1
        return 'You Won!'

    else:
        computer_wins += 1
        return 'Computer Won!'


print('Welcome to Rock, Paper, Scissors Game')
print('You will play 5 rounds against our smart computer')
print()

for round in range(1, 5):
    print(f'Round {round}. Fight!')

    user_choice = input('Choose your option (Rock, Paper, Scissors): ')
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    print(f'User Choice: {user_choice}')
    print(f'Computer Choice: {computer_choice}')

    winner = game_engine(user_choice, computer_choice)

    print(f'{user_choice} Vs. {computer_choice} = {winner}')
    print()

print()

if user_wins > computer_wins:
    print(f'You Beat the Computer! {user_wins} Rounds Vs. {computer_wins} Rounds')
elif computer_wins > user_wins:
    print(f'You have Lost! {user_wins} Rounds Vs. {computer_wins} Rounds')
else:
    print('The game ended in a tie!')
