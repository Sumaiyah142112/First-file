import turtle

turtle.bgcolor("beige")

shape=turtle.Turtle()

sc=turtle.Screen()
sc.setup(800,900)

#Creating a rectangle
shape.fillcolor("light blue")
shape.begin_fill()
for i in range(2):
 shape.forward(50)
 shape.left(90)
 shape.forward(100)
 shape.left(90)
shape.end_fill()
 
#Creating a hexagon
shape.penup()
shape.forward(150)
shape.pendown()

shape.fillcolor("light pink")
shape.begin_fill()

for i in range(7):
 shape.forward(50)
 shape.left(60)
shape.end_fill()

#Creating an equilateral triangle
shape.penup()
shape.left(120)
shape.forward(300)
shape.pendown()

shape.fillcolor("light green")
shape.begin_fill()

for i in range(4):
 shape.forward(100)
 shape.right(120)
shape.end_fill()

 
 



