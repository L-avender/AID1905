"""
    定义父类
        车（数据：速度，品牌）
    定义子类
        电动车（数据：电池容量，充电功率）
"""
class Car:
    def __init__(self,speed,brand):
        self.speed=speed
        self.brand=brand

class ElectricCar(Car):
    def __init__(self,speed,brand,capacity,power):
       super().__init__(speed,brand)
       self.capacity=capacity
       self.power=power

e01=ElectricCar(200,"yage",20000,1000)
e02=ElectricCar(200,"aima",20000,1000)
print(e01.brand),  
