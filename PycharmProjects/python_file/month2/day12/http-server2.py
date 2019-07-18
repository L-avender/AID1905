"""
httpserver v2.0
env: python3.6
io多路复用 和 http训练
"""

from socket import *
from select import *

# 具体功能实现
class HTTPServer:

    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)
        self.creat_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def creat_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.sockfd.bind(self.address)

    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port is %d"%self.port)
        self.select()

    def select(self):
        self.rlist.append(self.sockfd)
        wlist = []
        xlist = []
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self,connfd):
        request = connfd.recv(1024)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line=request.splitlines()[0]#将字节串按行切割
        print(request_line)
        info=request_line.decode().split(" ")[1]
        print(connfd.getpeername(),":",info)

        if info=="./" or info[-5:]==".html":
            self.get_html(info,connfd)

        else:
            self.get_data(info,connfd)


    def get_html(self,info,connfd):
        if info == '/':
           filename=self.dir+"index.html"

        else:
           filename = self.dir + info

        try:
            fd=open(filename)
        except Exception:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry.....</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            connfd.send(response.encode())

    def get_data(self,info,connfd):
        pass


# 用户使用HTTPServer

if __name__ == "__main__":
    """
    通过 HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 9527
    DIR = './static' # 网页存储位置

    httpd = HTTPServer(HOST,PORT,DIR) # 实例化对象
    httpd.server_forever() # 启动服务