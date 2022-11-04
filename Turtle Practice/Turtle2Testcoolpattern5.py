from turtle import *
angle = 91
x = xcor() #this uses the current "x" coordinate as a variable
showturtle()
shape("turtle")
for x in range(5000):
    
    forward(x)
    left(angle)
    
    
    speed(0)

mainloop()