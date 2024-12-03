import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(2)

# Draw the cigarette body
t.penup()
t.goto(-100, 0)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)
t.end_fill()

# Draw the filter part
t.penup()
t.goto(-100, 0)
t.pendown()
t.color("tan")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
t.end_fill()

# Draw the burning end
t.penup()
t.goto(100, 0)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw some smoke
t.penup()
t.goto(110, 10)
t.color("grey")
t.pensize(1)
for i in range(3):
    t.pendown()
    t.setheading(45)
    t.circle(20, 90)
    t.penup()
    t.goto(110 + i*10, 10 + i*10)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()
