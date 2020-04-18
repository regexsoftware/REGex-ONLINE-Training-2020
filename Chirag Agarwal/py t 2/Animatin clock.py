import time
for i in range(5):
    x = str(time.ctime())
    y = x.split(" ")
    print(y[3])
    time.sleep(1)
