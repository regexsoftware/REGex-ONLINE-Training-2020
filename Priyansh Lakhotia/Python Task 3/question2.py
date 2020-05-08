# Question 2
'''
Lets say you have a string “hello this world @2020!!! ”
    ○ Remove the punctuation like [“@!#$%&*()”] from the string
        ■ Final output should be without the punctuation
            ● “hello this world 2020”
'''
#Solution :
s = ("hello this world @2020!!! ")
final_output=('')
punc = ['@', '!', '#', '$', '%', '&', '*', '(', ')']
for i in s:
    if i not in punc:
        final_output = final_output + i
print (final_output)
