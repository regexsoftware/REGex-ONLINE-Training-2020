#!/usr/bin/env python
# coding: utf-8

# In[21]:


for i in range(6,0,-1):
    for j in  range(i-1):
        print('5',end = " ")
    print()


# In[19]:


for i in range(7,2,-1):
    for j in  range(i-1):
        print(j,end = " ")
    print()


# In[5]:


i = 1
while i<=5:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print()


# In[11]:


for i in range(1,6,1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


# In[14]:


i=1
j=1
k=j
for x in range(1,6):
    for y in  range(i,j):
        k-=1
        print(k,end = " ")
    print()
    i=j
    j+=x
    k=j


# In[42]:


def series(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j)," ", end="")
        print()

def function(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
 
    return res
 
series(7)


# In[43]:


for i in range(1,6):
    for j in range(1,6):
        if j <= i:  
            print(i, end=' ')  
        else:  
            print(j, end=' ')  
    print()


# In[28]:


for i in range(1,9,1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


# In[44]:


rows = 5  
  
    
k= 2 * rows - 2  
 
for i in range(rows, -1, -1):  
     
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  


# In[48]:


n =  7
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1    
    for j in range(0, i + 1):    
        print("* ", end=' ')  
    print(" ")


# In[45]:


for i in range(0, rows):  
     
    for j in range(0, i + 1):  
        print("*", end=' ')  
      
    print(" ")

print()
# For second pattern  
for i in range(rows + 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  


# In[46]:


rows = 5
  
 
for i in range(0, rows):  
  
    for j in range(0, i + 1):  
        print("*", end=' ')  

    print(" ")


# For second pattern  
for i in range(rows, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ") 


# In[1]:


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
 
 
pattern(5)


# In[10]:


def main():
    character = "*"
    rows_number = 5

    if not(character.endswith(" ")):   
        character+= " " 

    for i in range(rows_number):
        print(" "*i+character*(rows_number-i))
    for j in range(1, rows_number+1):
        print(" "*(rows_number-j)+character*j)

if __name__ == "__main__":
    main()


# In[ ]:




