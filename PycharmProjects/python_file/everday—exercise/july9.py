import math
# print(sum(range(101)))

# dict={"k0":0,"k1":1,"k2":2,"k3":3,"k4":4,"k5":5,"k6":6,"k7":7,"k8":8,"k9":9,"k10":10}
# for item in dict:
#     if int(item[1:])>5:
#        print (dict[item])

# while True:
#     number = int(input("请输入数字："))
#     if math.sqrt(number)<50:
#         break

# list=[item for item in range(2000,3201) if item%7==0 and item%5!=0]
# print(list)

# list=[item for item in range(100,1000) if item==(int(str(item)[0])**3+int(str(item)[1])**3+int(str(item)[2])**3)]
# print(list)

# def fun(list):
#     list02=[]
#     for item in list:
#         item+=1
#         list02.append(item)
#     return  list02
# list=[1,5,7,9,10,34]
# print(fun(list))

list=[8,19,21,22,7,6,1,12,15]
list01=[]
list02=[]
for item in list:
    if item%2==0:
        list01.append(item)
    else:
        list02.append(item)
list01.sort(reverse=True)
list02.sort()
list03=[]
for item in range(min(len(list01),len(list02))):
    list03.append(list01[item])
    list03.append(list02[item])
if len(list01)<len(list02):
    for item in range(len(list01),len(list02)):
        list03.append(list02[item])
if len(list01)>len(list02):
    for item in range(len(list02),len(list01)):
        list03.append(list01[item])
print(list03)
