"""
fork-server.py  基于fork的多进程并发重点

1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建新的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""

from socket import *
import os
import  signal
#全局变量
HOST="0.0.0.0"
POPT=9527
ADDR=(HOST,POPT)

#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#处理僵死进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888.....")

#具体处理客户端请求
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()

while True:
    #循环处理客户端连接
    try:
        c,addr=s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

#创建子进程处理客户端事物
    pid=os.fork()
    if pid==0:
        s.close()
        handle(c)#处理具体事物
    else:
        c.close()