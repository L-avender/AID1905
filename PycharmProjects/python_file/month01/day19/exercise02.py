import time


def validation(func):
    def verify(*args, **kwargs):
        start=time.time()
        func(*args, **kwargs)
        elapsed = (time.time() - start)
        print("Time used:", elapsed)
        return func(*args, **kwargs)
    return verify
@validation
def fun01():
    time.sleep(2)
    print("fun01执行完毕")
@validation
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕，参数是：",a)

fun01()
fun02(100)