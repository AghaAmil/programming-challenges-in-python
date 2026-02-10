# Caesar Cipher Challenge

Build a command-line Python program that can **encode** and **decode** messages using the Caesar cipher.

## Challenge Description

The Caesar cipher is a simple substitution cipher where each letter in a message is shifted by a fixed number in the alphabet.

- With a shift of `3`:
  - `a -> d`
  - `b -> e`
  - `x -> a` (wraps around)

Your program should let the user choose whether they want to encrypt (`encode`) or decrypt (`decode`) a message.

## Objective

Create a program that:

1. Asks the user to choose `encode` or `decode`
2. Asks for a message
3. Asks for a shift number
4. Prints the transformed text
5. Repeats until the user decides to stop

## Requirements

- Use lowercase English letters: `a-z`
- Keep non-letter characters unchanged (spaces, numbers, symbols, punctuation)
- Handle shifts larger than `26` by wrapping with modulo
- For decoding, shift in the opposite direction
- Continue running in a loop while the user wants to go again

## Suggested Program Flow

1. Print a logo/banner (optional)
2. Get user inputs:
   - direction: `encode` or `decode`
   - message text
   - shift number
3. Apply Caesar cipher transformation
4. Show result
5. Ask if user wants another round (`yes`/`no`)

## Example Interaction

```text
Type 'encode' to encrypt your message, type 'decode' to decrypt your message:
encode

Type your message:
hello world!

Type the shift number:
5

Here is the encoded result:
mjqqt btwqi!
```

```text
Type 'encode' to encrypt your message, type 'decode' to decrypt your message:
decode

Type your message:
mjqqt btwqi!

Type the shift number:
5

Here is the decoded result:
hello world!
```

## Hints

- Store the alphabet in a list or string.
- Use `% 26` to wrap index values safely.
- If direction is `decode`, use a negative shift.
- A helper function makes the code cleaner, for example:
  - `caesar_cipher(text, shift, direction)`

## Optional Extensions

- Preserve uppercase letters in output
- Validate invalid user input
- Add unit tests
- Support custom alphabets

## Run a Solution

From this folder:

```bash
python3 caesar_cipher.py
```
