from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_lvl(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=FONT)