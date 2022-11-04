from turtle import *
angle = 91
x = int(xcor())
showturtle()
shape("turtle")
if x in range(1000):
    forward(x)
    left(angle)
    speed(0)
else:
    backward(x)
    right(angle)
    speed(0)



