COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.car_list = []

    def car_creator(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            random_y = random.randint(-250,250)
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(290,random_y)
            self.car_list.append(new_car)

    def car_drives(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)


