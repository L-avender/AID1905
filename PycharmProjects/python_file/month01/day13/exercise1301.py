"""
    定义父类
       动物（行为：叫，吃）

    定义子类
        狗（行为：跑）
        鸟（行为：飞）
"""
class Animal:
    def voice(self):
        print("叫")
    def eat(self):
        print("进食")
class Dog(Animal):
    def run(self):
        print("狗在跑")
class Bird(Animal):
    def fly(self):
        print("鸟在飞翔")
animal01=Animal()
dog01=Dog()
bird01=Bird()
print(isinstance(dog01,Animal))
print(isinstance(bird01,Animal))
print(isinstance(animal01,Dog))
print(isinstance(animal01,Bird))
print(issubclass(Dog,Animal))
print(issubclass(Bird,Animal))
print(issubclass(Dog,Animal))