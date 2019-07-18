class Animial:
    def __init__(self,pig_number,chicken_number,sheep_number):
        self.pig_number=pig_number
        self.chicken_number=chicken_number
        self.sheep_number=sheep_number

    def count_legs(self):
        total_legs =  self.pig_number* 4 +  self.chicken_number* 2 + self.sheep_number* 4
        return total_legs

Animial01=Animial(2,3,4)
print(Animial01.count_legs())

def a():
    for item in range(1,101):
        for a in range(2,item):
            if item%a==0:
              break
        else:
            yield item

def fun(b):
    a=1
    d=0
    for c in range(1,b+1):
        a*=c
        d+=a
    return d
print(fun(5))

















