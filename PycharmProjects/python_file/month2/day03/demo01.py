def fib(n):
    sum1 = 0
    if n == 0:
       sum1 = 1
    else:
        sum1 = n * fib(n - 1)
    return sum1
print(fib(3))

def fun(b):
    a=1
    for c in range(1,b+1):
        a*=c
    return a
print(fun(5))
"""
选择排序
"""
list=[1,5,38,7,8,64,58]
for item in range(len(list)-1):
    for a in range(item+1,len(list)):
        if list[item]>list[a]:
            list[item],list[a]=list[a],list[item]
print(list)

"""
冒泡排序
"""
list=[10,18,9,18,8,64,58]
for item in range(len(list)-1):
    for a in range(len(list)-1-item):
        if list[a]>list[a+1]:
            list[a],list[a+1]=list[a+1],list[a]
print(list)
"""
插入排序
"""
list=[10,18,9,18,8,64,58]
for item in range(len(list)-1):
    for a in range(item+1,0,-1):
        if list[a]<list[a-1]:
            list[a],list[a-1]=list[a-1],list[a]
print(list)
