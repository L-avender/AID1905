# 练习:将下列代码，定义到函数中，再调用一次.
def print_jz(a,b,char):
    """
    打印矩阵
    :param a: 行
    :param b: 列
    :param char: 字符串
    :return:
    """

    for r in range(a):
        for c in range(b):
            print(char, end=" ")
        print()
print_jz(4,5,"#")
