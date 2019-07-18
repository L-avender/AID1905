class Dog:
    def __init__(self,name,sex,colocor):
        self.name=name
        self.sex=sex
        self.colocor=colocor
    def run(self):
        print(self.name+"奔跑")
dog01=Dog("xiaoming","nv","red")
dog01.run()
