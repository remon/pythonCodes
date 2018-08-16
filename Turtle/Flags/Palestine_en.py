#added by @Azharo
#Python 3

#Draw Palestine Flag

import turtle

turtle.shape("turtle")
window = turtle.Screen()
window.bgcolor("white")
window.setup(width=1.0, height=1.0, startx=None, starty=None)
	
turtle.title("Programming by Azharo - Palestine - 2018")
	
## The black part	
turtle.begin_fill()
turtle.color("black")

for i in range(2):
  turtle.forward(500)
  turtle.left(90)
  turtle.forward(300)
  turtle.left(90)
turtle.end_fill()
  
  
## The green part
turtle.begin_fill()
turtle.color("dark green")

turtle.left(90)
turtle.forward(100)  
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(100)

turtle.end_fill()
  
  
## The white  part
turtle.begin_fill()
turtle.color("white")

turtle.right(180)
turtle.forward(200)
turtle.left(90)
turtle.forward(500) 
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(500) 

turtle.end_fill()
  
#change turtle deirection

turtle.left(90)
turtle.forward(200) 
turtle.left(90)
turtle.forward(500) 
turtle.left(150)

## The Red Part
turtle.begin_fill()
turtle.color("red")

turtle.right(9.9)
turtle.forward(232)

turtle.right(100)

turtle.forward(232)


turtle.end_fill()

## Make the flag stand 

turtle.begin_fill()
turtle.color("black")
turtle.up()
turtle.setpos(0,300)
turtle.setheading(180)
turtle.down()
turtle.forward(20)

turtle.setheading(270)

turtle.forward(550)

turtle.setheading(0)

turtle.forward(20)

turtle.setheading(90)

turtle.forward(550)

turtle.end_fill()



def writetext(text,color,x,y):
   for i in range(1,10):
      turtle.penup()
      turtle.setx(x)
      turtle.sety(y)
      turtle.pendown
   
   turtle.pencolor(color)
   turtle.write(text,move=True, font=("Arial",16,"normal"))
     

writetext('Programming by Azharo - Palestine - 2018','black',8,-100)
writetext('UDACITY Full Stack Web Developer Student','blue',8,-150)

turtle.hideturtle()

turtle.exitonclick()
