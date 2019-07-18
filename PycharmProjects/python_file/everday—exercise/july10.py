def fun(list01,list02):
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
    return list03
list01=["早饭","午饭","晚饭","夜宵"]
list02=["牛奶面包","饺子","麻辣香锅"]
print(fun(list01,list02))

def fun02(total_volume):
    a=0
    for item in total_volume:
        a+=item[0]*item[1]*item[2]
    return a
total_volume=([2,3,2],[6,6,7],[1,2,1])
print(fun02(total_volume))

