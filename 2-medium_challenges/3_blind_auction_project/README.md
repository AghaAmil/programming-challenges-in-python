# 💰 Blind Auction Project

A command-line application implementing a **First-Price Sealed-Bid Auction** system where multiple bidders can submit
their bids anonymously, and the highest bidder wins the auction.

## 📋 Description

In a blind auction (also known as a sealed-bid auction), bidders submit their bids without knowing what other
participants have bid. This program simulates this process by:

- Collecting bids from multiple participants
- Keeping each bid hidden from other bidders (by clearing the screen)
- Determining the winner based on the highest bid amount

## 📖 Project Objectives

1. **Start the Program**: The welcome screen will display with instructions
2. **Enter Your Name**: Provide your name when prompted
3. **Enter Your Bid**: Enter the amount you wish to bid (must be a positive number)
4. **Add More Bidders**:
   - Type `yes` or `y` to add another bidder (screen will clear for privacy)
   - Type `no` or `n` to end the auction and reveal the winner
5. **View Results**: The winner and winning bid amount will be displayed

## 💡 Example Usage

```
===============================================================
  Welcome to the First-Price Sealed-Bid Auction Program
===============================================================

📋 Instructions:
   • Enter your name and bid amount
   • Your bid will remain hidden from other participants
   • The highest bidder wins the auction!

--------------------------------------------------------------

💰 New Bidder Registration
--------------------------------------------------------------
Enter your name: Alice
Enter your bid: $500
✅ Bid registered successfully for Alice!

--------------------------------------------------------------

Are there any other bidders? Type 'yes' or 'no': yes

[Screen clears for next bidder]

💰 New Bidder Registration
--------------------------------------------------------------
Enter your name: Bob
Enter your bid: $750
✅ Bid registered successfully for Bob!

--------------------------------------------------------------

Are there any other bidders? Type 'yes' or 'no': no

===============================================================
  🎉 AUCTION RESULTS 🎉
===============================================================

🏆 Winner: Bob
💵 Winning Bid: $750

🎊 Congratulations to Bob!

===============================================================
```

## 📚 Learning Objectives

### Prerequisites

To complete a simple version of this project, you should know:

- **Variables and Data Types**: Strings, integers, and dictionaries
- **Input/Output**: Using `input()` and `print()` functions
- **Conditionals**: `if`, `elif`, `else` statements
- **Loops**: `while` loops for repeated operations
- **Functions**: Creating and calling basic functions

### Skills to Practice

This challenge will help you practice:

- **Dictionary Operations**: Store and retrieve bidder information
- **Finding Maximum Values**: Determine the highest bid from all entries
- **Input Validation**: Check if user input is valid before processing
- **Control Flow**: Manage program flow with loops and conditions
- **Screen Clearing**: Use the `os` module to clear the terminal

## 🚀 Optional Extensions

### Beginner Level

- **Minimum Bid Amount**: Set a minimum bid requirement (e.g., $10)
- **Bid Confirmation**: Ask users to confirm their bid before submitting
- **Show Participant Count**: Display how many people have bid so far

### Intermediate Level

- **Bid History Display**: Show all bids in sorted order after the auction ends
- **Tie Breaking System**: Handle cases where multiple bidders have the same highest bid
- **Save to File**: Write auction results to a text file for record keeping

---

**Good luck with the project! 🎉**

---

_Challenge Type: Medium_  
_Topics: Dictionaries, User Input, Control Flow, Functions, Input Validation_  
_Estimated Time (with deep research): 20-40 minutes_
