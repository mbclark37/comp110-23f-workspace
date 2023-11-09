"""My turtle."""

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    juniper: Turtle = Turtle()
    petals(juniper, 0, 200, 252, 145, 150, 3)
    petals(juniper, 0, 175, 247, 128, 255, 2)
    petals(juniper, 0, 150, 255, 162, 71, 1)
    stem(juniper, -15, -50,)
    leaf(juniper, 15, -200)
    sun(juniper, -300, 300)


done()


def petals(petal_turtle: Turtle, x: float, y: float, R: int, G: int, B: int, length: float) -> None:
    """Draws the petals."""
    petal_turtle.penup()
    petal_turtle.goto(x, y)
    petal_turtle.pendown()
    petal_turtle.color(R, G, B)
    petal_turtle.speed(50)
    petal_turtle.begin_fill()
    for i in range(360):
        petal_turtle.forward(length)
        petal_turtle.right(1)
    petal_turtle.end_fill()


def stem(stem_turtle: Turtle, x: float, y: float) -> None:
    """Draws the stem."""
    rectangle: Turtle = Turtle()
    stem_turtle.penup()
    stem_turtle.goto(x, y)
    stem_turtle.pendown()
    stem_turtle.color(44, 130, 35)
    stem_turtle.speed(50)
    stem_turtle.begin_fill()
    draw_rectangle(rectangle, 0, -100, 300, 30)
    stem_turtle.end_fill()


def leaf(leaf_turtle: Turtle, x: float, y: float) -> None:
    """Draws the leaf."""
    rectangle: Turtle = Turtle()
    leaf_turtle.penup()
    leaf_turtle.goto(x, y)
    leaf_turtle.pendown()
    leaf_turtle.color(11, 74, 5)
    leaf_turtle.speed(50)
    leaf_turtle.begin_fill()
    draw_rectangle(rectangle, 100, 100, 30, 10)
    leaf_turtle.end_fill()


def draw_rectangle(r_turtle: Turtle, angle_x: float, angle_y: float, length: float, width: float) -> None:
    """Helper function for rectangles."""
    """The towards statement is me trying something new! It angles the turtle so I can draw things on a slant!"""
    r_turtle.towards(angle_x, angle_y) 
    for x in range(2):
        r_turtle.forward(length)
        r_turtle.right(90)
        r_turtle.forward(width)
        r_turtle.right(90)


def sun(sun_turtle: Turtle, x: float, y: float) -> None:
    """Draws the sun."""
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.pendown()
    sun_turtle.color(252, 233, 45)
    sun_turtle.speed(50)
    sun_turtle.begin_fill()
    for i in range(360):
        sun_turtle.forward(1.5)
        sun_turtle.right(1)
    sun_turtle.end_fill()


done()