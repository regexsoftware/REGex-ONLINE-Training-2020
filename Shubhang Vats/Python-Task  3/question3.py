# Question 3

'''
You have a list with words - [“Apple”, “banana”, “cat”, “REGEX”,”apple”]
    ○ Sort words in Alphabetical order
        ■ If you get output, like [Apple, apple, banana]
            ● How has it happened?
'''

ls = ["Apple", "banana", "cat", "REGEX","apple"]
sortls = sorted(ls)
print (sortls)



'''
This happens because we have not specified the parameter key and default this is
as the priority order of A then a
'''

