from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_score(self, score):
        self.clear()
        self.write(str(score), False, 'center', ('Arial', 24, 'normal'))

