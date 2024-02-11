from turtle import Screen
from snake import Snake
import time

from food import Food
from scoreboard import Scoreboard

## Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)

game_is_on = True
i = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    scoreboard.print_current_score()
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if the head collides with any segment in the tail:
    #   trigger game_over
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()