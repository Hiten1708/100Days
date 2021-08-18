import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
score = Scoreboard()
hit = Player()
screen.listen()
screen.onkey(hit.move, "Up")
cars = []
positions = []
rasu = [0, 0, 0, 0, 1]

for char in range(24):
    post = (-180 + (20*char))
    positions.append(post)

x = 0.1

game_is_on = True
while game_is_on:
    time.sleep(x)
    for char in range(random.choice(rasu)):
        car = CarManager(random.choice(positions))
        cars.append(car)

    for car in cars:
        car.move()

        if car.distance(hit) < 20 and car.xcor() - 40 < hit.xcor() < car.xcor() + 40:
            game_is_on = False
            score.gameover()

        if hit.ycor() >= 280:
            score.increase_score()
            hit.reposition()
            x *= 0.6

    screen.update()

screen.exitonclick()