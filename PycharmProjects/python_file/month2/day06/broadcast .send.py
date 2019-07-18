"""
广播发送
1、创建udp套接字
2、设置可以发送广播
3、循环向广播地址发送
"""
from socket import *
from time import *
addr=("176.209.103.255",9998)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data="66666"
while True:
    sleep(2)
    s.sendto(data.encode(),addr)