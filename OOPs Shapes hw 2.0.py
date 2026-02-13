class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
         self.length = length
         self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side
    
obj1 = Rectangle(10,50)
obj2 = Square(55)

print("Rectangle Area:", obj1.area())
print("Square Area:", obj2.area())






