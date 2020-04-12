# Assignment 1 [Python] [Ayush Goyal]

## 1. What is IPython & CPython?

**Ipython :** IPython is an alternative Python interpreter. It is an interactive shell used for computing in Python.

**CPython :** is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the language. CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it. 

## 2. Basic difference between Python2 & python3?

**Python2**   
- Two string types.   
	- Unicode strings.
	- Non-unicode strings.
- Seperate int and long types for non-floating point numbers.
- Return type of division of integers is "int" meaning `5/4` will return 1 instead of 1.25
- `print` is a special statement rather than a function.

**Python3**
- All strings are unicode strings
- Only one integer type called `int`, which behaves like the long type.
- Return type of integer division is `float`, i.e. `5/4` will return 1.25
- `print()` is a built in function. 

## 3. Difference between ASCII & unicode?
The main difference between the two is in the way they encode the character and the number of bits that they use for each. **ASCII originally used 7 bits** to encode each character. In contrast, **Unicode** uses a variable bit encoding program where you can choose between **32, 16, and 8-bit** encodings.


