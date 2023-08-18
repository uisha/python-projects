import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
title = "Guess the State"

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        title = f"Guessed {len(guessed_states)}/50 States"
screen.exitonclick()