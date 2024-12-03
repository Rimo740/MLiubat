import turtle
import time

# Set up the turtle
t = turtle.Turtle()
t.speed(10)  # Set moderate speed for visible animation
t.pensize(5)
t.color("blue")

# Move to starting position
t.penup()
t.goto(-200, 0)
t.pendown()

# Write R
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.left(135)
t.forward(50)

# Move for I
t.penup()
t.goto(-150, 0)
t.pendown()
t.left(135)
t.forward(100)

# Move for M
t.penup()
t.goto(-120, 0)
t.pendown()
t.left(0)
t.forward(100)
t.right(135)
t.forward(50)
t.left(90)
t.forward(50)
t.right(135)
t.forward(100)

# Move for O
t.penup()
t.goto(-20, 0)
t.left(90)
t.forward(50)
t.pendown()
t.circle(45)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()
