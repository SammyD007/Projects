from turtle import *
angle = 92
x = xcor() #this uses the current "x" coordinate as a variable
showturtle()
shape("turtle")
for x in range(300):
    penup() #penup "lifts" the pen, meaning that it will not draw in the chunk of commands below penup
    forward(x)
    left(angle)
    pendown() ##pendown "sets" the pen back down alowing the turtle to draw again
    circle(x)
    speed(0)
else: 
    while True:
        penup() #penup "lifts" the pen, meaning that it will not draw in the chunk of commands below penup
        forward(x)
        right(angle)
        pendown() #pendown "sets" the pen back down alowing the turtle to draw again
        circle(15)
        speed(0)
    

mainloop()