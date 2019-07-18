# 练习2:["无忌","赵敏","周芷若"]  [101,102,103]
#  {"无忌":101,"赵敏":102,"周芷若":103}
list01=["无忌","赵敏","周芷若"]
list02=[101,102,103]
dict01={}
for a in range(len(list01)):
   dict01[list01[a]]=list02[a]

print(dict01)
# 需求：字典如何根据value查找key
# 解决方案１:键值互换
# dict02 = {value: key for key, value in dict01.items()}
# print(dict02)
# print(dict02[101])
for i in range(len(list01)):
    print(i)