# 练习:定义在控制台中打印一维列表的函数.
# 例如：[1,2,3]-->1 2 3  每个元素一行
def print_list(list_target):
    """
    打印一维列表
    :param list_target: 目标列表
    :return:
    """
    for item in list_target:
        print(item)
list02=[1,2,3,4]
print_list(list02)
