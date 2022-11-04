from turtle import *
shape("classic")
x = xcor()
angle = 95
fd1 = (x + 10 * 2)
while True:
    forward(fd1)
    stamp()
    right(angle)
    speed(0)
    if abs(pos()) < 1:
            break
mainloop()