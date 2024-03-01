from turtle import Turtle, Screen
import time

from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
STEP = 20

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    left_paddle = Paddle(-(WIDTH / 2 - 50), HEIGHT)
    screen.onkeypress(left_paddle.go_up, "w")
    screen.onkeypress(left_paddle.go_down, "s")

    right_paddle = Paddle(WIDTH / 2 - 50, HEIGHT)
    screen.onkeypress(right_paddle.go_up, "Up")
    screen.onkeypress(right_paddle.go_down, "Down")

    ball = Ball()

    scoreboard = Scoreboard(HEIGHT)

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect ball collision with wall
        if ball.ycor() > HEIGHT / 2 - 20 or ball.ycor() < -HEIGHT / 2 + 20:
            ball.bounce_y()

        # Detect ball collision with paddle
        if ball.distance(left_paddle) < 50 and ball.xcor() < -WIDTH / 2 + 80 \
                or ball.distance(right_paddle) < 50 and ball.xcor() > WIDTH / 2 - 80:
            ball.bounce_x()

        # Detect R paddle misses the ball
        if ball.xcor() > WIDTH/2 - 30:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle misses the ball
        if ball.xcor() < -WIDTH/2 + 30:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()
