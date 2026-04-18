# 1. Numeric Types

Numbers are an unavoidable part of any program. They are not only fundamental to programming, but they also provide a good introduction to how a programming language operates. We encounter numbers daily in our lives. For instance, when withdrawing cash from an ATM or making a simple phone call, cellular frequencies rely on math and numbers.

Python has three different numeric types:
- `int` - consider as whole numbers
- `float` - consider as whole numbers with a fractional component (decimal numbers)
- `complex` - it's enough to know the first two for now.

Although working with numbers can be fairly simple. It's important to understand how variable assignment and functions arguments work with integers and floats.

## Background Information


| Concept     | Description                                                                                                                    | Example                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| random      | Module for generating random numbers and selecting random elements<br><br>[learn more here](https://mng.bz/Z2wj)               | `number = random.randint(1,100)`                                       |
| Comparisons | Operators for comparing values<br><br>[learn more here](https://mng.bz/oPJj)                                                   | `x < y`                                                                |
| f-strings   | Strings into which expressions can be interpolated<br><br>[learn more here](http://mng.bz/1z6Z) and [here](http://mng.bz/PAm2) | `f"It is currently {datetime.datetime.now()}"`                         |
| for loops   | Iterates over the elements of an iterable<br><br>[learn more here](https://mng.bz/Jymp)                                        | ```for i in range(10):<br>print(i * i)```                              |
| input       | Prompts the user to enter a string, and returns a string<br><br>[learn more here](http://mng.bz/wB27)                          | `input("Enter your name: ")`                                           |
| enumerate   | Helps us to number elements of iterables<br><br>[learn more here](https://mng.bz/qM1K)                                         | ```for index, item in enumerate("abc"):<br>print(f"{index}:{item}")``` |
| reversed    | Returns an iterator with the reversed elements of an iterable                                                                  | `r = reversed("abcd")`                                                 |


## Exercise 1: Number Guessing Game

For this exercise:
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
	- Too high
	- Too low
	- Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.

*improve the question - display program output*

### Exercise Extension

- Modify this program, such that it gives the user only three chances to guess the correct number. If they try three times without success, the program tells them that they didn’t guess in time and then exits.
- Not only should you choose a random number, but you should also choose a random number base, from 2 to 16, in which the user should submit their input. If the user inputs “10” as their guess, you’ll need to interpret it in the correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16 (hexadecimal).
- Try the same thing, but have the program randomly select a word from the dictionary and then ask the user to guess it. (You might want to limit the word length to two to five letters to avoid making it too challenging.) Instead of instructing the user to guess a smaller or larger number, have them choose an earlier or later word from the dictionary.

*update extension based on my code in enhanced version*

### Solution

*will be generated later*

**Python Loops**
As you might know, Python only provides two kinds of loops: `for` and `while`. The fact that almost every data type can be processed within a for loop makes them incredibly common and useful. Whether you’re working with database records, elements in an XML file, or the results of a text search using regular expressions, you’ll likely encounter `for` loops quite frequently.

**About `input()`**
If the user simply presses Enter when prompted to input something, the value returned by the input function is an empty string, not None. In fact, the return value from the input function **will always be a string**, regardless of the user’s input.

**About `randint()`**
Note that the maximum value in the `random.randint` function is inclusive. This is unusual in Python, where most ranges are exclusive, meaning the higher number is not included.

> [!NOTE] Note
> If you want to learn more about the walrus operator, its controversy, and why it’s actually quite useful, I suggest that you watch the following talk from PyCon 2019, in which Dustin Ingram makes an effective case for it: http://mng.bz/nPxv.
> 
> You can also read more about this operator in PEP 572, where it was introduced and defined: http://mng.bz/vxOx.

> [!NOTE] Note!
> For the sake of this exercise, we’ll assume that our user will only input valid data, specifically integers. It’s important to note that the int function typically expects a decimal number, which means its argument can only contain digits. If you’re being particularly meticulous, you can use the `str.isdigit` method (http://mng.bz/oPVN) to verify that a string contains only digits. Alternatively, you can catch the `ValueError` exception that will be raised if you attempt to convert something that cannot be converted into an integer using the int function.

## Exercise 2: Summing Numbers

The challenge is to create a `mysum()` function that performs the same task as the built-in `sum()` function. 
However instead of accepting a single sequence as an argument, it should accept a variable number of arguments. Therefore, while you might call `sum([1, 2, 3])`, you would instead call `mysum(1, 2, 3)` or `mysum(10, 20, 30, 40, 50)`.

> [!NOTE] `sum()` function
> sum function takes a sequence of numbers and returns their sum. For instance, if you call `sum([1, 2, 3])`, it will return 6. Learn more about it here: http://mng.bz/MdW2.
> 
> The built-in `sum` function takes an optional second argument, which we're ignoring here.

> [!TIP] TIP
> In order to solve this exercise, you need to know about the `splat` operator (asterisk). If you are unfamiliar with it, you can learn more about it in this Python tutorial: http://mng.bz/aR4J

*improve the question - display program output*
*Write a document for Passing an Arbitrary Number of Arguments*

### Exercise Extension

- The built-in version of sum takes an optional second argument, which is used as the starting point for the summing. (That’s why it takes a list of numbers as its first argument, unlike our `mysum` implementation.) So `sum([1,2,3], 4)` returns `10`, because `1+2+3` is `6`, which would be added to the starting value of `4`. Reimplement your `mysum` function such that it works in this way. If a second argument is no provided, then it should default to `0`. Note that while you can write a function in Python 3 that defines a parameter after args, I’d suggest avoid-ing it and just taking two arguments-a list and an optional starting point.
- Write a function that takes a list of numbers. It should return the average (i.e.,arithmetic mean) of those numbers.
- Write a function that takes a list of words (strings). It should return a tuple containing three integers, representing the length of the shortest word, the length of the longest word, and the average word length.
- Write a function that takes a list of Python objects. Sum the objects that either are integers or can be turned into integers, ignoring the others.

### Solution

#### Passing an Arbitrary Number of Arguments

*mixing positional and arbitrary arguments*
*using arbitrary keyword arguments*

```python
def make_pizza(size, *toppings):
    print(f"Making a {size} inch pizza with the following toppings: ")

    for item in toppings:
        print(f" - {item}")


make_pizza(16, "Mushroom", "Green-Papper", "Beef Steak", "Extra Cheese")
make_pizza(12, "Garlic", "Chicken", "Mushroom", "Onion")
```

```python
def build_profile(name, lastname, age, mobile, **user_profile):

    user_profile["first_name"] = name
    user_profile["last_name"] = lastname
    user_profile["user_age"] = age
    user_profile["contact"] = mobile

    print(user_profile)


build_profile("Amirhossein", "Moravveji", 32, "+989124993212")
```


