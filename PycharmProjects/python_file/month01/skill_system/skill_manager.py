list_zodiac=["龙","蛇","马","羊","猴","鸡","狗","猪","鼠","牛","虎","兔"]
def judge_zodiac(year):
     a=(year-2000)%12
     return list_zodiac[a]
print("你的生肖属相是："+judge_zodiac(1994))
