# Question - 5


"""
WhatsApp texting using webbrowser Lib.
"""

#Solution:

import webbrowser as wb
import time
import  pyautogui as g
send = False
print(time.ctime())
number = int(input("Enter the number to send message: "))
message = input("Enter your message")
YourTime = input("Enter time to send message(hh:mm:ss): ")
print(time.ctime())
while(True):
    t = time.ctime()
    str(t)
    a = t.split(" ")
    if a[3] == YourTime:
        send = True
    if send == True:
        print("send")
        send = False
        time.sleep(1)
        url = 'https://wa.me/'+str(number)+'?text='+str(message)
        print(url)
        wb.open(url)
        time.sleep(5)
        g.moveTo(670, 315)
        g.click()
        time.sleep(5)
        g.moveTo(698, 394) # for using watsapp web
        g.click()
        time.sleep(10)
        g.press('enter')
        print("Task Complete")
        break
    
        
