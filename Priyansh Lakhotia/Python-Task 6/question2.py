# Question - 2
"""
2. Write a Python program to read a file line by line store it into an array.
"""

#Solution:

arr = []
f = open("abc.txt", 'r')
file_text = f.readlines()
for word in file_text:
    arr.append(word)    
print(arr)
