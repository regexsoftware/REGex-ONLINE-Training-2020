# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:47:04 2020

@author: shree
"""
#%%
#Ques-1

LIST_STATES = ["GOA","RAJASTHAN","KARNATAKA","GUJRAT","MANIPUR",
               "MADHYA PRADESH"]
list2=[]
for states in LIST_STATES:
      list2.append(states[0])
print(list2)
  

#%%
#Ques-2

list1= ['GAnga', 'Tapti', 'Kaveri', 'Yamuna', 'Narmada' ]
list2=[]
for river_name in list1:
    sum=0
    for name in river_name:
        a=ord(name)
        sum=sum+a
    list2.append(sum)
print(list2)



#%%
#Ques-3

import time 
from datetime import datetime
list1=[]
while(True):
    if time.strftime("%H:%M:%S")=="19:33:35":
        t=datetime.now()
        t=str(t)
        list1=t.split(" ")
        print(list1)
        break
    else:
        time.sleep(1)
        continue

#%%
#Ques-4

tuple1 = ('a','l','g','o','r','i','t','h','m')

list1=list(tuple1)
tuple2=()
print("\nThe tuple is")
print(tuple1[0:])
t=tuple1[:3]+tuple1[4:]
print(t)


#%%
#Ques-5
REGex=[1,2,3,4,5,6,7,8,9,0,77,44,15,33,65,89,12]
list1=[]
list2=[]
for num in REGex:
    if(num>20):
       list1.append(num)
    elif(num<=20):
        list2.append(num)
print("\nlist of number which are greater than 20")
print(list1)
print("\nlist of number which are smaller or equal to 20")
print(list2)

#%%
#Ques-6

import os
a = os.popen("date")
date = a.read()
print(date)
