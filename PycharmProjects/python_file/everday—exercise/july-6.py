# dict01={"1":"i","2":"l","3":"y"}
# dict_new=dict([value,key] for key,value in dict01.items())
# print(dict_new)

import random
def fun():
    result=random.randint(0,100)
    n=0
    while True:
        guess_number=int(input("请输入你的猜想数字："))
        if type(guess_number)!=int or  guess_number<0 or guess_number>100:
            print("输入错误，请输入0-100以内的整数")
        if 100>=guess_number>result:
           n+=1
           print("猜大了，请重新输入")
        if 0<=guess_number<result:
            n += 1
            print("猜小了，请重新输入")
        elif guess_number==result:
            print("猜想正确，总计猜想%d次，猜想的数字为%d"%(n+1,result))
            print("此次猜想结束")
            break

fun()
