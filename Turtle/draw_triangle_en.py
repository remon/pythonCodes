#added by @Azharoo
#Python 3

# Example - 1

#Draw triangle 

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")

t.color("red")
t.hideturtle() # hide the turtle
 
def triangle(length,angle=120):
    for steps in range(3):
        t.fd(length)
        t.left(angle)
 
triangle(200)