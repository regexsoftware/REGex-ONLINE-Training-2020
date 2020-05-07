# Question-3

'''
3. ###### You have to run your Program at 9:00am. Date: 14th April 2020.
    #HINT:
        # You have to use datetime Module or time module..
        # You have to convert your output in #LIST_FORMAT
        # [ '2020-04-13' , '17:11:01.952975' ]
        # you can use this with the helf of IF/Else statement
'''



import datetime
x = datetime.datetime.now()

# converting the time to a list
a = str(x)
ls = a.split(" ")



# running program at 09:00 AM Date 14th April 2020
import time
while True:
    x = time.ctime()
    ls = x.split(" ")
    print(ls)
    if ls == ['Wed', 'Apr', '15', '15:08:03', '2020']:
        print("This is the time")
        break
    else:
        continue
        
    
