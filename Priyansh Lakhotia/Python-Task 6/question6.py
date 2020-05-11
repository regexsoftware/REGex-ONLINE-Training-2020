# Question - 6
"""
6. Write a Python program to create a file where all letters of English
alphabet are listed by specified number of letters on each line.
"""
#Solution:

import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)
