#元祖
#基础操作
#1.创建元祖
#tuple01=()
#具有默认值
#tuple01=(1,2,3)
#元祖只有一个元素，在元素后加，号
#tuple01=(100,)
#print(tuple01)
#不能变化
#2.练习：在控制台中录入日期（年月），计算这是这一年的第几天，
#例如3月5日
day_of_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month=int(input("请输入月份"))
day=int(input("请输入日"))
total_day=0
for i in range(month-1):
   total_day+=day_of_month[i]
total_day+=day
print("是这一年的第%d天"%total_day)
#total_day=sum(day_of_month[:month-1])
#total_day+=day
#print("是这一年的第%d天"%total_day)