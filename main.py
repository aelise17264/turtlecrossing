import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

my_turtle = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_cars()
    car.move_cars()

    for each_car in car.all_cars:
        if each_car.distance(my_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if my_turtle.ycor() > 280:
        scoreboard.levelup()
        my_turtle.reset_position()
        car.faster()



screen.exitonclick()