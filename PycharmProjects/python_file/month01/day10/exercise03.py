"""
练习：定义对象计数器
定义老婆类，创建3个老婆对象
可以通过类变量记录老婆对象个数
可以通过类方法打印老婆对象个数
"""
class Wife:
    total_wife = 0
    @classmethod
    def print_total_wife(cls):
        print("老婆对象个数是%d"% Wife.total_wife)
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Wife.total_wife += 1
    def play(self):
        print("做饭的是%s"%(self.name))

wi01=Wife("lili","24")
wi02=Wife("lala","23")
wi03=Wife("honghong","22")
wi01.play()
wi02.play()
wi03.play()
print(Wife.total_wife)
print("老婆对象个数%d"% Wife.total_wife)