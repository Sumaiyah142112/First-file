class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width = width

    def area (self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

R = Rectangle(6,7)
print(R.area())

S = Square(55)
print(S.area())