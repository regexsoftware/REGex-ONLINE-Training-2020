# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 07:43:55 2020

@author: shree
"""


#%%
#Ques-1

list1=[]
fp=open('dummy_text.txt','r')
for line in fp:
  content=fp.readline()
  line1=content.rstrip('\n')
  list1.append(line1)
print(list1)
fp.close()


#%%
#Ques-2

array1=[]
fp=open('dummy_text.txt','r')
for line in fp:
     content=fp.readline()
     line1=content.rstrip('\n')
     array1.append(line1)
print(array1)
fp.close()



#%%
#Ques-3


import random
list1=[]
fp=open('dummy_text.txt','r')
content=fp.readlines()
print("\n")
print(random.choice(content))
fp.close()

#%%
#Ques-4

fp=open('dummy_text.txt','r')
fp1=open('dummy_text2.txt','r')
contents=fp.readline()
contents1=fp1.readline()

while(contents!='' and contents1!=''):
     
     print(contents)
     print(contents1)
     
     contents=fp.readline()
     contents1=fp1.readline()

fp.close()
fp1.close()




#%%
#Ques-5

alpha='A'
for i in range(0,26):
    
    alpha=chr(ord(alpha)+1)
    fp=open(alpha+'.txt','x')


#%%
#Ques-6

letter='A'
a=ord(letter)
while a<90:
    f = open("file3.txt","a")
    for i in range(3):
        f.write(letter)
        a=ord(letter)+1
        letter=chr(a)
        if letter==None:
            f.write(" ")
    f.write("\n")
    f.close()

#%%
#Ques-7
  
import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
a=soup.find("div",{"class":"label-counter"})
print(a.text)

c=soup.findAll("h1")
b=soup.findAll("div",{"class":"maincounter-number"})
list1=[]
for i in c:
 list1.append(i.text)
j=0
for i in b:
 print(list1[j])
 print(i.text)
 j+=1
