#1)Write a Program to print new list which contains all the first Characters of strings present in a List.
#LIST_STATES = ["GOA","RAJASTHAN","KARNATAKA","GUJRAT","MANIPUR", “MADHYA PRADESH”]
#Sol. 
LIST_STATES = ["GOA","RAJASTHAN","KARNATAKA","GUJRAT","MANIPUR", "MADHYA PRADESH"]
for i in LIST_STATES:
    print(i[0])


#2)Write a program to replace each string with an integer value in a given list of strings. The replacement integer value should be a sum of AScci values of each character of type corresponding string.
#LIST: ['GAnga', 'Tapti', 'Kaveri', 'Yamuna', 'Narmada' ]
#Sol.
LIST=['GAnga', 'Tapti', 'Kaveri', 'Yamuna', 'Narmada' ]
k=0 
for i in LIST:
    j=0
    sum_=0
    for j in i:
        sum_=sum_ + ord(j)
    LIST[k]=sum_
    k+=1
print(LIST)


#3)You have to run your Program at 9:00am. Date: 14th April 2020.
#HINT:
# You have to use datetime Module or time module..
# You have to convert your output in #LIST_FORMAT
# [ '2020-04-13' , '17:11:01.952975' ]
# you can use this with the helf of IF/Else statement
#sol)


#4)GIve a tuple:tuple = ('a','l','g','o','r','i','t','h','m')
#1. Using the concept of slicing, print the whole tuple
#2. delete the element at the 3rd Index, print the tuple.
tuple = ('a','l','g','o','r','i','t','h','m')
print(tuple[0:])

tuple = tuple[:2] + tuple[3:] 
print(tuple)

#5. Take a list REGex=[1,2,3,4,5,6,7,8,9,0,77,44,15,33,65,89,12]
#- print only those numbers greator then 20
#- then print those numbers those are less then 10 or equal to 10
#- store these above two list in two different list.
#Sol.
REGex=[1,2,3,4,5,6,7,8,9,0,77,44,15,33,65,89,12]
list1=[]
list2=[]
for i in REGex:
    if i> 20:
        list1.append(i)
    if i<= 10:
        list2.append(i)  
print(list1)
print(list2)

#6. Execute standard LINUX Commands using Python Programming
#Sol.
import os
cmd = 'wc -l my_text_file.txt > out_file.txt'
os.system(cmd)

#7. Revise *args and **kwargs Concepts
#Sol.
def totalSum(*args):
    result = 0
    for x in args:
        result += x
    return result

def concStr(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(totalSum(1, 2, 3))
print(concStr(a="This", b="is", c="a", d="Python", e="Program"))




