#added by @Azharo
#Python 3

# Example - 1


#beautiful_spiral

import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
colors=["blue","purple","red","yellow","orange","brown"]
#t.screen.tracer(0,0)
 
for x in range(300):
    t.color(colors[x%6])
    t.fd(x)
    t.left(59)
 
t.screen.exitonclick()
t.screen.mainloop()