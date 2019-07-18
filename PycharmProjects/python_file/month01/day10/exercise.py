class Student:
    def __init__(self,name,age,score,sex):
        self.name=name
        self.age=age
        self.score=score
        self.sex=sex
    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s"%(self.name,self.age,self.score,self.sex))
list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("周芷若",25, 62, "女"),
    Student("张无忌",25, 98, "男"),
]
# print(len(list01))
# def find04():
#     for item in list01:
#         if item.age>=30:
#            count+=1
#     return count
def find04():
    for item in list01:
        item.score=0

    return
def get_name():
    list02=[]
    for item in list01:
        list02.append(item.name)
    return list02
def find05():



