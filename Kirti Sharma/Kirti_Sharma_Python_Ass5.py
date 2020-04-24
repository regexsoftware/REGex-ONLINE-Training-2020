# Ques1 : -> Make a use of Time Module and for Loop
        # -> Output Should be :
            # Loading.
            # Loading..
            # Loading...
            # Loading....
            # Loading.....
# Here it shows you 5 output but you have to print only "Loading....." in animated form.
# Ans:
import time
print('Loading', end = '')
count = 0
while count<5:
    time.sleep(1)
    print('.', end = '')
    count += 1



# Ques2 : Difference between Return and Yield ?
# Ans : In Python, yield turns a function into a generator that yields its results iteratively(as a sequence) to the calling function.
        # Essentially you call the function multiple times and get one result back each time. 
        # Return just hands an object (default value None), but can be any thing(e.g. a list)
        # back to the calling program and discards all internal state in the function.



# Ques3 : 3 Make digital Clock and run it for 5 sec.
        # Output:
        # 16:39:08
        # 16:39:09
        # 16:39:10
        # 16:39:11
        # 16:39:12
# Ans : 
import datetime
import time
count = 0
while count<5:
	x = datetime.datetime.now().time().replace(microsecond=0)         # "time.replace(microseconds=0)" will not print microseconds 
	print(x)
	time.sleep(1)
	count += 1



# Ques4 : Add anything in tuple.. example: (1,2,3,4) -> new tuple (1,2,3,4,5)
# Ans : 
a = tuple(map(int, input('Enter elements of tuple in a single line separated by space : ').split()))          # Will take the input in tuple
print('Tuple is : ',a)                                                                          
b = int(input('Enter number you want to add in tuple : '))
a = list(a)
a.append(b)
a = tuple(a)
print('New tuple is :',a)


# Ques5 : WhatsApp texting using webbrowser Lib.

import webbrowser                  # for opening whatsapp web using the default browser
import pyautogui as pg             # for automate the movement and clicks of keyboard and mouse.
import time

webbrowser.open('https://web.whatsapp.com/send?phone=number&text=HEY BUDDY!!', new=2, autoraise=True)
# phone = "number with country code to which you want to send the message" -> eg: +91 xxx-xxx-xxxx 
# text = "text that you want to send" -> eg: send = HEY!! (this will show "HEY" on the sender's message box but will not send it)

time.sleep(15)                      # In case whatsapp'll take time to open due to internet connectivity.

pg.press('enter')                   # This will press "enter" on the keyboard & message have been send.