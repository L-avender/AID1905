class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
    def print(self):
        print("查找的目标技能：编号是%d,技能名称是%s,攻击加成是%d,持续时间是%d"%(self.id,self.name,self.atk_ratio,self.duration))
list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]

def find01():
    for item in list_skill:
        if item.name=="葵花宝典":
            return  item
re=find01()
re.print()

def find02():
    for item in list_skill:
        if item.id==101:
            return  item
re=find02()
re.print()

def find03():
    for item in list_skill:
        if item.duration>0:
            return item
re=find03()
re.print()

def condition01(item):
    return item.name=="葵花宝典"
def condition02(item):
    return item.id==101
def condition03(item):
    return item.duration>0

def find(func_condition):
    """
        通用的查找方法
    :param func_condition: 查找条件,函数类型.
            函数名(变量) --> 返回值bool类型
    :return:
    """
    for item in list_skill:
        # "多态":调用父(变量),执行子(具体函数).
        #       不同子类重写父类方法,执行逻辑不同.

        if func_condition(item):
           return item
re=find(condition01)
re.print()







