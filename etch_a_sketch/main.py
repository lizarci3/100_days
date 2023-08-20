from turtle import Turtle, Screen

lizzy = Turtle()
screen = Screen()
step_size = 10

def move_forwards():
    lizzy.forward(step_size)

def move_backwards():
    lizzy.backward(step_size)

def counter_clockwise():
    current_heading = lizzy.heading()
    lizzy.setheading(current_heading + 5)

def clockwise():
    current_heading = lizzy.heading()
    lizzy.setheading(current_heading - 5)


def clear():
    lizzy.clear()
    lizzy.penup()
    lizzy.home()
    lizzy.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_forwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")

screen.onkey(fun=clear, key="c")

screen.exitonclick()