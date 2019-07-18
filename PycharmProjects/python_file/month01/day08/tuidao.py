# 练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
#   第一列变成第一行
#   第二列变成第二行
#   第三列变成第三行
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
# item=list01[0][0]
# print(item
#       )
list03=[]
for c in range(len(list01)):
    list02=[]
    list03.append(list02)
    for a in range(len(list01[0])):
        list02.append(list01[a][c])
print(list03)


