# 3. 定义在控制台中打印二维列表的函数
# [
#     [1,2,3,44],
#     [4,5,5,5,65,6,87]
#     [7,5]
# ]
#
# 1 2 3 44
# 4 5 5 5 65 6 87
# 7 5
def print_list(list_target):
    """
    打印二位列表
    :param list_target: 目标列表
    :return:
    """
    for a in list_target:
      for c in a:
          print(c,end=" ")
      print()
list01=[[1,2,3,44],
   [4,5,5,5,65,6,87],
  [7,5],
        [4,5,6,7]]
print_list(list01)