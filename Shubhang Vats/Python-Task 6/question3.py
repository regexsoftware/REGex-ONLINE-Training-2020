# Question- 3
"""
Write a Python program to read a random line from a file.
"""


import random

f = open("abc.txt", 'r')
h = (f.read().splitlines())
print(random.choice(h))







