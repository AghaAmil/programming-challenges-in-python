import random

from art import LOGO

CARD_DECK = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def random_card_generator():
    """
    Generate a random card deck with its corresponding value

    :return:
        string: a random card deck from CARD_DECK
        int: the card value
    """
    return random.choice(list(CARD_DECK.items()))


def deal_card(hand):
    """
    Draw one card and append it to the given hand.

    :param hand: List of card labels
    :return:
        str: card label
        int: card value
    """
    card, value = random_card_generator()
    hand.append(card)

    return card, value


def deal_initial_cards(player_hand, dealer_hand):
    """
    Deal two cards to player and dealer to start the game.
    """
    for _ in range(2):
        deal_card(player_hand)
        deal_card(dealer_hand)


def calculate_hand_value(hand):
    """
    Calculate the player/dealer hand value

    :param hand: List of card labels
    :return:
        int: hand value
    """
    total_score = sum(CARD_DECK[card] for card in hand)
    aces = hand.count("A")

    if total_score > 21 and aces > 0:
        total_score -= 10
        aces -= 1
    return total_score


def game_result(player_hand, dealer_hand):
    """
    Check player and dealer hand value and decide the winner

    :param player_hand:
    :param dealer_hand:
    :return:
    """
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    if player_score == dealer_score:
        return "It's a tie! 😬"
    elif player_score == 21:
        return "Player Win! with a Blackjack 😎💪🏻"
    elif dealer_score == 21:
        return "Player Lose! Dealer has a Blackjack 😱"
    elif player_score > 21:
        return "Player Lose! Player went over 21. 😢"
    elif dealer_score > 21:
        return "Player Win! Dealer went over 21. 😈"
    elif player_score > dealer_score:
        return "Player Win! Player has higher score ☺️"
    else:
        return "Player Lose! Dealer has higher score 😔"


def blackjack_game():
    """
    Run the Blackjack game and display the result

    :return:
    """
    player_hand = []
    dealer_hand = []

    player_score = 0
    dealer_score = 0

    print(LOGO)
    print("=" * 80)

    # first deal card to player and dealer
    deal_initial_cards(player_hand, dealer_hand)

    while True:
        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        # display initial card dealing
        print(f"    Player Current Hand: {player_hand}         Player Score: {player_score}")
        print(f"    Dealer First Card: {dealer_hand[0]}        Dealer Score: {CARD_DECK[dealer_hand[0]]}\n")

        if player_score == 21 and dealer_score != 21:
            print("Lucky Bastard! Your first hand is a Blackjack!")

            break

        request_card = input("Type 'y' to get another card or type 'n' to pass: ").strip().lower()

        if request_card == "y":
            deal_card(player_hand)
        elif request_card == "n":
            break
        else:
            print("Invalid input!! Please type 'y' or 'n' explicitly\n")

    while dealer_score < 17:
        deal_card(dealer_hand)

    # blank line
    print()
    print(f"    Player Final Hand: {player_hand}      Player Score: {player_score}")
    print(f"    Dealer Final Hand: {dealer_hand}      Dealer Score: {dealer_score}")
    print(game_result(player_hand, dealer_hand))


def main():
    """
    Main function, ask the user to play a game or quit the game.

    :return: Close the program
    """
    while True:
        play_again = input('\nDo you want to play a game of Blackjack? type "y" or "n" : ').strip().lower()
        if play_again == "y":
            blackjack_game()
        elif play_again == "n":
            print("Thank you for playing Blackjack with us!")
            return
        else:
            print("Invalid input!! Please type 'y' or 'n' explicitly")


if __name__ == "__main__":
    main()
