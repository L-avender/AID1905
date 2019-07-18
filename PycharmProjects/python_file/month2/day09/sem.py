from multiprocessing import *
from  time import *
import  os


#创建信号量
sem=Semaphore(3)

#任务函数