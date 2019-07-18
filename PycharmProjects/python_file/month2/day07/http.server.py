"""
httpserver v1.0
基本要求：1.获取来自浏览器的请求
　　　　　2.判断如果请求内容是/ 将index.html返回给客户端
　　　　　3.如果请求的是其他内容则返回404　
"""

# from socket import *
#
# #　客户端(浏览器)处理
# def request(connfd):
#     # 获取请求将请求内容提取出来
#
#     # 判断是/ 则返回index.html 不是则返回404
#     if info == '/':
#
#     else:


#
# #　搭建ｔｃｐ网络
# sockfd = socket(AF_INET,SOCK_STREAM)
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sockfd.bind(('0.0.0.0',8000))
# sockfd.listen(3)
# while True:
#     connfd,addr = sockfd.accept()
#     request(connfd) #　处理客户端请求