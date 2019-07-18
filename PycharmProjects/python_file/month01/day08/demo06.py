"""
函数参数
    形式参数
"""
# def fun01(a=100,b=0,c=0,d=100):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# fun01(b=2,c=3)
#缺省（默认）参数：如果实参不提供，可以使用默认值(必须从右到左依次存在)

#关键字实参+缺省形参：调用者可以随意传递参数

#位置形参

#星号元组形参:将所有实参合并为一个元组
#让实参个数无限

#命名关键字形参:在星号元组形参以后的位置形参
# def fun04(a,*args,b):
#     print(a)
#     print(args)
#     print(b)
# fun04(1,2,3,4,b=2)

#双星号字典形参:实参可以传递数量无限的关键字实参
#将实参合并为字典
def fun06(**kwargs):
    print(**kwargs)

fun06(a=1,b=2)

# def fun03(*args):
#     print(args)
# fun03()
#练习：定义函数，数值相加的函数。
# def fun04(*args):
#     return sum(args)
# print(fun04(1,2,3))
# #练习：定义函数：根据小时，分钟，秒，计算总秒数
# def count_seconds(hours=0,minutes=0,seconds=0):
#     """
#     根据小时，分钟，秒，计算总秒数
#     :param hours: 小时
#     :param minutes: 分钟
#     :param seconds: 秒数
#     :return: 返回
#     """
#     result=hours*60*60+minutes*60+seconds
#     return result
# result=count_seconds(hours=1)
# print(result)
