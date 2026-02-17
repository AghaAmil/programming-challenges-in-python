"""
Caesar Cipher Encryption/Decryption Tool
AI-Generated Implementation

A command-line program that encrypts and decrypts messages using the Caesar cipher,
one of the oldest and simplest encryption techniques.
"""

import string
from typing import Literal

# Constants
ALPHABET = string.ascii_lowercase
SEPARATOR_HEAVY = "=" * 60
SEPARATOR_LIGHT = "-" * 60


def encrypt_decrypt(text: str, shift: int, mode: Literal["encode", "decode"]) -> str:
    """
    Apply Caesar cipher transformation to the input text.
    
    The Caesar cipher shifts each letter by a fixed number of positions in the alphabet.
    Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged.
    
    Args:
        text: The message to transform
        shift: Number of positions to shift (positive or negative)
        mode: 'encode' to encrypt, 'decode' to decrypt
    
    Returns:
        The transformed text
    
    Examples:
        >>> encrypt_decrypt("hello", 3, "encode")
        'khoor'
        >>> encrypt_decrypt("khoor", 3, "decode")
        'hello'
    """
    # For decoding, shift in the opposite direction
    effective_shift = -shift if mode == "decode" else shift
    
    result = []
    for char in text:
        if char.lower() in ALPHABET:
            # Preserve original case
            is_upper = char.isupper()
            char_lower = char.lower()
            
            # Find position in alphabet and apply shift
            old_index = ALPHABET.index(char_lower)
            new_index = (old_index + effective_shift) % len(ALPHABET)
            new_char = ALPHABET[new_index]
            
            # Restore case if needed
            result.append(new_char.upper() if is_upper else new_char)
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)


def get_mode() -> Literal["encode", "decode"]:
    """
    Prompt user to select encryption or decryption mode.
    
    Returns:
        'encode' or 'decode'
    """
    while True:
        print("\n🔐 Select operation mode:")
        print("   [1] Encode (encrypt)")
        print("   [2] Decode (decrypt)")
        choice = input("   Enter choice (1/2 or encode/decode): ").strip().lower()
        
        if choice in ["1", "encode", "e"]:
            return "encode"
        elif choice in ["2", "decode", "d"]:
            return "decode"
        else:
            print("   ❌ Invalid choice. Please try again.")


def get_message() -> str:
    """
    Get the message to encrypt or decrypt from the user.
    
    Returns:
        User's message
    """
    while True:
        message = input("\n📝 Enter your message:\n   → ")
        if message.strip():
            return message
        print("   ❌ Message cannot be empty. Please try again.")


def get_shift() -> int:
    """
    Get the shift amount from the user with validation.
    
    Returns:
        Shift amount (integer)
    """
    while True:
        try:
            shift_input = input("\n🔢 Enter shift amount (1-25 recommended):\n   → ")
            shift = int(shift_input)
            return shift
        except ValueError:
            print("   ❌ Please enter a valid number.")


def display_result(original: str, result: str, shift: int, mode: str) -> None:
    """
    Display the encryption/decryption result in a formatted way.
    
    Args:
        original: The original message
        result: The transformed message
        shift: The shift amount used
        mode: 'encode' or 'decode'
    """
    action = "ENCRYPTED" if mode == "encode" else "DECRYPTED"
    
    print(f"\n{SEPARATOR_HEAVY}")
    print(f"  ✨ {action} MESSAGE")
    print(SEPARATOR_LIGHT)
    print(f"  Original:  {original}")
    print(f"  Result:    {result}")
    print(SEPARATOR_LIGHT)
    print(f"  Mode:      {mode.upper()}")
    print(f"  Shift:     {shift}")
    print(SEPARATOR_HEAVY)


def display_welcome() -> None:
    """Display welcome banner."""
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║         CAESAR CIPHER ENCRYPTION TOOL                  ║
    ║         AI-Generated Implementation                    ║
    ╚════════════════════════════════════════════════════════╝
    """
    print(banner)
    print("  Welcome! This tool encrypts and decrypts messages using")
    print("  the Caesar cipher - a simple letter substitution technique.")
    print(f"\n{SEPARATOR_LIGHT}")


def display_goodbye() -> None:
    """Display goodbye message."""
    print(f"\n{SEPARATOR_HEAVY}")
    print("  ✨ Thank you for using Caesar Cipher Tool!")
    print("  🔐 Keep your messages secret!")
    print(SEPARATOR_HEAVY)


def continue_prompt() -> bool:
    """
    Ask user if they want to perform another operation.
    
    Returns:
        True to continue, False to exit
    """
    while True:
        choice = input("\n🔄 Would you like to continue? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("   ❌ Please answer 'yes' or 'no'.")


def run_cipher_operation() -> None:
    """Execute a single cipher operation (encode or decode)."""
    mode = get_mode()
    message = get_message()
    shift = get_shift()
    
    # Perform the encryption/decryption
    result = encrypt_decrypt(message, shift, mode)
    
    # Display the result
    display_result(message, result, shift, mode)


def main() -> None:
    """Main program entry point."""
    # Show welcome message
    display_welcome()
    
    # Main program loop
    while True:
        try:
            run_cipher_operation()
            
            # Ask if user wants to continue
            if not continue_prompt():
                break
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user.")
            break
    
    # Show goodbye message
    display_goodbye()


if __name__ == "__main__":
    main()
