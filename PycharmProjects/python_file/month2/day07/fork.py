import os
import time

a=1
pid=os.fork()
if pid<0:
    print("Create process failed")
elif pid==0:
    time.sleep(3)
    print("The new process")
    print (a)
    a=1000
else:
    time.sleep(4)
    print("The old process")
    print(a)
    a=4
print("Fork test over")
print(a)
