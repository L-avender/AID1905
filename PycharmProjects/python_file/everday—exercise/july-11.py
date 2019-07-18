import random
def fun():
    list01=random.sample(range(100),10)
    list02=[item for item in list01]
    list02.remove(min(list01))
    return ("原列表为：",list01,"修改后列表为：",list02)
print(fun())

def fun2(str):
    list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z","a"]
    str1=""
    for item in str:
       item=list[list.index(item)+1]
       str1+=item
    return str1
print(fun2("heallz"))

def fun1(func):
    print("=======1")
    def fun2(*args, **kwargs):
        print("======2")
        return func()
    return fun2

@fun1 #fun3=fun1(fun3)----fun3=fun2
def fun3():
		print("===3")

fun3()