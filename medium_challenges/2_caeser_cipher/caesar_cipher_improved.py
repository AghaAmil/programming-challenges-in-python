"""Caesar Cipher - Improved Version"""

import string
from art import LOGO

# Use Python's built-in constant for cleaner code
ALPHABET = list(string.ascii_lowercase)

# Simple decorative elements
SEPARATOR = "=" * 50


def caesar_cipher(original_text, shift_amount, option):
    """
    Encrypt or decrypt text using Caesar cipher.
    
    Args:
        original_text: The message to transform
        shift_amount: Number of positions to shift
        option: 'encode' or 'decode'
    
    Returns:
        The transformed text
    """
    output_text = ""
    
    # FIX: Handle decode ONCE before the loop, not for every letter
    if option == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in ALPHABET:
            shifted_index = ALPHABET.index(letter) + shift_amount
            shifted_index %= len(ALPHABET)
            output_text += ALPHABET[shifted_index]
        else:
            output_text += letter
    
    return output_text


def get_user_inputs():
    """Get all inputs from user with basic validation."""
    direction = input("\nType 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    message = input("\nType your message:\n").lower()
    
    # Simple error handling for shift input
    try:
        shift = int(input("\nType the shift number:\n"))
    except ValueError:
        print("Invalid number. Using shift of 3 as default.")
        shift = 3
    
    return direction, message, shift


def display_result(result, option):
    """Display the result in a formatted way."""
    print(f"\n{SEPARATOR}")
    print(f"Here is the {option}d result:")
    print(f"{SEPARATOR}")
    print(f"{result}")
    print(f"{SEPARATOR}")


def main():
    """Main program function."""
    # Display logo
    print(LOGO)
    print("\nWelcome to Caesar Cipher Program!")
    
    # First run
    direction, message, shift = get_user_inputs()
    result = caesar_cipher(message, shift, direction)
    display_result(result, direction)
    
    # Continue loop
    while True:
        go_again = input("\nType 'yes' to go again, 'no' to exit: ").lower()
        
        if go_again == "yes":
            direction, message, shift = get_user_inputs()
            result = caesar_cipher(message, shift, direction)
            display_result(result, direction)
        elif go_again == "no":
            print("\n*** Thank you for using Caesar Cipher Program ***\n")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
