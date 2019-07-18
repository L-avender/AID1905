from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9527))
s.listen(5)
def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"ok")

while True:
    c,addr=s.accept()
    print("Connect from",addr)
    handle(c)
