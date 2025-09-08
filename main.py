import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # created the car with probability 1/6
    if random.randint(1, 6) == 1:
        car_manager.create_car()
    car_manager.move()

    # detect collision with
    if player.ycor() >= 280:
        scoreboard.score_increase()
        player.starting_position()
        car_manager.move_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.end_game()
            game_is_on = False

screen.exitonclick()