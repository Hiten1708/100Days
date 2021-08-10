# import colorgram
#
# color = []
#
# cream = colorgram.extract("image.jpg", 255)
#
# for camel in cream:
#     first_color = cream[cream.index(camel)]
#     rgb = first_color.rgb
#     color.append((rgb.r, rgb.g, rgb.b))
#
# print(color)
# import random
# import turtle
# from turtle import Turtle, Screen
# turtle.colormode(255)
#
# colour =[(131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211), (65, 66, 57), (100, 141, 129), (155, 202, 223), (143, 130, 108)]
#
#
# screen = Screen()
# hit = Turtle()
#
#
# hit.penup()
# hit.goto(-225, -185)
# count = 1
# hit.dot(20, colour[random.randint(0, 31)])
#
# for n in range(10):
#     for x in range(9):
#         hit.forward(50)
#         hit.dot(20, colour[random.randint(0, 31)])
#     count += 1
#     if count == 10:
#         break
#     if count % 2 == 0:
#         hit.left(90)
#         hit.forward(50)
#         hit.dot(20, colour[random.randint(0, 31)])
#         hit.left(90)
#     else:
#         hit.right(90)
#         hit.forward(50)
#         hit.dot(20, colour[random.randint(0, 31)])
#         hit.right(90)
#
# screen.exitonclick()

import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

colour =[(131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211), (65, 66, 57), (100, 141, 129), (155, 202, 223), (143, 130, 108)]


screen = Screen()
hit = Turtle()

hit.penup()
hit.goto(-225, -185)


for n in range(10):
    x = hit.xcor()
    y = hit.ycor()
    for x in range(10):
        hit.forward(50)
        hit.dot(20, colour[random.randint(0, 31)])
    hit.goto(x - 235, y + 50)

screen.exitonclick()
