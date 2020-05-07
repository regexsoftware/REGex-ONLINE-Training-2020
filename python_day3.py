# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:34:59 2020

@author: shree
"""
#%%
#Ques-1

str1="hello this world @2020!!!"
str2=str1[0:-3]
str2=str2.replace('@','')
print(str2)





#%%
#Ques-2

num=int(input('Enter the number'))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum += digit ** 3
    temp=temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   

    
#%%
    
#Ques 3
list1=["Apple","banana","cat","REGEX","apple"]
list2=sorted(list1,key=str.lower)
#using the "key = str.lower" converts all the upper case string into lower case and then sorts
# the list by which we get the following output otherwise we would have got this:
#['Apple', 'REGEX', 'apple', 'banana', 'cat']
print(list2)