dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
    选择菜单
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy()
        elif item == "2":
            settlement()


def settlement():
    zong_jia = 0
    zong_jia = calculate_total_price(zong_jia)
    pay(zong_jia)


def pay(zong_jia):
    while True:
        qian = float(input("总价%d元，请输入金额：" % zong_jia))
        if qian >= zong_jia:
            print("购买成功，找回：%d元。" % (qian - zong_jia))
            list_order.clear()
            break
        else:
            print("金额不足.")


def calculate_total_price(zong_jia):
    zong_jia = 0
    for item in list_order:
        shang_pin = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        zong_jia += shang_pin["price"] * item["count"]
    return zong_jia


def buy():
    print_commodity_info()
    create_order()
    print("添加到购物车。")


def create_order():
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    list_order.append({"cid": cid, "count": count})


def input_commodity_id():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


select_menu()