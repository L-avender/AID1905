"""
   练习：定义 根据成绩计算等级的函数

"""
def get_level_score(score):
    """
    根据成绩计算等级
    :param score:学生成绩
    :return:返回学生成绩的等级
    """
    if score > 100 or score < 0:
       return ("输入有误")
    if 90 <= score:
       return ("优秀")
    if 80 <= score:
       return ("良好")
    if 60 <= score:
       return("及格")
    return("不及格")
str1=get_level_score(99)
print(str1)
