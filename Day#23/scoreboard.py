from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-235, 260)
        self.write("LEVEL: " + str(self.level), False, 'center', FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write("LEVEL: " + str(self.level), False, 'center', FONT)

    def gameover(self):
        self.home()
        self.level = 1
        self.write("GAMEOVER", False, 'center', FONT)