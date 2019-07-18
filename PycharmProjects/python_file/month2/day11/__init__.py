"""
select tcp服务
重点代码

思路分析：
1. 将关注的IO放入到监控列表
2. 当IO就绪时会通过select返回
3. 遍历返回值列表，得知哪个IO就绪进行处理
"""
from socket import *
from select import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9527))
s.listen(5)

rlist=[s]
wlist=[]
xlist=[]

rs,ws,xs=select(rlist,wlist,xlist)

while True:
    for r in rs:
        if r is s:
            c,addr=r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            r.send(b"ok")
    for w in ws:
        pass

    for x in xs:
        pass
