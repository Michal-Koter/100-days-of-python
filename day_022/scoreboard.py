from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Courier', 38, "bold")
X_POS = 70

class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(screen_height/2 - 60)

        self.l_score = 0
        self.r_score = 0

        self.update_score()

    def update_score(self):
        self.clear()
        self.setx(-X_POS)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.setx(X_POS)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
