# Question - 1
"""
1. Write a Python program to read a file line by line and store it into a list
"""

#Solution:

ls=[]
f = open("abc.txt", 'r')
file_text = f.readlines()
for word in file_text:
    ls.append(word)    
print(ls)
    

