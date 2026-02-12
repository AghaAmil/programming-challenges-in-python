"""
Blind Auction Program - First-price Sealed-bid Auction
A command-line application where multiple bidders can submit their bids anonymously,
and the highest bidder wins the auction.
"""

import os

from art import LOGO


# Dictionary to store all bidders and their respective bid values
bidder_info = {}


def display_welcome_message():
    # """Display welcome banner and instructions to the user."""
    print(f"{LOGO}\n")
    print("=" * 70)
    print("  Welcome to the First-Price Sealed-Bid Auction Program")
    print("=" * 70)
    print("\n📋 Instructions:")
    print("   • Enter your name and bid amount")
    print("   • Your bid will remain hidden from other participants")
    print("   • The highest bidder wins the auction!\n")
    print("-" * 70)


def winner_selection(bidders):
    """
    Determine the auction winner using Python's built-in max function.
    
    Args:
        bidders (dict): Dictionary containing bidder names as keys and bid amounts as values
        
    Returns:
        tuple: A tuple containing (winner_name, winning_bid)
    """
    # This finds the pair with the highest value and unpacks it
    # It returns a tuple like ('Name', 100)
    auction_winner, winner_bid = max(bidders.items(), key=lambda item: item[1])
    return auction_winner, winner_bid


def winner_selection_legacy(bidders):
    """
    Determine the auction winner using traditional iteration (legacy method).
    
    Args:
        bidders (dict): Dictionary containing bidder names as keys and bid amounts as values
        
    Returns:
        tuple: A tuple containing (winner_name, winning_bid)
    """
    winner_name = ""
    highest_bid = 0
    
    for bidder_name in bidders:
        if bidders[bidder_name] > highest_bid:
            highest_bid = bidders[bidder_name]
            winner_name = bidder_name
    
    return winner_name, highest_bid


def bid_collection():
    """
    Collect bidder information (name and bid amount) with input validation.
    
    Returns:
        bool: True if bid was collected successfully, False otherwise
    """
    try:
        print("\n💰 New Bidder Registration")
        print("-" * 70)
        
        # Get and validate user name
        user_name = input("Enter your name: ").strip()
        if not user_name:
            print("❌ Error: Name cannot be empty!")
            return False
        
        if user_name in bidder_info:
            print(f"⚠️  Warning: {user_name} has already placed a bid. Updating bid amount...")
        
        # Get and validate bid amount
        user_bid_input = input("Enter your bid: $").strip()
        user_bid = int(user_bid_input)
        
        if user_bid <= 0:
            print("❌ Error: Bid amount must be greater than $0!")
            return False
        
        # Store the bid
        bidder_info[user_name] = user_bid
        print(f"✅ Bid registered successfully for {user_name}!")
        
        return True
        
    except ValueError:
        print("❌ Error: Please enter a valid numeric bid amount!")
        return False
    except KeyboardInterrupt:
        print("\n\n⚠️  Auction cancelled by user.")
        return False


def clear_screen():
    """Clear the terminal screen for privacy between bidders."""
    # 'nt' is for Windows, others are typically Unix-based (Linux, macOS)
    os.system("cls" if os.name == "nt" else "clear")


def display_winner(winner_name, winning_bid):
    """
    Display the auction winner in a formatted manner.
    
    Args:
        winner_name (str): Name of the winning bidder
        winning_bid (int): Winning bid amount
    """
    print("\n")
    print("=" * 70)
    print("  🎉 AUCTION RESULTS 🎉")
    print("=" * 70)
    print(f"\n🏆 Winner: {winner_name}")
    print(f"💵 Winning Bid: ${winning_bid:,}")
    print(f"\n🎊 Congratulations to {winner_name}!")
    print("\n" + "=" * 70)


def main():
    """Main function to run the blind auction program."""
    display_welcome_message()
    
    # Collect the first bid
    if not bid_collection():
        print("\n❌ Auction terminated due to invalid input.")
        return
    
    # Continue collecting bids from additional bidders
    while True:
        print("\n" + "-" * 70)
        new_bidder = input("\nAre there any other bidders? Type 'yes' or 'no': ").strip().lower()
        
        if new_bidder in ["yes", "y"]:
            # Clear CLI interface to hide previous bidders' information
            clear_screen()
            display_welcome_message()
            print(f"\n📊 Total bidders so far: {len(bidder_info)}")
            
            if not bid_collection():
                print("\n⚠️  Skipping this bidder due to invalid input...")
                
        elif new_bidder in ["no", "n"]:
            # Auction complete - determine and display the winner
            if not bidder_info:
                print("\n❌ No valid bids were placed. Auction cancelled.")
                return
            
            # Using the optimized max() method
            winner, bid = winner_selection(bidder_info)
            display_winner(winner, bid)
            
            # Alternative: using legacy method (uncomment to use)
            # winner, bid = winner_selection_legacy(bidder_info)
            # display_winner(winner, bid)
            
            break
        else:
            print("❌ Invalid input! Please type 'yes' or 'no'.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Auction terminated by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please try running the program again.")
