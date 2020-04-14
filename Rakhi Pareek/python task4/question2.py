# Question-2

'''
Write a program to replace each string with an integer value in a given list of strings.
The replacement integer value should be a sum of AScci values of each character of type
corresponding string........
    LIST: ['GAnga', 'Tapti', 'Kaveri', 'Yamuna', 'Narmada' ]
'''

LIST = ['GAnga', 'Tapti', 'Kaveri', 'Yamuna', 'Narmada' ]

ls = []
add = 0
for i in LIST:
    for j in i:
        add = add + ord(j)
    ls.append(add)
print(ls)
