# Question-1

'''
Write a Program to print new list which contains all the first Characters of strings present in a
list.....
    LIST_STATES = ["GOA","RAJASTHAN","KARNATAKA","GUJRAT","MANIPUR","MADHYA PRADESH"]

'''

LIST_STATES = ["GOA","RAJASTHAN","KARNATAKA","GUJRAT","MANIPUR","MADHYA PRADESH"]


new_list = []

for i in LIST_STATES:
    new_list.append(i[0])
    
    
print(new_list)

