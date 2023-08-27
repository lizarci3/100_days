from turtle import Turtle, Screen
import random

# placing bets
screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color: ")

######### setting up the racing track
screen_width = 1000
sceen_height = 800
screen.setup(width=screen_width, height=sceen_height)

######### initializing our turtle and its opponents
######### ready
is_race_on = True

########## set
colors_rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
start_of_race_x = 0 - screen_width/2 + 20 # the extra 20 is to give some padding to the position
start_of_race_y = 0 + ((len(colors_rainbow)/2)*50) 

all_turtles = []

for t in colors_rainbow:
    each_turtle = Turtle(shape="turtle")
    each_turtle.color(t)
    each_turtle.speed('fast')

    # initializing the position of the turtles
    each_turtle.penup()
    each_turtle.goto(x=start_of_race_x, y=start_of_race_y)
    
    start_of_race_y = start_of_race_y - 50
    all_turtles.append(each_turtle)

########### and go!
while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))

        if turtle.pos()[0] >= (screen_width/2 - 40):
            is_race_on = False
            
            winner = turtle.color()[0]

########## did you win?
if winner == user_bet:
    print(f"Congrats! your {user_bet} turtle won!")
else:
    print(f"You Loose, the winner was {winner}")


screen.exitonclick()