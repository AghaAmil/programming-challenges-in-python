import os
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


def clear_screen():
    """
    Clear the terminal screen between rounds.
    """
    # 'nt' is for Windows, others are typically Unix-based (Linux, macOS)
    os.system("cls" if os.name == "nt" else "clear")


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
    """
    card, _ = random_card_generator()
    hand.append(card)


def deal_initial_cards(player_hand, dealer_hand):
    """
    Deal two cards to player and dealer to start the game.

    :param player_hand: List of card labels for the player
    :param dealer_hand: List of card labels for the dealer
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

    while total_score > 21 and aces > 0:
        total_score -= 10
        aces -= 1
    return total_score


def game_result(player_hand, dealer_hand):
    """
    Compare player and dealer hand values and decide the winner.
    Handles Blackjack, bust, tie, and score comparison cases.

    :param player_hand: List of card labels for the player
    :param dealer_hand: List of card labels for the dealer
    :return:
        str: result message indicating the outcome
    """
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    if player_score == 21 and len(player_hand) == 2 and not (dealer_score == 21 and len(dealer_hand) == 2):
        return "Player Win! with a Blackjack 😎💪🏻"
    elif dealer_score == 21 and len(dealer_hand) == 2 and not (player_score == 21 and len(player_hand) == 2):
        return "Player Lose! Dealer has a Blackjack 😱"
    elif player_score == dealer_score:
        return "It's a tie! 😬"
    elif player_score > 21:
        return "Player Lose! Player went over 21. 😢"
    elif dealer_score > 21:
        return "Player Win! Dealer went over 21. 😈"
    elif player_score > dealer_score:
        return "Player Win! Player has higher score ☺️"
    else:
        return "Player Lose! Dealer has higher score 😔"


def play_blackjack():
    """
    Run a single round of Blackjack. Deals initial cards, handles the
    player's hit/stand decisions, runs the dealer's turn, and displays
    the final result.
    """
    player_hand = []
    dealer_hand = []

    print(LOGO)
    print("=" * 70)

    # first deal card to player and dealer
    deal_initial_cards(player_hand, dealer_hand)

    print(f"    Player Current Hand: {player_hand}         Player Score: {calculate_hand_value(player_hand)}")
    print(f"    Dealer First Card: {dealer_hand[0]}        Dealer Score: {CARD_DECK[dealer_hand[0]]}\n")

    if calculate_hand_value(player_hand) == 21:
        print("Lucky Bastard! Your first hand is a Blackjack!")
    else:
        while True:
            request_card = input("Type 'y' to get another card or type 'n' to pass: ").strip().lower()

            if request_card == "y":
                deal_card(player_hand)
                print(f"    Player Current Hand: {player_hand}         Player Score: {calculate_hand_value(player_hand)}\n")
                if calculate_hand_value(player_hand) > 21:
                    break
            elif request_card == "n":
                break
            else:
                print("Invalid input!! Please type 'y' or 'n' explicitly\n")

    if calculate_hand_value(player_hand) <= 21:
        while calculate_hand_value(dealer_hand) < 17:
            deal_card(dealer_hand)

    # blank line
    print()
    print(f"    Player Final Hand: {player_hand}      Player Score: {calculate_hand_value(player_hand)}")
    print(f"    Dealer Final Hand: {dealer_hand}      Dealer Score: {calculate_hand_value(dealer_hand)}")
    print(game_result(player_hand, dealer_hand))


def main():
    """
    Main function, ask the user to play a game or quit the game.

    :return: Close the program
    """
    play_blackjack()

    while True:
        play_again = input('\nDo you want to play a game of Blackjack? type "y" or "n" : ').strip().lower()
        if play_again == "y":
            clear_screen()
            play_blackjack()
        elif play_again == "n":
            print("\nThank you for playing Blackjack with us! 🫶🏻")
            return
        else:
            print("Invalid input!! Please type 'y' or 'n' explicitly")


if __name__ == "__main__":
    main()
