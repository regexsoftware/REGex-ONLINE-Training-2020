# Ques1 : Write a Python program to read a file line by line and store it into a list.
# Ans : 
f = open('sample','r')
l = []

for i in f:
	if(i[-1] == '\n'):               # i will have a full sentence in a line including '\n' that's why we are removing '\n' in a list
		l.append(i[:-1])
	else:
		l.append(i)
f.close()

print('Line by line text of a file in a list : ',l)



# Ques2 : Write a Python program to read a file line by line store it into an array.
# Ans:
import numpy

f = open('sample','r')
array = numpy.array([])

for i in f:
    if(i[-1] == '\n'): 
        array = numpy.append(array, [i[:-1]])
    else:
        array = numpy.append(array, i)
f.close()

print('Line by line text of a file in an array : ', array)



# Ques3 : Write a Python program to read a random line from a file.
# Ans : 
import random
random_lines = random.choice(open('sample','r').readlines())
print(random_lines)



# Ques4 : Write a Python program to combine each line from first file with the corresponding line in second file.
# Ans :
f1 = open('sample','r')
f2 = open('sample2','r')


file1 = f1.readlines()
file2 = f2.readlines()

f1.close()
f2.close()

for i in range(len(file1)):
    if '\n' in file1[i]:                         # ".readlines" creates an output : ['sentence in a line \n'] so this step is to remove '\n' 
        print(file1[i][:-1] + file2[i])
    else:
        print(file1[i] + file2[i])



# Ques5 : 5. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# Ans :

for i in range(65, 91):           # Ascii codes from A-Z = 65-90
    alpha = chr(i)                # Convert ascii to character value
    file_name = alpha +'.txt'
    f = open(file_name,'w')
    f.close()
    print(file_name)              # just to be sure that file has created successfully.



# Ques6 : Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.
# Ans :
number = int(input('Enter a number : '))
in_one_line = 26//number
num = 97                               # Ascii code of "a" : 97   
while num<=122:                        # Ascii code of "z" : 122
    for i in range(number):
        print(chr(num), end=' ')
        num += 1
        if(num > 122):
            break
    print()