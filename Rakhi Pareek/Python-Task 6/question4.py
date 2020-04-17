# Question - 4

"""
4. Write a Python program to combine each line from first file with the
corresponding line in second file
"""

f = open("abc.txt", 'r')
a = f.read().splitlines()

f= open("xyz.txt", 'r')
b = f.read().splitlines()

ls = []
for i,j in zip(a,b):
    print(i + j)
    