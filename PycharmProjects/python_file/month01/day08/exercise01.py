#练习一：定义计算四位整数,每位相加和的函数
#测试：”1234“
def sum(number):
    """
    四位整数的各位数相加
    :param number: 需计算的整数
    :return: 返回4位数的相加和
    """
    result=number%10+number//10%10+number//100%10+number//1000
    return result
result=sum(1234)
print(result)

