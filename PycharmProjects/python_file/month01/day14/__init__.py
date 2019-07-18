class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def print(self):
        print("敌人的名字是%s，血量为%d，攻击力为%d"%(self.name,self.hp,self.atk))

    def __str__(self):
        return "敌人的名字是%s，血量为%d，攻击力为%d"%(self.name,self.hp,self.atk)
    def __repr__(self):
        return "Enemy('%s',%d,%d)" %(self.name, self.hp, self.atk)

e01=Enemy("meiba",1000,999)
e01.print()
e02 =eval(repr(e01))
print(e02)


