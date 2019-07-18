"""
fork-server-process.py  基于process的多进程并发重点

1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建新的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""
from threading import *
from socket import *
import sys
#全局变量
HOST="0.0.0.0"
POPT=9527
ADDR=(HOST,POPT)

#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

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
#循环等待客户端链接
while True:
    try:
        c,addr=s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        sys._exit("退出服务器")
    except Exception as e:
        print(e)
        continue

#创建线程处理客户端事物
    p=Thread(target=handle,args=(c,))
    p.setDaemon(True)
    p.start()
