# Question 3

'''
You have a list with words - [“Apple”, “banana”, “cat”, “REGEX”,”apple”]
    ○ Sort words in Alphabetical order
        ■ If you get output, like [Apple, apple, banana]
            ● How has it happened?
'''

#Solution:

ls = ["Apple", "banana", "cat", "REGEX","apple"]
sortls = sorted(ls)
print (sortls)



'''
This happens because as per the ASCII encoding, the CAPITAL LETTERS have a smaller value than the small letters and as such, when arranged in alphabetical order (which uses the ASCII value as its ordering basis), the CAPITAL LETTERS appear first.
'''

