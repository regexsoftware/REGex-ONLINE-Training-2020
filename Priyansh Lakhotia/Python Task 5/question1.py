# Question-1

'''
1. Hint:
    -> Make a use of Time Module and for Loop
    -> Output Should be :
            Loading.
            Loading..
            Loading...
            Loading....
            Loading.....
        Here it shows you 5 output but you have to print only "Loading....." in animated form.
'''

#Solution:
import time
print("Loading", end = "")
i = 1
while(i < 6):
    print('.', end = "")
    time.sleep(1)
    i += 1
