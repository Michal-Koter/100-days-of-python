import turtle
from random import randint
import random

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.pensize(2)

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# # 1st example
# def draw_shape(sides_num):
#     angle = 360 / sides_num
#     for _ in range(sides_num):
#         my_turtle.forward(100)
#         my_turtle.left(angle)
#
# for i in range(3, 10):
#     my_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
#     draw_shape(i)


# # 2nd example
# directions = (0, 90, 180, 270)
#
# for i in range(200):
#     my_turtle.color(random_color())
#     my_turtle.forward(25)
#     my_turtle.setheading(random.choice(directions))


# 3rd example
def draw_spirograph(gape_size):
    for i in range(int(360/gape_size)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + gape_size)

draw_spirograph(10)


screen = turtle.Screen()
screen.exitonclick()
