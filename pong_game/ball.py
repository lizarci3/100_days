from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1
        self.y_move = 1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.x_move = 1
        self.y_move = 1
    
    def increase_speed(self):
        self.x_move = self.x_move * 1.2
        self.y_move = self.y_move * 1.2
        