def deposit(money):
    print("存%d钱咯"%money)

def withdraw(login_id,pwd):
    print("取钱咯",login_id,pwd)


def validation(func):
    def verify(*args, **kwargs):
        print("验证账户及密码")
        return func(*args, **kwargs)
    return verify

@validation
def deposit(money):
    print("存%d钱咯" % money)
@validation
def withdraw(login_id,pwd):
    print("取钱咯",login_id,pwd)
deposit(10000)
withdraw("zs",123)
