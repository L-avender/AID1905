# 练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
#   第一列变成第一行
#   第二列变成第二行
#   第三列变成第三行
def transposition(list_target):
    """

    :param list_target:
    :return:
    """
    for c in range(1, len(list_target)):
     for a in range(c, len(list_target[c])):
         list_target[a][c - 1], list_target[c - 1][a]= list_target[c - 1][a], list_target[a][c - 1]
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
transposition(list01)
print(list01)



