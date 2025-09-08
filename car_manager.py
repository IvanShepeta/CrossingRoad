from turtle import Turtle


import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        y_position = random.randint(-250, 250)
        car.goto(300, y_position)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def move_up(self):
        self.car_speed += self.move_increment



