import random
print_number=int(input("请输入您要打印几注："))
count=0
while count<print_number:
    red=random.sample(range(1,34),6)
    print("红色球：",sorted(red))
    blue=random.sample(range(1,17),1)
    print("蓝色球：", blue)
    count+=1
print("出票成功")

