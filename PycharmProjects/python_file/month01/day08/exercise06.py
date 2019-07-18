# 在控制台中获取一个月份
# 打印天数,或者提示"输入有误".
# 1 3 5 7 8 10 12  --> 31天
# 4 6 9 11 --> 30天
# 2 --> 28天
# 16:05
#根据年月计算有多少天，考虑闰年和平年
def year(year):
   return year % 4 == 0 and year % 100 != 0 or year % 400 ==0
def get_day_of_month(year,month):
    """
    根据年月计算有多少天，考虑闰年和平年
    :param year: 目标年份
    :param month: 目标月份
    :return: 目标年份当月的天数
    """
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if year(year):return 28
           return 28
    if month == 4 or month == 6 or month == 9\
            or month == 11:
        return 30
    return 31
print(get_day_of_month(2004,2))