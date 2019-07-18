class GraphicsManager:

    def area(self,calculateArea):
        return calculateArea.calculate_area()

class CalculateArea:
    def calculate_area(self):
       pass


class Circle(CalculateArea):
    def __init__(self,radius,pi=3.14):
        self.radius=radius
        self.pi=pi
    def calculate_area(self):
        circle_area=self.pi*self.radius**2
        return circle_area



class Rectangle(CalculateArea):
    def __init__(self,length,wide):
        self.length=length
        self.wide=wide
    def calculate_area(self):
        rectangle_area=self.length*self.wide
        return rectangle_area

graph01=GraphicsManager()
c01=Circle(2)
r01=Rectangle(3,4)

print(graph01.area(c01))
print(graph01.area(r01))

