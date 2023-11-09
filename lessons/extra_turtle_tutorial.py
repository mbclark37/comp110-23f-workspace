"""A dupilcate turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)

side_length: int = 300
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.color(99, 204, 250)
leo.speed(50)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()
 
bob: Turtle = Turtle()
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.color(16, 5, 191)
bob.speed(80)
i = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1

girl: Turtle = Turtle()
i = 0
girl.penup()
girl.goto(0, 200)
girl.pendown()
girl.speed(50)
while (i < 360):
    girl.forward(3)
    girl.right(1)
    i += 1


boy: Turtle = Turtle()
i = 0
while (i < 360):
    boy.forward(2)
    boy.right(1)
    i += 1
done()