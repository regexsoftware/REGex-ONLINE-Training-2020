
'''
Late Night Task

You have to Make a WhatsApp Script

-> Till now we have seen about sending message in WhatsApp through Python using Webbrowser.


-> run a program and send a same message to 6 persons through a script.


-> Script to send "Hi" 5 times to a friend 




'''

import webbrowser as wb
import time
import  pyautogui as g
send = False
print(time.ctime())

friends = ['917866555***', '9198712*****', '9198634*****', '91799*******', '9187464*****', '9197667*****']

for n in friends:
    
    number = int(n)
    message = ("hi")
    YourTime = ("00:45:00")
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
        