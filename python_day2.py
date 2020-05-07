# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:59:02 2020

@author: shree
"""


#%%
#Ques-1

print(3+4**6-9*10/2)

#%%
#Ques-2


string ="hello this side regex"
count=0
for word in string:
    for letter in word:
        if letter in ['a','e','i','o','u']:
            count+=1
print("\nThe total no of vowels are:")           
print(count)

#%%
#Ques-3


height=input("Enter the height of the triangle")
base=input("Enter the base of the triangle")
h=int(height)
b=int(base)
print("\nThe area of the triangle is:")
area=1/2*h*b
print(area)

#%%
#Ques-4

import calendar

y = int(input("Enter year: "))
print("display the calendar.")
print(calendar.calendar(y))

#%%




