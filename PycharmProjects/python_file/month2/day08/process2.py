from  multiprocessing import *
from time import *
import os
def fun01():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def fun02():
    sleep(3)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())

def fun03():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())
things=[fun01,fun02,fun03]
job=[]
for fun in things:
    p=Process(target=fun)
    job.append(p)
    p.start()
for i in job:
    i.join()