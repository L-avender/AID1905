import  random
# def fun():
list=[random.randint(0,9) for item in range(100) ]
a = set(list)
dict={item:list.count(item) for item in a}
    # for item in range(100):
    #     list.append(random.randint(0,9))
    # a=set(list)
    # for item in a:
    #  dict[item]=list.count(item)
    # return dict
# print(fun())
dict1={}
for item in range(100):
    a=random.randint(0,9)
    if a not in dict1:
        dict1[a]=1
    else:
        dict1[a]+=1
print(dict1)