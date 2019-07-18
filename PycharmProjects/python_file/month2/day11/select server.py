"""
ｓｅｌｅｃｔ　ｔｃｐ服务
重点代码
思路分析：
１．将关注的ｉｏ放入到监控列表
２．当ｉｏ就绪时会通过ｓｅｌｅｃｔ返回
３．遍历返回值列表，得知那个ｉｏ就绪进行处理
"""

from socket import *
from select import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9527))
s.listen(3)

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)

    for r in rs:
        if r is s:
            c,addr=r.accept()
            print("Connect from",addr)
            rlist.append(r)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b"ok")
            wlist.append(r)
    for w in ws:
        w.send(b"ok")
        wlist.remove(w)
    for x in xs:
        pass