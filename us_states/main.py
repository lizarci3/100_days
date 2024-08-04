import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
screen.screensize(2,15)
image = 'blank_states_img.gif'

## Turtle image
screen.addshape(image)
turtle.shape(image)

## Turtle writer
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

states_locations = pd.read_csv('50_states.csv')
states_locations['state_lowered'] = states_locations['state'].str.lower()
all_states_names = states_locations['state_lowered'].to_list()

guessed_correctly = 0
list_guessed_states = []
while guessed_correctly < 50:

    typed_answer = screen.textinput(title=f"Guess the state {guessed_correctly}/50", prompt='Write down the state name')
    answer_state = typed_answer.lower()

    if answer_state in all_states_names:

        xy_state = states_locations[states_locations['state_lowered']==answer_state]
        x_state = xy_state['x'].unique()[0]
        y_state = xy_state['y'].unique()[0]

        writer.goto(x_state, y_state)
        writer.write(answer_state)
        list_guessed_states.append(answer_state)

        guessed_correctly += 1


turtle.mainloop()

