"""
udp.server.py   udp 套接字服务流程
"""
from socket import *
import struct
# def find(data):
#     fd = open("dict.txt", "r")
#     for line in fd:
#         list = line.split(" ", 1)
#         if data == list[0]:
#             return list[1]
#         else:
#             return ("meiyou")
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=("176.209.103.5",9527)
sockfd.bind(server_addr)
#循环收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    data=struct.unpack("i4sif",data)
    print("收到消息：",data)
    # sockfd.sendto("已接受",addr)
#关闭套接字
sockfd.close()