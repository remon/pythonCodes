#added by @Azharoo
#Python 3
#draw a simple square 

# Example - 1

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
t.color("blue")
t.shape("turtle")
for i in range(4):
  t.fd(100)
  t.left(90)

# Example - 2

import turtle
t= turtle.Turtle()
t.screen.bgcolor("black")
t.color("red")
t.hideturtle()  # Hide the turtle during the draw
 
def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)
 
square(100)