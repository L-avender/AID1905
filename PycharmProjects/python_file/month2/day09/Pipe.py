"""
pipe.py  管道通信
注意：1、multiprocessing中管道通信只能用于有亲缘关系进程中
     2、管道对象在父进程中创建，子进程通过父进程获取
"""


from multiprocessing import *
#创建管道
fd1,fd2=Pipe()


def app1():
    print("启动app 1，请登录")
    print("启动app 2授权")
    fd1.send("启动app 1，请登录")
    data=fd1.recv()
    if data:
        print("登录成功")


def app2():
    data=fd2.recv()    #阻塞等待读取管道内容
    print(data)
    fd2.send(("xyz","123"))