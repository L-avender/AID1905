list1 = ['1','2','3','4','a']
print(''.join(list1))
print(' '.join(list1))
print('!'.join(list1))

list1 = ['1', '2', '3', '4', 'a', (1, 2, 3)]
print(tuple(list1))

tuple1 = ('1','2','3','4','5','2','a')
print(''.join(tuple1))

dict1={1:'a',2:'b',3:'c'}
print(set(dict1.values()))

print("hello world dd".split(" "))

str="ABCDEFG"
print(str[5:2])

d = {"a": 3, "b": 2, "c": 1}
print(max(d))

class A:
    v = 100
    def __init__(self):
        self.v = 200
a1 = A()
a2 = A()
del a2.v
print(a1.__class__.v)
print(a2.v)
print(a1.v)
print(A.v)
print(bool("  "))
print("小明" '今年', 20, '岁')