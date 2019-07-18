def fun(a,b):
    list=[]
    for item in range(min(a,b),0,-1):
        if a%item==0 and b%item==0:
         return item
print(fun(2,6))