from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
    
    def reset_level(self):
        self.setposition(STARTING_POSITION)
