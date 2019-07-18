"""
    练习:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
    15:35
"""
def jude_item_equal(list_target):
    """
    判断列表中元素是否具有相同的
    :param list_target: 目标列表
    :return: 返回结果，有重复返回True；没有重复返回False
    """
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False
list01=[1,2,3,4,5,6]
print(jude_item_equal(list01))
