from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0,250)

    def update_score(self):
        """
        Every time it encounters food, score will go up
        """
        self.score = self.score + 1

    def print_current_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER :P", align=ALIGNMENT, font=FONT)