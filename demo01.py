#练习：使用range生成1--10之间的数字，将数字的平方存入list01中
#将list01中所有的奇数出入lisy02中
#将list01中所有的偶数数出入lisy03中
#将list01中所有的偶数大于5的数字增加1后存入lisy04中
#list01=[] 创建列表01vc
#for item in range(1,11): 在range中取值
  #  list01.append(item ** 2)  将值放入列表1中
list01 = [item ** 2 for item in range(1,11)]

#list02=[] 创建列表02
#for itme in list01: 在列表01取值
# if itme % 2==1:    取值为奇数
 #    list02.append(itme)  将取值放入列表02中
list02 = [itme for itme in list01 if itme % 2==1]
print(list02
      )
#list03=[]
#for item in list01:
 #   if item % 2==0:
  #      list03.append(item)
   #     print(list03)
list03=[item for item in list01 if item %2==0]
print(list03)
#将list01中所有的偶数大于5的数字增加1后存入lisy04中
list04=[]
for item in list01:
    if item % 2==0 and item>5:
        list04.append(item+1)
print(list04)


