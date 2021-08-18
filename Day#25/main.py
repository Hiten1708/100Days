import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(700, 500)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

correct = 0
answers_guessed = []

states = pandas.read_csv("50_states.csv")

game_is_on = True
answer = ""

while game_is_on and answer != "Exit":
    answer = screen.textinput(title=f"U.S. States Game {correct}/50", prompt="Enter name of the state: ")
    answer = answer.title()
    for st in states.state:
        if correct <= 50:
            if answer == st and answer not in answers_guessed:
                correct_list = states[states.state == st]
                xy = correct_list
                x = xy.x.to_list()
                y = xy.y.to_list()
                name_tur = Turtle()
                name_tur.penup()
                name_tur.hideturtle()
                name_tur.goto(int(x[0]), int(y[0]))
                name_tur.write(st, False, "center", ("Arial", 10, "normal"))
                correct += 1
                answers_guessed.append(st)
            else:
                pass


list = states.state.to_list()
not_guessed = []

for char in list:
    if char not in answers_guessed:
        not_guessed.append(char)

ng = pandas.DataFrame(not_guessed)

ng.to_csv("States_to_learn")
