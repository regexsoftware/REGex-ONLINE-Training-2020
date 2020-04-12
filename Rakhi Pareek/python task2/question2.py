# Question 2
'''
Let say I have, some string "hello this side regex"
    Find out the count of the total vowels
    vowels - ['a','e','i','o','u']
'''

vowels = ['a', 'e', 'i' ,'o', 'u']

text = ("hello this side regex")
count = 0
for i in text:
    if i in vowels:
        count = (count + 1)
print (count)
