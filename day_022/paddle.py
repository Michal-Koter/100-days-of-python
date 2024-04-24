from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, screen_height):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(x_pos)
        self.screen_height = screen_height

    def go_up(self):
        if self.ycor() < self.screen_height / 2 - 50:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def go_down(self):
        if self.ycor() > -self.screen_height / 2 + 50:
            new_y = self.ycor() - 20
            self.sety(new_y)
