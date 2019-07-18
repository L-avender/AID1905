list01=[3,4,"55",6,7,"8",9,"5",6]
# def my_enumerate(target_list):
#     for a in range(len(target_list)):
#         item=target_list[a]
#         yield (a,item)
# for a,c in my_enumerate(list01):
#     print(a,c)
# def my_enumerate(*args):
#    for item in zip(*args):
#        yield item
# for item in my_enumerate(list01,list02,list03):
#     print(item)
def get_str(list_target):
    for item in list_target:
        if type(item)==str:
            yield item

re=get_str(list01)
for item in re:
    print(item)


re=(item for item in list01 if type(item)==str)
for item in re:
    print(item)

list=[item for item in list01 if type(item)==str]
for item in list:
    print(item)

