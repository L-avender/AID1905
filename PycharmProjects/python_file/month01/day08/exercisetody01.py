# 定义函数，计算指定范围内的素数
def get_prime_number(n,m):
    """

    :param n:
    :param m:
    :return:
    """
    list01=[]
    for a in range(n,m+1):
        for c in range(2,a):
            if a%c==0:
              break
        else:
            list01.append(a)
    return list01
print(get_prime_number(1,101))
