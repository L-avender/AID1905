tuple=([1,1,2],[2,5,6,8],[1,2,3,4,6])
print(max(tuple,key = lambda item:len(item)))
class Enemy:
    def __init__(self,name,atk,defense,hp):
        self.name=name
        self.atk=atk
        self.defense=defense
        self.hp=hp
    def __str__(self):
        return "敌人数据是:%s,%d,%d,%d" % (self.name, self.atk, self.defense,self.hp)
list_enemy=[Enemy("灭霸",101,100,999),
            Enemy("焰灵姬",80,2,20),
            Enemy("卫庄",90,80,666)]

for item in map(lambda item:(item.name,item.atk,item.hp),list_enemy):
    print (item)
for item in filter(lambda item:item.atk>100 and item.hp>0,list_enemy):
    print(item)
for item in sorted(list_enemy,key = lambda item:item.defense,reverse = True):
    print(item)

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