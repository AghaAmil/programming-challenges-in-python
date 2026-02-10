# Caesar Cipher Challenge

## 🎯 Challenge Overview

Build a command-line Python program that implements the **Caesar Cipher** encryption and decryption algorithm. This classic cryptography challenge will help you practice string manipulation, list operations, modulo arithmetic, and user input handling.

---

## 📚 What is the Caesar Cipher?

The Caesar Cipher is one of the oldest and simplest encryption techniques, named after Julius Caesar who reportedly used it to protect military messages. It's a **substitution cipher** where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

### How It Works

- Each letter is replaced by a letter a fixed number of positions down the alphabet
- For example, with a **shift of 3**:
  - `a` → `d`
  - `b` → `e`
  - `c` → `f`
  - ...
  - `x` → `a` (wraps around to the beginning)
  - `y` → `b`
  - `z` → `c`

### Example

**Original message:** `hello world`  
**Shift:** `5`  
**Encrypted message:** `mjqqt btwqi`

To decrypt, you simply shift in the **opposite direction** by the same amount.

---

## 🎓 Challenge Objectives

Create a Python program that can encode and decode messages using the Caesar cipher algorithm.

1. Asks the user to choose `encode` or `decode`
2. Asks for a message
3. Asks for a shift number
4. Prints the transformed text
5. Repeats until the user decides to stop

---

## 🖥️ Example Interaction

### Encoding Example

```
Type 'encode' to encrypt your message, type 'decode' to decrypt your message:
encode

Type your message:
hello world!

Type the shift number:
5

Here is the encoded result:
mjqqt btwqi!

Type 'yes' if you want to go again. Otherwise type 'no': yes
```

### Decoding Example

```
Type 'encode' to encrypt your message, type 'decode' to decrypt your message:
decode

Type your message:
mjqqt btwqi!

Type the shift number:
5

Here is the decoded result:
hello world!

Type 'yes' if you want to go again. Otherwise type 'no': no

*** Hope you enjoy Caesar Cipher Program ***
```

---

## 🌟 Optional Extensions

Once you have the basic program working, try these enhancements:

### Beginner Extensions

- ✨ Add input validation (check if shift is a number)
- ✨ Handle both uppercase and lowercase letters while preserving case
- ✨ Add error handling for invalid inputs

### Intermediate Extensions

- ✨ Support encryption without knowing the shift (brute force decryption)
- ✨ Add a "crack mode" that tries all 26 possible shifts
- ✨ Create a file encryption/decryption mode
- ✨ Add frequency analysis to suggest the most likely decryption

### Advanced Extensions

- ✨ Support custom alphabets (numbers, special characters)
- ✨ Implement other classical ciphers (Vigenère, ROT13)
- ✨ Create a GUI version with tkinter
- ✨ Add unit tests with pytest

---

## 📖 Learning Outcomes

By completing this challenge, you will practice:

- **String manipulation** - iterating through characters
- **List operations** - indexing, searching
- **Modulo arithmetic** - wrapping values
- **Functions** - organizing code into reusable blocks
- **Loops** - while loops for continuous operation
- **User input** - getting and validating input
- **Conditional logic** - if/elif/else statements
- **Type conversion** - string to integer
- **Algorithm implementation** - translating logic into code

---

**Good luck with the challenge! 🎉**

---

_Challenge Type: Medium_  
_Topics: Cryptography, String Manipulation, Loops, Functions_  
_Estimated Time: 30-60 minutes_
