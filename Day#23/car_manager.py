from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.setx(300)
        self.sety(position)
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=1.5)
        self.color(random.choice(COLORS))
        self.forth = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.forth)

