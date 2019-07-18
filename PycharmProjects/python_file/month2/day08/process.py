"""
multiprocessing   模块创建进程
1.编写进程
2.生成进程对象
3.启动进程
4.回收进程
"""
import multiprocessing as mp
from  time import *
def fun():
    print("开始一个进程")
    sleep(5)
    print("子进程结束")
p=mp.Process(target=fun)
p.start()
print("父进程做点事")
p.join()

