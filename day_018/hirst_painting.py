import random

import colorgram
import turtle


def extract_colors(img_path):
    extracted_colors = colorgram.extract(img_path, 30)

    colors = []
    for item in extracted_colors:
        r = item.rgb.r
        g = item.rgb.g
        b = item.rgb.b
        new_color = (r, g, b)
        colors.append(new_color)

    return colors


def paint_dots(colors):
    my_turtle = turtle.Turtle()
    my_turtle.penup()

    step = 50
    dots_on_side = 10

    my_turtle.setheading(225)
    my_turtle.forward(step * (dots_on_side / 2 + 1))
    my_turtle.setheading(0)

    x, y = my_turtle.pos()

    for _ in range(dots_on_side):
        for _ in range(dots_on_side):
            my_turtle.dot(20, random.choice(colors))
            my_turtle.forward(step)
        y += step
        my_turtle.setpos(x, y)


if __name__ == '__main__':
    turtle.colormode(255)
    turtle.speed("fastest")

    color_list = extract_colors("Complete_menu_no_buttons.jpg")
    paint_dots(color_list)
    screen = turtle.Screen()
    screen.exitonclick()

