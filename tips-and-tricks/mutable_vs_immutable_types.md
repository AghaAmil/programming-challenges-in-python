# Mutable vs Immutable Types in Python

## Table of Contents
1. [Introduction](#introduction)
2. [Mutable vs Immutable Types](#mutable-vs-immutable-types)
3. [How Python Passes Arguments](#how-python-passes-arguments)
4. [The Scope Problem](#the-scope-problem)
5. [Common Mistakes](#common-mistakes)
6. [Best Practices](#best-practices)
7. [Advanced Examples](#advanced-examples)

---

## Introduction

One of the most important concepts in Python is understanding how data types behave when you modify them or pass them to functions. This behavior is determined by whether a type is **mutable** or **immutable**.

### Key Concept
- **Mutable objects** can be changed after creation
- **Immutable objects** cannot be changed after creation

This distinction has profound implications for how your code behaves, especially when working with functions and variable scopes.

---

## Mutable vs Immutable Types

### Immutable Types (Cannot be changed in-place)
- `int` - Integers
- `float` - Floating-point numbers
- `str` - Strings
- `tuple` - Tuples
- `bool` - Booleans
- `frozenset` - Frozen sets

### Mutable Types (Can be changed in-place)
- `list` - Lists
- `dict` - Dictionaries
- `set` - Sets
- Custom objects (usually)

### Example: Immutable Behavior

```python
# Strings are immutable
text = "hello"
text_id = id(text)  # Memory address
text = text + " world"  # Creates a NEW string object
print(id(text) == text_id)  # False - different object!

# Integers are immutable
count = 5
count_id = id(count)
count = count + 1  # Creates a NEW integer object
print(id(count) == count_id)  # False - different object!
```

### Example: Mutable Behavior

```python
# Lists are mutable
numbers = [1, 2, 3]
numbers_id = id(numbers)
numbers.append(4)  # Modifies the SAME list object
print(id(numbers) == numbers_id)  # True - same object!

# Dictionaries are mutable
scores = {"Alice": 90}
scores_id = id(scores)
scores["Bob"] = 85  # Modifies the SAME dict object
print(id(scores) == scores_id)  # True - same object!
```

---

## How Python Passes Arguments

Python uses **"pass by object reference"** (sometimes called "pass by assignment"). This means:
- The function receives a reference to the same object
- BUT what happens next depends on whether the object is mutable or immutable

### With Immutable Objects

```python
def increment(number):
    number = number + 1  # Creates NEW integer, local variable reassigned
    return number

x = 10
result = increment(x)
print(x)       # 10 (unchanged!)
print(result)  # 11
```

**What happened?**
1. `x` references integer object `10`
2. Function parameter `number` also references `10`
3. `number = number + 1` creates a NEW integer `11`
4. Local variable `number` now references `11`
5. Original `x` still references `10` - unchanged!

### With Mutable Objects

```python
def add_item(items):
    items.append("new")  # Modifies the SAME list object
    return items

my_list = ["old"]
result = add_item(my_list)
print(my_list)  # ["old", "new"] (changed!)
print(result)   # ["old", "new"]
print(my_list is result)  # True - same object!
```

**What happened?**
1. `my_list` references a list object
2. Function parameter `items` references the SAME list object
3. `items.append("new")` modifies the list in-place
4. Both `my_list` and `items` point to the same modified list

---

## The Scope Problem

### The Classic Mistake: Trying to Accumulate Immutable Values

```python
total = 0

def add_to_total(amount):
    total = total + amount  # ❌ UnboundLocalError!
    return total

add_to_total(10)
```

**Error:** `UnboundLocalError: local variable 'total' referenced before assignment`

**Why?** Python sees an assignment to `total`, so it treats it as a local variable. But you're trying to read it before assigning to it!

### The Common Workaround (That Doesn't Work as Expected)

```python
counter = 0

def increment_counter(value):
    value = value + 1  # Only changes local parameter
    return value

increment_counter(counter)  # Returns 1
increment_counter(counter)  # Returns 1 again
increment_counter(counter)  # Returns 1 again
print(counter)  # 0 - Never changed!
```

**The Problem:**
- Each call passes the current value of `counter` (which is always 0)
- The function increments its local copy
- The return value is ignored
- The global `counter` never changes

### The Correct Solution: Capture Return Values

```python
counter = 0

def increment_counter(value):
    value = value + 1
    return value

counter = increment_counter(counter)  # ✅ Capture and reassign!
counter = increment_counter(counter)
counter = increment_counter(counter)
print(counter)  # 3 - Works!
```

---

## Common Mistakes

### Mistake 1: Not Capturing Return Values for Immutables

```python
# ❌ WRONG
score = 0

def add_points(points):
    points += 10
    return points

add_points(score)  # Return value ignored!
print(score)  # 0 - unchanged

# ✅ CORRECT
score = add_points(score)  # Capture the return value
print(score)  # 10
```

### Mistake 2: Expecting Immutables to Behave Like Mutables

```python
# ❌ WRONG - Thinking like Java/C++
def reset_value(num):
    num = 0  # Only changes local variable

my_num = 42
reset_value(my_num)
print(my_num)  # 42 - unchanged!

# ✅ CORRECT
def reset_value(num):
    return 0

my_num = reset_value(my_num)
print(my_num)  # 0
```

### Mistake 3: Accidentally Mutating Shared Lists

```python
# ❌ DANGEROUS
def add_user(users, name):
    users.append(name)  # Modifies original list!
    return users

all_users = ["Alice"]
new_users = add_user(all_users, "Bob")
print(all_users)   # ["Alice", "Bob"] - was modified!
print(new_users)   # ["Alice", "Bob"]
print(all_users is new_users)  # True - same object!

# ✅ BETTER - Create a new list if you don't want side effects
def add_user(users, name):
    return users + [name]  # Creates new list

# ✅ OR - Be explicit about mutation
def add_user_in_place(users, name):
    """Modifies users list in-place."""
    users.append(name)
    # No return needed - caller's list is modified
```

### Mistake 4: Default Mutable Arguments

```python
# ❌ DANGEROUS BUG
def add_item(item, container=[]):  # DON'T DO THIS!
    container.append(item)
    return container

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Wait, what?!
print(add_item(3))  # [1, 2, 3] - The list persists!

# ✅ CORRECT
def add_item(item, container=None):
    if container is None:
        container = []  # Create new list each time
    container.append(item)
    return container

print(add_item(1))  # [1]
print(add_item(2))  # [2] - Fresh list!
print(add_item(3))  # [3] - Fresh list!
```

---

## Best Practices

### 1. Always Capture Return Values for Immutable Types

```python
# For immutable types (int, float, str, tuple)
count = 0
count = increment(count)  # ✅ Always reassign

total = 0.0
total = add_value(total, 5.5)  # ✅ Always reassign

name = "John"
name = capitalize(name)  # ✅ Always reassign
```

### 2. Be Explicit About Mutation

```python
# If a function modifies a mutable argument, make it clear:
def sort_list_in_place(items):
    """Sorts the list in-place. Returns None."""
    items.sort()

# If a function returns a new object, make it clear:
def get_sorted_list(items):
    """Returns a new sorted list. Original unchanged."""
    return sorted(items)

# Usage
my_list = [3, 1, 2]
sort_list_in_place(my_list)  # my_list is now [1, 2, 3]

my_list = [3, 1, 2]
new_list = get_sorted_list(my_list)  # my_list unchanged
```

### 3. Use the `global` or `nonlocal` Keywords When Needed

```python
# For modifying global variables
counter = 0

def increment_global():
    global counter  # Explicitly declare you're modifying global
    counter += 1

increment_global()
print(counter)  # 1

# For nested functions
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Access enclosing scope variable
        count += 1
    
    inner()
    inner()
    return count

print(outer())  # 2
```

### 4. Prefer Returning New Values Over Mutation

```python
# ❌ Harder to reason about
def update_user(user):
    user["last_login"] = "2026-02-16"  # Mutates original

# ✅ Easier to reason about
def update_user(user):
    return {**user, "last_login": "2026-02-16"}  # Returns new dict

# Usage
original = {"name": "Alice", "last_login": "2026-01-01"}
updated = update_user(original)
# original is unchanged, updated has new data
```

### 5. Use Immutable Defaults

```python
# ✅ GOOD - Immutable defaults are safe
def greet(name="Guest"):  # str is immutable
    return f"Hello, {name}!"

def multiply(x, factor=2):  # int is immutable
    return x * factor

# ❌ BAD - Mutable defaults
def add_to_list(item, lst=[]):  # DON'T DO THIS
    pass

# ✅ GOOD - Use None and create mutable inside
def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## Advanced Examples

### Example 1: Accumulating Values Correctly

```python
# Simulating a simple bank account

balance = 100

def deposit(current_balance, amount):
    """Returns new balance after deposit."""
    return current_balance + amount

def withdraw(current_balance, amount):
    """Returns new balance after withdrawal."""
    if current_balance >= amount:
        return current_balance - amount
    else:
        print("Insufficient funds")
        return current_balance

# ✅ Correct usage
balance = deposit(balance, 50)
print(f"Balance: ${balance}")  # $150

balance = withdraw(balance, 30)
print(f"Balance: ${balance}")  # $120

balance = withdraw(balance, 200)  # Insufficient funds
print(f"Balance: ${balance}")  # $120
```

### Example 2: Working with Lists (Mutable)

```python
# Building a shopping cart

cart = []

def add_to_cart(cart_items, product):
    """Modifies cart in-place."""
    cart_items.append(product)
    # No return needed - list is modified

def get_cart_copy(cart_items):
    """Returns a copy to prevent accidental modification."""
    return cart_items.copy()

# Usage
add_to_cart(cart, "Apple")
add_to_cart(cart, "Banana")
print(cart)  # ["Apple", "Banana"]

# If you want to preserve original:
backup = get_cart_copy(cart)
cart.clear()
print(cart)    # []
print(backup)  # ["Apple", "Banana"]
```

### Example 3: Understanding References

```python
# Shallow copy vs deep copy
import copy

# Original list with nested list
original = [1, 2, [3, 4]]

# Assignment - both names point to same object
same_list = original
same_list.append(5)
print(original)  # [1, 2, [3, 4], 5] - modified!

# Shallow copy - top level copied, nested objects shared
original = [1, 2, [3, 4]]
shallow = original.copy()
shallow.append(5)
print(original)  # [1, 2, [3, 4]] - not modified
shallow[2].append(99)
print(original)  # [1, 2, [3, 4, 99]] - nested list modified!

# Deep copy - everything copied
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep.append(5)
deep[2].append(99)
print(original)  # [1, 2, [3, 4]] - completely unchanged!
```

### Example 4: Class Objects (Usually Mutable)

```python
class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

def add_points(player, points):
    """Modifies player object in-place."""
    player.score += points
    # Even though player.score (int) is immutable,
    # we're modifying the object's attribute

player1 = Player("Alice", 100)
add_points(player1, 50)
print(player1.score)  # 150 - modified!

# Objects are passed by reference, so mutation affects original
```

### Example 5: Strings Are Immutable

```python
def modify_string(text):
    text = text + " World"  # Creates NEW string
    return text

def try_modify_in_place(text):
    text[0] = "H"  # ❌ TypeError: str doesn't support item assignment

greeting = "Hello"
result = modify_string(greeting)
print(greeting)  # "Hello" - unchanged
print(result)    # "Hello World"

# String methods always return new strings
name = "alice"
capitalized = name.capitalize()  # Returns new string
print(name)        # "alice" - original unchanged
print(capitalized) # "Alice"
```

---

## Summary

### Quick Reference Table

| Type | Mutable? | Pass to Function | Modify in Function | Original Changed? |
|------|----------|-----------------|-------------------|------------------|
| `int`, `float` | No | ✅ | Creates new local | ❌ No |
| `str` | No | ✅ | Creates new local | ❌ No |
| `tuple` | No | ✅ | Cannot modify | ❌ No |
| `list` | Yes | ✅ | Modifies original | ✅ Yes |
| `dict` | Yes | ✅ | Modifies original | ✅ Yes |
| `set` | Yes | ✅ | Modifies original | ✅ Yes |

### Key Takeaways

1. **Immutable types** (int, float, str, tuple) cannot be changed in-place. Operations create new objects.

2. **Mutable types** (list, dict, set) can be changed in-place. Operations modify the original object.

3. When you pass an **immutable** to a function and want to update the original variable, you **must capture the return value**.

4. When you pass a **mutable** to a function, it can be modified directly, but this can lead to unexpected side effects.

5. **Always reassign** when working with immutables:
   ```python
   x = function_that_returns_value(x)  # ✅ Correct
   ```

6. **Never use mutable default arguments** - use `None` and create the mutable inside the function.

7. Use `global` or `nonlocal` keywords explicitly if you need to modify variables from outer scopes.

8. When in doubt, prefer **returning new values** over mutating arguments for clearer code.

---

## Additional Resources

- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python FAQ on Mutable Default Arguments](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
