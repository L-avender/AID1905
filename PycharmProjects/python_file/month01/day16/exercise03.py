list01=[4,5,566,7,8,10]
list02=[]
def get_even_number(target):
    for item in target:
        if item %2==0:
           list02.append(item)
    return list02
print(get_even_number(list01))
