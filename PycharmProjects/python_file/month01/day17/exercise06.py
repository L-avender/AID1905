"""
    测试 通用模块list_helper
"""
from common.list_helper import *
class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


def condition01(item):
    return item.atk_ratio > 6


def condition02(item):
    return 4 < item.duration < 11


def condition03(item):
    return len(item.name) > 4 and item.duration < 6


generate01 = ListHelper.find_all(list_skill, condition01)
for item in generate01:
    print(item)

# 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
# 案例:查找名称是"葵花宝典"的技能.
#     查找编号是101的技能.
#     查找持续时间大于0的技能.

# 建议:
# 1. 现将所有功能实现
# 2. 封装变化(将变化点单独定义为函数)
#    定义不变的函数
# 3. 将不变的函数转移到list_helper.py中
# 4. 在当前模块测试

"""
def find01():
    for item in list_skill:
        if item.name =="葵花宝典":
            return item

def find02():
    for item in list_skill:
        if item.id ==101:
            return item

def find03():
    for item in list_skill:
        if item.duration > 0:
            return item
"""


def condition04(item):
    return item.name == "葵花宝典"


def condition05(item):
    return item.id == 101


def condition06(item):
    return item.duration > 0


"""
def find(func_condition):
    for item in list_skill:
        # if item.duration > 0:
        # if condition06(item):
        if func_condition(item):
            return item

print("-------")
re = find(condition04)
print(re)
"""

re = ListHelper.find_single(list_skill, lambda item:item.duration > 0 and item.id==101)
print(re)
print("--------")

def condition07(item):
    return len(item.name)>4

def condition08(item):
    return item.duration<=5

generate01 = ListHelper.find_count(list_skill, condition07)
print(generate01)