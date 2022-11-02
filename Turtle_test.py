from turtle import *
color('black', 'blue')
begin_fill()

while True:
        forward(100)
        right(179)
        forward(55)
        left(145)
        forward(50)
        left(75)
        forward(200)
        right(179)
        forward(55)
        left(145)
        forward(150)
        left(75)
        forward(100)
        right(179)
        forward(105)
        left(145)
        forward(100)
        left(75)
        speed(0)
        if abs(pos()) < 1:
            break
end_fill()
done()
