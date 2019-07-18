class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        # self.set_age(age)
        self.hp = hp
        # self.set_weight(weight)
        self.atk = atk
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 100 <= value <= 500:
            self.__hp = value
        else:
            raise ValueError("我不要")
e01=Enemy("灭霸",200,999)
print(e01.name,e01.hp,e01.atk)
