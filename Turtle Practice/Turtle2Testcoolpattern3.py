# Set up the window and its attributes
import turtle
wn = turtle.Screen()


# create tess and set some attributes
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

# create alex, who is a second turtle object
alex = turtle.Turtle()

# Let tess draw an equilateral triangle
tess.forward(80)
tess.left(75)
tess.forward(80)
tess.circle(15)
tess.forward(80)
tess.left(19)
tess.circle(15)

# turn tess around, and move her away from the origin
tess.right(180)
tess.forward(80)

# make alex draw a square
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()