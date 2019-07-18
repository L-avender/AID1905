"""
    封装设计思想
        需求：小明在招商银行取钱
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def get_money(self, money, bank):
       """
       :param money:
       :param bank:
       :return:
       """
       print(self.name, "去", bank)
       bank.method(money)
class Bank:
    def method(self, get_money):
       """

       :param get_money:
       :return:
       """
       print("到%s银行取钱:"%(get_money))


xm = Person("小明")
bank = Bank()
# 老张开车去东北
xm.get_money("小明", bank)