import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("lightblue")
t.pensize(3)
t.speed(3)

t.penup()
t.goto(-200, 50)
t.pendown()
t.color("red", "yellow")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(0, 50)
t.pendown()
t.color("blue", "lightgreen")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-100, -150)
t.pendown()
t.color("purple", "orange")
t.begin_fill()
for _ in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

t.hideturtle()
s.exitonclick()