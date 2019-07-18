from time import *
import os

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")
def f1():
    for i in range(3):
        sleep(2)
        print("写代码")
pid=os.fork()
if pid<0:
    print("errore")
if pid==0:
    f1()

else:
    f2()
       