from turtle import *
color("black")

while True:
        forward(100)
        right(50)
        backward(75)
        right(55)
        fd(100)
        circle(20)
        right(22)
        fd(20)
        right(112)
        fd(50)
        backward(65)
        circle(22)
        speed(0)
           
       

        if abs(pos()) < 1:
            break


done()
