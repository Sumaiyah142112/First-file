class Expressions:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def addition(self):
        result= self.num1 + self.num2 + self.num3
        print("The sum is:", result)

ef1 = Expressions(1,100,10000)
ef2 = Expressions(5, 15, 25)

ef1.addition()
ef2.addition()
