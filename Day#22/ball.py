from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.move_x = 3
        self.move_y = 3

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def hitx(self):
        self.move_x *= -1

    def hity(self):
        self.move_y *= -1