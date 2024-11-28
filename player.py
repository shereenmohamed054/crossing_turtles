from turtle import Turtle


MOVEMENT = 7
MOVE_INCREMENT = 4


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(x=0, y=-280)
        self.car_speed = MOVEMENT

    def up(self):
        self.forward(self.car_speed)

    def speeding_up(self):
        self.car_speed += MOVE_INCREMENT




