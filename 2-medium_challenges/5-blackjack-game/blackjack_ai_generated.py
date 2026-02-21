import random

from art import LOGO

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["H", "D", "C", "S"]
CARD_VALUES = {
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


def create_shuffled_deck():
    """Create and shuffle a standard 52-card deck.

    Returns:
        list[tuple[str, str]]: Shuffled deck where each card is (rank, suit).
    """
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def draw_card(deck):
    """Draw one card from the deck.

    If the deck is empty, a fresh shuffled deck is created and reused.

    Args:
        deck (list[tuple[str, str]]): Current deck.

    Returns:
        tuple[str, str]: Drawn card as (rank, suit).
    """
    if not deck:
        # Keep the round playable even if cards run out.
        deck.extend(create_shuffled_deck())
    return deck.pop()


def hand_value(hand):
    """Calculate Blackjack score for a hand.

    Aces are initially counted as 11 and converted to 1 as needed to avoid bust.

    Args:
        hand (list[tuple[str, str]]): Cards in hand as (rank, suit).

    Returns:
        int: Final hand score.
    """
    total = sum(CARD_VALUES[rank] for rank, _ in hand)
    ace_count = sum(1 for rank, _ in hand if rank == "A")

    # Reduce Ace values from 11 to 1 until total is safe or no Aces remain.
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def is_blackjack(hand):
    """Check whether a hand is a natural Blackjack.

    Args:
        hand (list[tuple[str, str]]): Cards in hand as (rank, suit).

    Returns:
        bool: True if hand has exactly two cards totaling 21.
    """
    return len(hand) == 2 and hand_value(hand) == 21


def format_hand(hand):
    """Format a hand for display.

    Args:
        hand (list[tuple[str, str]]): Cards in hand as (rank, suit).

    Returns:
        str: Comma-separated card labels (for example: "AH, 10S").
    """
    return ", ".join(f"{rank}{suit}" for rank, suit in hand)


def show_table(player_hand, dealer_hand, hide_dealer_card=True):
    """Print current table state for player and dealer.

    Args:
        player_hand (list[tuple[str, str]]): Player cards.
        dealer_hand (list[tuple[str, str]]): Dealer cards.
        hide_dealer_card (bool): Whether to hide dealer's second card.
    """
    print("\n" + "-" * 60)
    if hide_dealer_card:
        print(f"Dealer hand: {dealer_hand[0][0]}{dealer_hand[0][1]}, ??")
    else:
        print(f"Dealer hand: {format_hand(dealer_hand)} (value: {hand_value(dealer_hand)})")
    print(f"Your hand:   {format_hand(player_hand)} (value: {hand_value(player_hand)})")
    print("-" * 60)


def player_turn(deck, player_hand, dealer_hand):
    """Run player's decision loop until stand, bust, or 21.

    Args:
        deck (list[tuple[str, str]]): Current draw deck.
        player_hand (list[tuple[str, str]]): Player cards.
        dealer_hand (list[tuple[str, str]]): Dealer cards for table display.
    """
    while True:
        if hand_value(player_hand) >= 21:
            break

        choice = input("Hit or stand? Type 'h' or 's': ").strip().lower()
        if choice == "h":
            player_hand.append(draw_card(deck))
            show_table(player_hand, dealer_hand, hide_dealer_card=True)
        elif choice == "s":
            break
        else:
            print("Invalid input. Please type 'h' to hit or 's' to stand.")


def dealer_turn(deck, dealer_hand):
    """Run dealer drawing logic.

    Dealer must draw until the hand value reaches at least 17.

    Args:
        deck (list[tuple[str, str]]): Current draw deck.
        dealer_hand (list[tuple[str, str]]): Dealer cards.
    """
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))


def determine_result(player_hand, dealer_hand):
    """Determine final round outcome text.

    Args:
        player_hand (list[tuple[str, str]]): Player cards.
        dealer_hand (list[tuple[str, str]]): Dealer cards.

    Returns:
        str: Human-readable result message.
    """
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack and dealer_blackjack:
        return "Push. Both have Blackjack."
    if player_blackjack:
        return "You win with a Blackjack."
    if dealer_blackjack:
        return "You lose. Dealer has Blackjack."
    if player_score > 21:
        return "You bust. Dealer wins."
    if dealer_score > 21:
        return "Dealer busts. You win."
    if player_score > dealer_score:
        return "You win."
    if dealer_score > player_score:
        return "You lose."
    return "Push."


def play_round():
    """Play one complete Blackjack round.

    Returns:
        None
    """
    print(LOGO)
    deck = create_shuffled_deck()

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    show_table(player_hand, dealer_hand, hide_dealer_card=True)

    if not is_blackjack(player_hand) and not is_blackjack(dealer_hand):
        player_turn(deck, player_hand, dealer_hand)

    if hand_value(player_hand) <= 21 and not is_blackjack(dealer_hand):
        dealer_turn(deck, dealer_hand)

    show_table(player_hand, dealer_hand, hide_dealer_card=False)
    print(determine_result(player_hand, dealer_hand))


def should_continue():
    """Ask user whether to play another round.

    Returns:
        bool: True if user wants to continue, False otherwise.
    """
    while True:
        choice = input("\nPlay another round? Type 'y' or 'n': ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("Invalid input. Please type 'y' or 'n'.")


def main():
    """Program entry point for CLI gameplay loop.

    Returns:
        None
    """
    print("Welcome to Blackjack.\n")
    while True:
        play_round()
        if not should_continue():
            print("\nThanks for playing.")
            break


if __name__ == "__main__":
    main()
