"""
    参照day10/exercise02.py
    完成下列练习
"""
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]
# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成
def get_skill(iterable_targe):
    for item in iterable_targe:
        if item.duration<6 and len(item.name)>4:
            yield item.name
re=get_skill(list_skill)
for item in re:
    print(item)
re=(item.name for item in list_skill if item.duration<6 and len(item.name)>4)
for item in re:
    print(item)
