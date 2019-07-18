"""
ftp 文件服务，客户端
"""
from socket import *
import sys

# 服务器地址
ADDR = ('127.0.0.1',8080)

# 客户端文件处理类
class FTPClient:
    """
    客户端处理 查看，上传，下载，退出
    """
    def __init__(self,sockfd):
        self.sockfd = sockfd

    # 获取文件库中文件列表
    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次接收文件字符串
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    def do_get_file(self):
        pass
    def do_put_file(self):
        pass
    def quit(self):
        self.sockfd.send(b'Q')
        data = self.sockfd.recv(128).decode()
        print (data)
        self.sockfd.close()
        sys.exit('谢谢使用')


# 链接服务器
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 实例化对象，调用文件处理方法
    ftp = FTPClient(sockfd)

    # 循环发送请求
    while True:
        print("\n=========命令选项=========")
        print("*****      list      *****")
        print("*****    get file    *****")
        print("*****    put file    *****")
        print("*****      quit      *****")
        print("===========================")

        cmd = input("输入命令: ")
        if cmd.strip() == 'list':
            ftp.do_list()
        if cmd.strip() == 'get file':
            ftp.do_get_file()
        if cmd.strip()=="put file":
            ftp.do_put_file()
        if cmd.strip()=="quit":
            ftp.quit()



if __name__ == "__main__":
    main()