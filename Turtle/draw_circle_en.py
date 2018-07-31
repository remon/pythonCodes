
#added by @Azharoo
#Python 3

# Example - 1

#Draw one circle

import turtle

my_turtle = turtle.Turtle()
my_turtle.pencolor("red")
  
def circle(length,angle): 
  my_turtle.forward(length)
  my_turtle.left(angle)
  
for i in range(46):
  circle(10,8)


  # Example - 2
  #Draw Circle of Squares

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.pencolor("blue")

def square(length,angle):
  for i in range(4):
    my_turtle.forward(length)
    my_turtle.right(angle)

for i in range(100):
  square(100,90)
  my_turtle.right(11)



# Example - 3
  #Draw beautiful_circles

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
colors=["red","yellow","purple"]

for x in range(10,50):
    t.circle(x)
    t.color(colors[x%3])
    t.left(90)
 
t.screen.exitonclick()
t.screen.mainloop()