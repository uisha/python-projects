from turtle import Turtle

MOVE_DISTANCE = 15


class Paddle(Turtle):

    def __init__(self, STARTING_COORDINATES):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.goto(STARTING_COORDINATES)

    def go_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -225:
            self.sety(self.ycor() - MOVE_DISTANCE)
