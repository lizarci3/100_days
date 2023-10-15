from turtle import Turtle
import random

class Food(Turtle):

    """
    All sknakes gotta eat!
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")

        # randomly go to a location on the screen
        # as long as it is not too close to the edge
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def refresh(self):
        # randomly go to a location on the screen
        # as long as it is not too close to the edge
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)