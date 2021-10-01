from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-270, 260)
        self.write(f"Level = {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def levelup(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}", font=FONT)
