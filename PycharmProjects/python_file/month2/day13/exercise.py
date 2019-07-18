"""
编写接口函数，从端口输入名称获取端口运行状态中的地址值
"""
import re


def get_address(string):
    f = open("exc.txt")
    while True:
        data = ""
        for line in f:
            data += line
            if line == "\n":
                break
        if not data:
            break
        obj = re.match(string, data)
        if obj:
            pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/\d+"
            obj = re.search(pattern, data)
            return obj.group()
    return "没有该端口"

if __name__=="__main__":
   while True:
    string=input("请输入端口：")
    if string=="":
        break
    print(get_address(string))







