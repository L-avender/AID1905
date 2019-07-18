#练习：记录一个函数的执行次数
a=0
def fun01():
    global a
    a+=1
fun01()
fun01()
print("fun01调用了%d次"%a)
