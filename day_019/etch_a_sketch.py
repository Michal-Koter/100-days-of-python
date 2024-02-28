from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
speed = 20
angel = 10


def move_forwards():
    my_turtle.forward(speed)


def move_backwards():
    my_turtle.backward(speed)


def turn_left():
    my_turtle.left(angel)


def turn_right():
    my_turtle.right(angel)


def clear_screen():
    my_turtle.home()
    my_turtle.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
