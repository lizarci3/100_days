from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # recovering the last known high score
        with open('snake_game\data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0,250)

    def update_score(self):
        """
        Every time it encounters food, score will go up
        """
        self.score = self.score + 1
        self.print_current_score()

    def print_current_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game\data.txt', mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.print_current_score()