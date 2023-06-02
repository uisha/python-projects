from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
winner = str

y_pos = -125
for _ in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_pos)
    y_pos += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

if winner != user_bet:
    print(f"Sorry, you lost! {winner.capitalize()} won!")
else:
    print(f"Congrats, your turtle won!")

screen.exitonclick()
