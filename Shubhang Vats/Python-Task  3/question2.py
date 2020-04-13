# Question 2
'''
Let’s say you have a string “hello this world @2020!!! ”
    ○ Remove the punctuation like [“@!#$%&*()”] from the string
        ■ Final output should be without the punctuation
            ● “hello this world 2020”
'''

s = ("hello this world @2020!!! ")
news=('')
punc = ['@', '!', '#', '$', '%', '&', '*', '(', ')']
for i in s:
    if i not in punc:
        news = news + i
        

print (news)
