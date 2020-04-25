# --------------------------- LATE NIGHT TASK ----------------------------------



# Ques -> You have to make a Script to send "Hi" 5 times to a friend.

# Ans :

import webbrowser as web
import pyautogui as pg
import time

count = 0
while count<5:                   # To send a message 5 times
    
    web.open('https://web.whatsapp.com/send?phone=number,&text=Hi')        # Open Whatsapp Web with a perticular contact
    # phone = contact number of a reciever with a country code. -> eg: +91xxx-xxx-xxxx
    
    time.sleep(15)               # To wait for the Whatsapp to open completely (in case there's any internet issue)
    pg.press('enter')            # To send the message by automatically pressing "Enter" on the keyboard.
    time.sleep(3)                # To wait for the message to send so that the tab can be closed easily(without asking the user's permission)
    pg.hotkey('ctrl','w')        # To close the tab
    count += 1
    
web.open('http://web.whatsapp.com')        # To finally open Whatsapp Web so that you can check the messages.

# --- We can delete all the time module's code if there's no issue of internet. ---




# Ques -> You have to make a script to run a program and send a same message to 6 persons through a script.

# Ans :

import webbrowser as web
import pyautogui as pg
import time


# List of all the numbers you want to send meassage to 
# NOTE : Each number should have +91 before the 10 digit number, -> eg: +91xxx-xxx-xxxx
numbers = ['number1', 'number2', 'number3', 'number4', 'number5', 'number6']   


url1 = 'https://web.whatsapp.com/send?phone='
url2 = ',&text=Hi' 

for i in numbers:                   
    web.open(url1+i+url2)        # Open Whatsapp Web with a perticular contact
    time.sleep(15)               # To wait for the Whatsapp to open completely (in case there's any internet issue)
    pg.press('enter')            # To send the message by automatically pressing "Enter" on the keyboard.
    time.sleep(3)                # To wait for the message to send so that the tab can be closed easily(without asking the user's permission)
    pg.hotkey('ctrl','w')        # To close the tab
    
web.open('http://web.whatsapp.com')        # To finally open Whatsapp Web so that you can check the messages.

# --- We can delete all the time module's code if there's no issue of internet. ---


