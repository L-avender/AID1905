#功能
"""
【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
      服务端循环接受客户端请求，客户端发起操作命令
【2】 客户端可以查看服务器文件库中有什么文件。
      服务器文件库：建一个文件库，查询文件库，返回文件库里的文件名，允许访问文件
      客户端：发送查看请求，收到全部文件名
【3】 客户端可以从文件库中下载文件到本地。
      客户端读文件，将文件写入到新的文件中
【4】 客户端可以上传一个本地文件到文件库。
      服务端读文件，写入新的文件中保存
【5】 使用print在客户端打印命令输入提示，引导操作
"""
#框架分析
"""
#1.技术点确定
   #并发模型：多线程并发
   #数据传输：tcp传输
#2.结构设计
   #将基本文件操作功能封装为类
#3.功能模块
   #第一步：搭建网络通信模型
   #查看文件列表
   #下载文件
   #上传文件
   #客户端退出
#4.协议确定
    # Ｌ：请求文件列表
    # Ｑ：退出
    # Ｇ：下载文件
    # Ｐ：上传文件
"""

"""
ftp 文件服务器，服务端
env : python3.6
多进程/线程并发 socket
"""
from socket import *
from threading import Thread
import sys,os
import time

# 全局变量
HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST,PORT)
FTP = "folder" # 文件库位置


# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表，下载，上传，退出处理
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 拼接文件
        filelist = ""
        for file in files:
             if "." in file:
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_quit(self):
        self.connfd.send("退出进程".encode())

    def do_get_file(self):
        pass
    def do_put_file(self):
        pass



    # 循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data =="L":
                self.do_list()
            if data=="Q":
                self.do_quit()
            if data=="G":
                self.do_get_file()
            if data=="P":
                self.do_put_file()


# 搭建网络服务端模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8080...")

    # 循环等待客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit('退出服务器')
        except Exception as e:
            print(e)
            continue

        # 创建线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start() # 运行run


if __name__ == "__main__":
    main()