# 3. 自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
#     字符串："　校 训：自　强不息、厚德载物。　　"
#     查找空格的数量
#     删除字符串前后空格
#     删除字符串所有空格
#     查找"载物"的位置
#     判断字符串是否以"校训"开头.
string=" 校 训：自 强不息、厚德载物。  "
#     查找空格的数量
print(string.count(" "))
#     删除字符串前后空格
print(string.strip())
#     删除字符串所有空格
print(string.replace(" ",""))
#     查找"载物"的位置
print(string.find("载物"))
#     判断字符串是否以"校训"开头.
print(string.startswith("校训"))