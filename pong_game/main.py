from turtle import Screen, Turtle
from paddlec import Paddle
from ball import Ball
import time

LEFT_PADDLE_COORDINATES = (-350, 0)
RIGHT_PADDLE_COORDINATES = (350, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

## Setting up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong game!")
screen.tracer(0)

#start the paddles and ball
paddle_left = Paddle(LEFT_PADDLE_COORDINATES)
paddle_right = Paddle(RIGHT_PADDLE_COORDINATES)
ball = Ball()

# allow the screen to receive user input
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")


# game logic
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.move()
    screen.update()

    # detect a collision with the top or bottom wall
    if (ball.position()[1] > (SCREEN_HEIGHT/2 - 15)) or (ball.position()[1] < -(SCREEN_HEIGHT/2 - 15)):
        ball.bounce_y()

    # detect a colliciton with right or left paddle
    if ((ball.distance(paddle_right)<50) and (ball.xcor() > 330)) or ((ball.distance(paddle_left)<50) and (ball.xcor() < -330)):
        ball.bounce_x()



screen.exitonclick()
