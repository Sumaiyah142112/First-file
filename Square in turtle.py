import turtle
# Creating canvas
turtle.Screen().bgcolor("orange")

sc= turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to turtle window!!")

#turtle object creation

board=turtle.Turtle()

#Creating a square
for i in range(4):
 board.forward(100)
 board.left(90)
 i = i+1

