import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
car_player = CarManager()
screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_player.car_creator()
    car_player.car_drives()
    for car in car_player.car_list:
        if car.distance(player1) < 20:
            print("Game over!")
            game_is_on = False

screen.exitonclick()
