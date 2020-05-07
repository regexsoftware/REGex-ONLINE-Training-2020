# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:10:34 2020

@author: shree
"""

#%%
#Ques-1

import time
print("loading" ,end="")
for i in range(5):
    print(".",end="")
    time.sleep(1)
 
 #%%
#Ques-2
''' 
Return sends a specified value back to its caller whereas
Yield can produce a sequence of values. We should use yield when we 
want to iterate over a sequence, but don’t want to store the entire sequence 
in memory.
 
 
 '''

 
 #%%
#Ques-3

import datetime
print('\n')
for i in range(5):
    
    print(time.strftime('%H:%M:%S'))
    time.sleep(1)

  
 #%%
#Ques-4
    

tuple1= (1,2,3,4)
print("\noriginal Tuple is:")
print(tuple1)
list1=list(tuple1)
user_input=input("enter the element ")
user_input=int(user_input)
list1.append(user_input)
tuple2=tuple(list1)
print("\nnew Tuple is:")
print(tuple2)




 #%%
#Ques-5

import webbrowser
webbrowser.open_new_tab("https://wa.me/919981311234?text=hello!!")


