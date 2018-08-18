#Turtle Race Game :
#added by Heba-Ahmad
#This is a turtle game, that turtles will race against each other

#the code of the game with readable comments:
from turtle import *
from random import randint

#screen setup:
wn = Screen()
wn.bgcolor("green yellow")
wn.title("Turtles Race")
wn.setup(width = 500, height= 500)

#to write on the screen 
race = Turtle()
race.color("black")
race.shape("turtle")
race.up()
race.goto(-80,180)
race.down()
race.write("Turtles Race", True, align= "left", font=("comic sans ms", 20, "italic"))

#turtle objects setup:
speed('fastest')
penup()
goto(-140, 100)
#a race track 
for step in range (15):
    write(step, align= 'center')
    right(90)
    forward(10)
    pendown()
    #the track lines dashed instead of solid (for solid: add forward(150) instead of the loop and change backward value to 160)
    for i in range(10):
        forward(15)
        penup()
        forward(5)
        pendown()
    penup()
    backward(210)
    left(90)
    forward(20)

#Racing turtles
racer1 = Turtle()
racer1.color('red')
racer1.shape('turtle')
racer1.penup()
racer1.goto(-160, 60)
racer1.pendown()
#make each turtle do a 360 degree twirl after they get to the starting line
for turn in range(36):
  racer1.right(10)

racer2 = Turtle()
racer2.color('white')
racer2.shape('turtle')
racer2.penup()
racer2.goto(-160, 30)
racer2.pendown()
#A full turn right 10 degrees 36 times
for turn in range(36):
  racer2.left(10)

racer3 = Turtle()
racer3.color('yellow')
racer3.shape('turtle')
racer3.penup()
racer3.goto(-160, 0)
racer3.pendown()
for turn in range(36):
  racer3.right(10)

racer4 = Turtle()
racer4.color('purple')
racer4.shape('turtle')
racer4.penup()
racer4.goto(-160, -30)
racer4.pendown()
#A full turn right 5 degrees 72 times
for turn in range(72):
  racer4.right(5)

racer5 = Turtle()
racer5.color('blue')
racer5.shape('turtle')
racer5.penup()
racer5.goto(-160, -60)
racer5.pendown()
for turn in range(72):
  racer5.right(5)
#make the turtle race by moving a random number of steps at a time  
for turn in range(100):
  racer1.forward(randint(1, 5))
  racer2.forward(randint(1, 5))
  racer3.forward(randint(1, 5))
  racer4.forward(randint(1, 5))
  racer5.forward(randint(1, 5))
wn.exitonclick()
