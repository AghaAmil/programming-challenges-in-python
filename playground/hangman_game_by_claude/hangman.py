#!/usr/bin/env python3
"""
Simple Hangman Word Guessing Game
Run this file to play Hangman in the terminal!
"""

import random


# Hangman visual stages
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |     
       |      
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |     
       |      
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     
    ---|---
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
    ---|---
    """
]

# Word list for the game
WORD_LIST = [
    "python", "programming", "computer", "algorithm", "function",
    "variable", "database", "internet", "keyboard", "software",
    "hardware", "network", "terminal", "developer", "interface",
    "application", "framework", "library", "module", "package"
]


class HangmanGame:
    """Main Hangman game class"""
    
    def __init__(self, word_list=WORD_LIST):
        self.word_list = word_list
        self.max_attempts = len(HANGMAN_STAGES) - 1
        self.reset_game()
    
    def reset_game(self):
        """Reset game state for a new round"""
        self.secret_word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = self.max_attempts
        self.is_won = False
        self.is_lost = False
    
    def get_display_word(self):
        """Return the word with unguessed letters as underscores"""
        return ' '.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.secret_word
        )
    
    def get_hangman_stage(self):
        """Return current hangman visual based on wrong attempts"""
        wrong_attempts = self.max_attempts - self.attempts_left
        return HANGMAN_STAGES[wrong_attempts]
    
    def guess_letter(self, letter):
        """Process a letter guess"""
        letter = letter.upper()
        
        # Check if already guessed
        if letter in self.guessed_letters:
            return "already_guessed"
        
        # Add to guessed letters
        self.guessed_letters.add(letter)
        
        # Check if letter is in word
        if letter in self.secret_word:
            # Check if word is complete
            if all(letter in self.guessed_letters for letter in self.secret_word):
                self.is_won = True
            return "correct"
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.is_lost = True
            return "wrong"
    
    def get_sorted_guessed_letters(self):
        """Return sorted list of guessed letters"""
        return ', '.join(sorted(self.guessed_letters))
    
    def display_game_state(self):
        """Display current game state"""
        print("\n" + "=" * 50)
        print(self.get_hangman_stage())
        print("=" * 50)
        print(f"\nWord: {self.get_display_word()}")
        print(f"Attempts left: {self.attempts_left}")
        if self.guessed_letters:
            print(f"Guessed letters: {self.get_sorted_guessed_letters()}")
        print("=" * 50)


def get_valid_letter_input():
    """Get and validate letter input from user"""
    while True:
        user_input = input("\nGuess a letter: ").strip()
        
        if len(user_input) != 1:
            print("❌ Please enter exactly one letter.")
            continue
        
        if not user_input.isalpha():
            print("❌ Please enter a letter (A-Z).")
            continue
        
        return user_input.upper()


def play_hangman():
    """Main game loop"""
    print("\n" + "🎮" * 25)
    print("     WELCOME TO HANGMAN - WORD GUESSING GAME!")
    print("🎮" * 25 + "\n")
    
    game = HangmanGame()
    
    while True:
        # Display current game state
        game.display_game_state()
        
        # Check if game is over
        if game.is_won:
            print("\n🎉 " + "=" * 46 + " 🎉")
            print("     CONGRATULATIONS! You guessed the word!")
            print(f"     The word was: {game.secret_word}")
            print("🎉 " + "=" * 46 + " 🎉\n")
            break
        
        if game.is_lost:
            print("\n💀 " + "=" * 46 + " 💀")
            print("     GAME OVER! You ran out of attempts.")
            print(f"     The word was: {game.secret_word}")
            print("💀 " + "=" * 46 + " 💀\n")
            break
        
        # Get letter guess
        letter = get_valid_letter_input()
        result = game.guess_letter(letter)
        
        # Provide feedback
        if result == "already_guessed":
            print(f"⚠️  You already guessed '{letter}'. Try a different letter.")
        elif result == "correct":
            print(f"✅ Great! '{letter}' is in the word!")
        elif result == "wrong":
            print(f"❌ Sorry, '{letter}' is not in the word.")
    
    # Ask to play again
    while True:
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            game.reset_game()
            play_hangman()
            break
        elif play_again in ['no', 'n']:
            print("\n👋 Thanks for playing! Goodbye!\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    try:
        play_hangman()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")
