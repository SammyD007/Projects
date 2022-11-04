from turtle import *
shape("classic")
x = xcor() + 10 ** 2
angle = 94.3
fd1 = (x + 10 * 2)
while True:
    forward(fd1)
    stamp()
    right(angle)
    speed(0)
    if abs(pos()) < 1:
        backward(130)
        speed(0)


