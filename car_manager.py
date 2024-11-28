
from turtle import Turtle
import random


First_MOVING = 7
MOVE_INCREMENT = 4


colors = ["red", "green", "yellow", "black", "pink", "orange", "blue"]


class Car (Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.car_speed = First_MOVING

    def creating_cars(self):
        rand_choice = random.randint(1, 6)
        if rand_choice == 1:
            vehicle = Turtle()
            vehicle.shape("square")
            vehicle.color(random.choice(colors))
            vehicle.shapesize(stretch_len=2, stretch_wid=1)
            vehicle.penup()
            random_y = random.randint(-240, 250)
            vehicle.goto(x=-310, y=random_y)
            self.cars.append(vehicle)

    def moving_the_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def speeding_up(self):
        self.car_speed += MOVE_INCREMENT

























