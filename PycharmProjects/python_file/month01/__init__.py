def decorator_a(func):
    print("Get in decorator_a")
    def inner_a(*args,**kwargs):
        print("Get in inner_a")
        return func(*args,**kwargs)
    return inner_a

def decorator_b(func):
    print("Get in decorator_b")
    def inner_b(*args,**kwargs):
        print("Get in inner_b")
        return func(*args,**kwargs)
    return inner_b

@decorator_b#f=decorator_b(f)
@decorator_a#f=decorator_a(f)
def f(x):
    print("Get in f")
    return x*2
f(1)

str="hello"