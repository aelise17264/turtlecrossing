from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto(0, -300)

    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0, -250)