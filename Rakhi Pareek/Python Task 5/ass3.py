
'''

3. Make digital Clock and run it for 5 sec.
    Output:
            16:39:08
                :09
                :10
                :11
                :12
'''
import time


i=0
while i < 5:
    t = time.ctime()
    print(t[11:19])
    time.sleep(1)
    i = (i+1)
