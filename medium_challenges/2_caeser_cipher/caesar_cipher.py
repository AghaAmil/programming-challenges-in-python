from art import LOGO

ALPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar_chiper(original_text, shift_amount, option):
    output_text = ""

    for letter in original_text:
        if option == "decode":
            shift_amount *= -1

        if letter in ALPHABET:
            shifted_index = ALPHABET.index(letter) + shift_amount
            # if the shifted index in out of the range of english alphabet letters
            shifted_index %= len(ALPHABET)
            shifted_alphabet = ALPHABET[shifted_index]
            output_text += shifted_alphabet
        else:
            output_text += letter

    print(f"\nHere is the {option}d result:\n{output_text}")


def program_runner():
    direction = input("\nType 'encode' to encrypt your message, type 'decode' to decrypt your message:\n").lower()
    message = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar_chiper(original_text=message, shift_amount=shift, option=direction)


print(LOGO)
program_runner()

play_again = True

while play_again:
    go_again = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower()

    if go_again == "yes":
        program_runner()
    elif go_again == "no":
        print("\n*** Hope you enjoy Caesar Chipher Program ***\n")
        play_again = False
    else:
        print("Invalid Input")
