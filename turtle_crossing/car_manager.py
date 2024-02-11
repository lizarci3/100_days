from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.shape("square")
        self.shapesize(1,2)
        self.setposition(randint(-300, 1000), randint(-250, 250))

        self.x_move = STARTING_MOVE_DISTANCE
        self.y_move = STARTING_MOVE_DISTANCE

    def move(self):
        new_y = self.ycor()
        new_x = self.xcor() - self.x_move

        if self.xcor() < -400:
            new_x = randint(300, 1000)
            new_y = randint(-250, 250)
            
        self.goto(new_x, new_y)

    def new_level(self):
        self.x_move = self.x_move + MOVE_INCREMENT

    def game_over(self):
        self.x_move = 0