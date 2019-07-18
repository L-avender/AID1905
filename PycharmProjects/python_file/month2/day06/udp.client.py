"""
udp.client.py  udp客户端流程
"""
from socket import *
import struct
#服务器地址
arrd=("176.209.103.5",9527)
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#循环收发消息
while True:
    id=int(input("请输入学生编号："))
    name=str(input("请输入学生姓名："))
    age=int(input("请输入学生年龄："))
    scord=float(input("请输入学生成绩："))
    sockfd.sendto(struct.pack("i4sif",id,name.encode(),age,scord),arrd)
    msg, addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())
#关闭套接字
sockfd.close()