# Question 2
'''
Lets say I have some string "hello this side regex"
    Find out the count of the total vowels
    vowels - ['a','e','i','o','u']
'''

vowels = ['a','e','i','o','u']
text = ("hello this side regex")
total_vowels = 0
for i in text:
    if i in vowels:
        total_vowels = (total_vowels + 1)
print (total_vowels)
