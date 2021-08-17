from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)
