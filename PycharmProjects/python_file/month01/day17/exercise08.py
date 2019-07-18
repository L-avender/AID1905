"""3. 定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
"""
from common.list_helper import *
class Enemy:
    def __init__(self,name,atk,defense,hp):
        self.name=name
        self.atk=atk
        self.defense=defense
        self.hp=hp
    def __str__(self):
        return "敌人数据是:%s,%d,%d,%d" % (self.name, self.atk, self.defense,self.hp)
list_enemy=[Enemy("灭霸",0,100,999),
            Enemy("焰灵姬",0,2,20),
            Enemy("隐蝙", 0, 80, 0),
            Enemy("卫庄",90,80,666),]


print(ListHelper.find_single(list_enemy,lambda item:item.name=="灭霸"))

re=ListHelper.find_all(list_enemy,lambda item:item.atk>10)
for item in re:
    print(item)

print(ListHelper.find_count(list_enemy,lambda item:item.hp>0))

print(ListHelper.True_Flase(list_enemy,lambda item:item.name=="成昆"))

print(ListHelper.True_Flase(list_enemy,lambda item:item.atk<5 or item.defense<10))

print(ListHelper.all_sum(list_enemy,lambda item:item.hp))

print(ListHelper.screen(list_enemy,lambda item:(item.name,item.atk)))

print(ListHelper.get_biggest(list_enemy,lambda item:item.defense))
"""
作业
1.三合一（闭包）
2.当天练习独立完成(list_helper.py)
3.在list_helper.py中新增以下功能：
    (1)获取最小值
    (2)降序排列
    (3)根据指定条件删除元素
       案例:在敌人列表中，删除所有死人.
       案例:在敌人列表中，攻击力小于50的所有敌人.
       案例:在敌人列表中，防御力大于100的所有敌人.
4. 阅读"面向对象答辩优胜者"文档.
   总结出属于自己的话术，以便就业准备简历时使用(介绍项目).
"""
# def least():
#     least=list_enemy[0]
#     for item in list_enemy:
#         if least.hp>item.hp:
#             least=item
#     return least
# print(least())
print(ListHelper.least(list_enemy,lambda item:item.defense))

for item in ListHelper.descending_order(list_enemy,lambda item:item.hp):
    print(item)
print("-----")

for item in ListHelper.delete(list_enemy,lambda item:item.atk<50):
    print(item)