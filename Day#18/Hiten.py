import turtle
from turtle import Turtle
import random

timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


aa = 0

for char in range(36):
    aa += 10
    timmy.circle(100)
    timmy.setheading(aa)
    timmy.color(random_color())
