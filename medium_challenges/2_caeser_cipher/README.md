# 🔐 Caesar Cipher Project

A command-line application implementing the **Caesar Cipher** encryption and decryption algorithm, one of the oldest and
most famous cryptographic techniques used by Julius Caesar to protect military messages.

## 📋 Description

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions
in the alphabet. This program allows users to:

- Encrypt messages by shifting letters forward in the alphabet
- Decrypt messages by shifting letters backward in the alphabet
- Choose any shift value to customize the encryption strength
- Process messages while preserving spaces and special characters

### How It Works

Each letter is replaced by a letter a fixed number of positions down the alphabet. For example, with a **shift of 3**:

- `a` → `d`, `b` → `e`, `c` → `f`
- When reaching the end: `x` → `a`, `y` → `b`, `z` → `c` (wraps around)

To decrypt, simply shift in the **opposite direction** by the same amount.

## 📖 Project Objectives

1. **Start the Program**: Choose between `encode` (encrypt) or `decode` (decrypt)
2. **Enter Your Message**: Type the text you want to transform
3. **Enter Shift Number**: Provide the shift value (number of positions to move)
4. **View Results**: The encrypted or decrypted message will be displayed
5. **Continue or Exit**:
   - Type `yes` or `y` to process another message
   - Type `no` or `n` to exit the program

## 💡 Example Usage

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

--------------------------------------------------------------

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

## 📚 Learning Objectives

### Prerequisites

To complete a simple version of this project, you should know:

- **Variables and Data Types**: Strings, integers, and lists
- **Input/Output**: Using `input()` and `print()` functions
- **Conditionals**: `if`, `elif`, `else` statements
- **Loops**: `while` and `for` loops for iteration
- **Functions**: Creating and calling basic functions

### Skills to Practice

This challenge will help you practice:

- **String Manipulation**: Iterating through and transforming characters
- **List Operations**: Working with alphabet lists, indexing, and searching
- **Modulo Arithmetic**: Using `%` operator for wrapping values around
- **Control Flow**: Managing program flow with loops and conditions
- **Input Validation**: Checking and handling user input correctly

## 🚀 Optional Extensions

### Beginner Level

- **Input Validation**: Check if shift is a valid number before processing
- **Case Preservation**: Handle both uppercase and lowercase letters correctly
- **Error Handling**: Add try-except blocks for invalid inputs

### Intermediate Level

- **Brute Force Mode**: Try all 26 possible shifts to crack an encrypted message
- **File Encryption**: Read from and write encrypted messages to text files
- **Frequency Analysis**: Use letter frequency to suggest the most likely decryption

---

**Good luck with the project! 🎉**

---

_Challenge Type: Medium_  
_Topics: String Manipulation, Lists, Loops, Functions, Modulo Arithmetic_  
_Estimated Time (with deep research): 30-60 minutes_
