# xb=float((input("请输入小贝的体重：")))
# xy=float((input("请输入小鱼的体重：")))
# xl=float((input("请输入小螺的体重：")))
# dict={}
# dict["小贝"]=xb
# dict["小鱼"]=xy
# dict["小螺"]=xl
# list=[]
# for name,weight in dict.items():
#     list.append((weight,name))
# list.sort()
# print(list)

list1=[0,1,2,3,4,5,6]
list2=[0,1,2,3,4,5,6]
list3=[0,1,2,3,4,5,6]
list4=[0,1,2,3,4,5,6]
list5=[]
for a in range(7):
    for b in range(7):
        for c in range(7):
            for d in range(7):
                if list1[a]+list2[b]+list3[c]+list4[d]==6:
                    list5.append((list1[a],list2[b],list3[c],list4[d]))
print(len(list5))


