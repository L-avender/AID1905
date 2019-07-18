def isogram(str):
    for c in range(len(str)-1):
        for a in range(c+1,len(str)):
            if str[c]==str[a]:
                return False
    return True

print(isogram("abad"))


def get_new_list(a,b):
    list=[a,b]
    for a in range(2,8):
        list.append(list[a-1]+list[a-2])
    return list


