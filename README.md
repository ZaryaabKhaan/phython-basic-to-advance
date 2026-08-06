# ============================================
# MINICONDA & PYTHON ESSENTIALS - COMPLETE GUIDE
# ============================================

# ============================================
# 1. MINICONDA COMMANDS (Terminal)
# ============================================
# conda create -n myenv python=3.9
# conda activate myenv
# python filename.py
# python --version

# ============================================
# 2. PYTHON BASICS
# ============================================

# --- Indentation ---
if True:
    print("Proper indentation - 4 spaces")

# --- Check Python Version ---
import sys
print("\nPython Version:", sys.version)

# --- Variables ---
name = "John"           # String
age = 25                # Integer
height = 5.9            # Float
is_student = True       # Boolean
print(f"\nName: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# --- Comments ---
# This is a single line comment

"""
This is a
multi-line comment
"""

# --- Numbers ---
x = 10
y = 3.14
z = 2 + 3j
result = (x + y) * 2
print(f"\nNumbers: x={x}, y={y}, z={z}, Result={result}")

# ============================================
# 3. USER INPUT & TYPE CONVERSION
# ============================================

# --- Get Input from User ---
# Uncomment to test:
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# --- Data Type Conversion ---
num_str = "123"
num_int = int(num_str)
age = 25
age_str = str(age)
pi = 3.14
pi_int = int(pi)

print(f"\nConversion: '{num_str}' -> {num_int} (type: {type(num_int)})")
print(f"Conversion: {pi} -> {pi_int} (type: {type(pi_int)})")

# --- Data Types ---
text = "Hello"          # str
number = 42             # int
decimal = 3.14          # float
is_valid = True         # bool
items = [1, 2, 3]       # list
coordinates = (4, 5)    # tuple
person = {"name": "John"}  # dict
unique = {1, 2, 3}      # set

print(f"\nData Types: {type(text)}, {type(number)}, {type(items)}")

# ============================================
# 4. RANDOM NUMBERS
# ============================================

import random

rand_int = random.randint(1, 10)
rand_float = random.random()
colors = ['red', 'blue', 'green']
rand_choice = random.choice(colors)

print(f"\nRandom: Integer={rand_int}, Float={rand_float:.2f}, Choice={rand_choice}")

# ============================================
# 5. STRINGS DEEP DIVE
# ============================================

# --- String Basics ---
str1 = 'Single quotes'
str2 = "Double quotes"
str3 = """Multi-line
string"""
print(f"\nStrings: {str1}, {str2}")

# --- String Slicing ---
text = "Hello World"
print(f"\nOriginal: {text}")
print(f"Slicing [0:5]: {text[0:5]}")
print(f"Slicing [6:]: {text[6:]}")
print(f"Slicing [-5:]: {text[-5:]}")
print(f"Reverse [::-1]: {text[::-1]}")
print(f"Step [::2]: {text[::2]}")

# --- For Loop with Strings ---
print("\nFor Loop through string:")
for char in "Python":
    print(f"  {char}")

print("\nWith index:")
for i, char in enumerate("Python"):
    print(f"  Index {i}: {char}")

# --- Modify Strings ---
text = "  Hello World  "
print(f"\nOriginal: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")
print(f"Split: {text.split()}")

# --- String Formatting ---
name = "Alice"
age = 30
print(f"\nF-string: My name is {name} and I'm {age} years old")

# ============================================
# 6. OPERATORS
# ============================================

# --- Arithmetic Operators ---
a, b = 10, 3
print(f"\nArithmetic:")
print(f"  {a} + {b} = {a + b}")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} / {b} = {a / b}")
print(f"  {a} // {b} = {a // b} (Floor)")
print(f"  {a} % {b} = {a % b} (Modulus)")
print(f"  {a} ** {b} = {a ** b} (Exponent)")

# --- Comparison Operators ---
x, y = 5, 10
print(f"\nComparison:")
print(f"  {x} == {y}: {x == y}")
print(f"  {x} != {y}: {x != y}")
print(f"  {x} < {y}: {x < y}")
print(f"  {x} > {y}: {x > y}")
print(f"  {x} <= {y}: {x <= y}")
print(f"  {x} >= {y}: {x >= y}")

# --- Logical Operators ---
p, q = True, False
print(f"\nLogical:")
print(f"  {p} and {q}: {p and q}")
print(f"  {p} or {q}: {p or q}")
print(f"  not {p}: {not p}")

# ============================================
# 7. LISTS
# ============================================

# --- Creating Lists ---
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]
range_list = list(range(5))
print(f"\nLists:")
print(f"  Fruits: {fruits}")
print(f"  Range: {range_list}")

# --- List Slicing ---
items = ['a', 'b', 'c', 'd', 'e']
print(f"\nList Slicing on {items}:")
print(f"  [1:4]: {items[1:4]}")
print(f"  [:3]: {items[:3]}")
print(f"  [2:]: {items[2:]}")
print(f"  [-3:]: {items[-3:]}")
print(f"  [::2]: {items[::2]}")

# --- List Item Change ---
colors = ['red', 'blue', 'green']
print(f"\nOriginal: {colors}")

colors[1] = 'yellow'
print(f"After change: {colors}")

colors[1:3] = ['pink', 'purple']
print(f"After slice change: {colors}")

colors.insert(1, 'orange')
print(f"After insert: {colors}")

colors.append('white')
print(f"After append: {colors}")

colors.remove('pink')
print(f"After remove: {colors}")

# --- List Comprehension ---
squares = [x**2 for x in range(5)]
even_numbers = [x for x in range(10) if x % 2 == 0]
names = ['Alice', 'Bob', 'Charlie']
name_lengths = [len(name) for name in names]

print(f"\nList Comprehension:")
print(f"  Squares: {squares}")
print(f"  Even numbers: {even_numbers}")
print(f"  Name lengths: {name_lengths}")

# --- List Comprehension with Range ---
multiples = [i*2 for i in range(1, 6)]
pairs = [(x, x**2) for x in range(3)]
matrix = [[j for j in range(3)] for i in range(3)]
flattened = [num for row in matrix for num in row]

print(f"\nMore List Comprehension:")
print(f"  Multiples: {multiples}")
print(f"  Pairs: {pairs}")
print(f"  Matrix: {matrix}")
print(f"  Flattened: {flattened}")

# ============================================
# 8. ADVANCED PATTERNS
# ============================================

# --- Error Handling ---
print("\nError Handling:")
try:
    result = 10 / 2
    print(f"  Result: {result}")
except ZeroDivisionError:
    print("  Can't divide by zero!")
finally:
    print("  This always runs")

# --- Reading Files (Example) ---
print("\nFile Handling (commented):")
# with open('file.txt', 'r') as file:
#     content = file.read()

# --- Main Guard ---
print("\nMain Guard Pattern:")
if __name__ == "__main__":
    print("  This runs when script is executed directly")

# ============================================
# SUMMARY
# ============================================
print("\n" + "="*50)
print("✅ ALL CONCEPTS COVERED SUCCESSFULLY!")
print("="*50)

