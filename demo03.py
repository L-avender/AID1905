#练习1：在控制台中循环录入商品信息（名称，单价）
#如果名称输入空字符，则停止录入
#将所有信息打印出来
dict_commodity_info={}
while True:
    name=input("请输入商品名称")
    if name=="":
        break
    price=input("请输入商品价格")
    dict_commodity_info[name]=price
for name,price in dict_commodity_info.items():
    print("%s的价格是%s"%(name,price))
