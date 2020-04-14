# Question - 5

'''
Take a list REGex=[1,2,3,4,5,6,7,8,9,0,77,44,15,33,65,89,12]
    - print only those numbers greator then 20
    - then print those numbers those are less then 10 or equal to 10
    - store these above two list in two different list.

'''
a=[] #list of those numbers greater then 20
b=[] #list of those numbers those are less then 10 or equal to 10

REGex=[1,2,3,4,5,6,7,8,9,0,77,44,15,33,65,89,12]
for i in REGex:
    if i>20:
        a.append(i)
    elif i <= 10:
        b.append(i)
        
print(a) 

print(b)
