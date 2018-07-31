#added by @Azharoo
#Python 3
#draw a simple rectangle 

# Example - 1

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
t.hideturtle()
t.color("red")
 
def slanted_rectangle(length,width):
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
 
slanted_rectangle(length=200,width=100)


# Example - 2
#draw a slanted rectangle 

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")


t.hideturtle()
t.color("red")
 
def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
 
slanted_rectangle(length=200,angle=45,width=100)