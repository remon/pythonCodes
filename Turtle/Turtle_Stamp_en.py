#Added by @Azharo
#Python 3

# Example - 1 Draw shape using stamp

import turtle
loadWindow = turtle.Screen()
loadWindow.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("dark green")

t.penup()                # This is new
size = 20
for i in range(35):      #The number of stamps
   t.stamp()             # Leave an impression on the canvas
   size = size + 3       # Increase the size on every iteration
   t.forward(size)       # Move tess along
   t.right(24)           #  ...  and turn her

turtle.exitonclick()



# Example - 2 Draw clock shape

import turtle

loadWindow = turtle.Screen()
loadWindow.bgcolor("yellow")

Lena = turtle.Pen()
Lena.shape('turtle')
Lena.color('red')
Lena.pensize(4)
Lena.stamp()  #Stamp a copy of the turtle shape onto the canvas at the current turtle position.

for i in range(12):
	Lena.penup()
	Lena.forward(100)
	Lena.pendown()
	Lena.forward(30)
	Lena.penup()
	Lena.forward(40)
	Lena.stamp()
	Lena.backward(170)
	Lena.right(360/12)

turtle.exitonclick()
