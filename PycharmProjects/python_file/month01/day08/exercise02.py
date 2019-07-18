def calculate_weight_for_jin(liang_weight):
    """
    根据两的重量计算几斤几两
    :param liang_weight: 给出的两的重量
    :return: 元组(斤，两)
    """
    jin=liang_weight//16
    liang=liang_weight%16
    return (jin,liang)
er=calculate_weight_for_jin(20)
print(er)