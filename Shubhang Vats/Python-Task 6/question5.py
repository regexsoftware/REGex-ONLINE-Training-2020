# Question - 5
"""
5. Write a Python program to generate 26 text files named A.txt, B.txt, and
so on up to Z.txt.
"""


# for list of capital alphabets
alpha = []
for i in range (0,26):
    alpha.append(chr(ord('A') + i))


# for creation of files
for word in alpha:
    f= open(word + '.txt', 'w')
    f.write(word + 'File')
    
    
