"""
把能被17整除的三位数全部显示出来
"""
def fun():
    for item in range(100,1000):
        if item%17==0:
            yield item

"""
实现摄氏温度和华氏温度之间的换算
"""
def fun01():
    while True:
        select=input("请选择需要进行的转化：1/摄氏温度转华氏温度；2/华氏温度转摄氏温度")
        if not select:
            break
        select=int(select)
        if select==1 or select==2:
            temperature=float(input("请输入要转化的温度："))
            if select==1:
                F=9*temperature/5+32
                print("由摄氏温度转化为华氏温度为：",F)
            elif select==2:
                C=(temperature-32)*5/9
                print("由华氏温度转化为摄氏温度为：",C)
        else:
            print("请按选则1或者2")
fun01()
