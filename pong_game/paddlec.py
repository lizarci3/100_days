from turtle import Turtle

STEP_MOVE = 50

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.setposition(coordinates)

    def move_up(self):
        self.sety(self.ycor() + STEP_MOVE)

    def move_down(self):
        self.sety(self.ycor() - STEP_MOVE)