class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight+=1
p01=Person("xiaoming",75)
a=p01.run
print(a)
p01.eat()
print(p01.weight)



