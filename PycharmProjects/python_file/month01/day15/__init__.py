# 练习2：根据生日(年月日)，计算活了多少天。
# 思路：
# 年月日 --> 出生时间
# 当前时间 --> 出生时间
# 计算天
import time
def life_day(year,month,day):
    tuple_time=time.strptime("%d-%d-%d"%(year,month,day), "%Y-%m-%d")
    time.time()
    live_day=int((time.time()-time.mktime(tuple_time))/60/60/24)
    return live_day
print(life_day(2019,6,19))








