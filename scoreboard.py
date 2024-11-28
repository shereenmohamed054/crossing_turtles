from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.levels()

    def levels(self):
        self.goto(x=-240, y=270)
        self.write(arg=f"Level : {self.level}", align="center", font=('Arial', 20, 'normal'))

    def leveling_up(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level : {self.level}", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over ", align="center", font=('Arial', 20, 'normal'))





