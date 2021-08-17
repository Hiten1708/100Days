from players import Player
from scoreboard import ScoreBoard
from ball import Ball
from turtle import Screen
import time

screen = Screen()
screen.setup(800, 600)

left = Player()
right = Player()
score1 = ScoreBoard()
score2 = ScoreBoard()
left_score = 0
right_score = 0

left.goto(-380, 0)
right.goto(380, 0)
score1.goto(-30, 240)
score2.goto(30, 240)

score1.write_score(left_score)
score2.write_score(right_score)


screen.listen()
screen.onkey(left.move_up, "Up")
screen.onkey(left.move_down, "Down")
screen.onkey(right.move_up, "w")
screen.onkey(right.move_down, "s")

games_on = True
ball = Ball()

while games_on:
    ball.penup()
    ball.move()

    if ball.xcor() < -360 and ball.distance(left) < 50 or ball.xcor() > 360 and ball.distance(right) < 50:
        ball.hitx()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.hity()

    if ball.xcor() < -380:
        ball.reset()
        right_score += 1
        score2.write_score(right_score)
        time.sleep(3)

    if ball.xcor() > 380:
        ball.reset()
        left_score += 1
        score1.write_score(left_score)
        time.sleep(3)

screen.exitonclick()

screen = Screen()
