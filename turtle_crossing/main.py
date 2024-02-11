import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

# initiate the turtle crossing
turtle = Player()

# initiate the scoreboard
scoreboard = Scoreboard()

# initiate the cars
cars = []

for _ in range(30):
    car = CarManager()
    cars.append(car)

# allow the screen to receive user input
screen.listen()
screen.onkey(turtle.move_up, "Up")

# game logic
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for c in cars:
        c.move()

    # detect if the turtle has made it across safely
    if (turtle.position()[1] > (300)):
        turtle.reset_level()
        scoreboard.new_level()

        for c in cars:
            c.new_level()

    # detect a collision with a car
    for c in cars:
        if (turtle.distance(c)<20):
            scoreboard.game_over()
            
            game_is_on = False
            time.sleep(5)
            screen.update()
            



