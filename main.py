from turtle import Screen
import time
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing Game")
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.up, key="Up")
car = Car()
score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.creating_cars()
    car.moving_the_cars()

    for vehicle in car.cars:
        if player.distance(vehicle.position()) < 23:
            game_is_on = False
            score.game_over()
        if player.ycor() > 270:

            player.goto(0, -280)
            score.leveling_up()
            player.speeding_up()
            car.speeding_up()

screen.exitonclick()
