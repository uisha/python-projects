from turtle import Turtle, Screen, colormode
import random as r

t = Turtle()
screen = Screen()

t.shape("classic")
t.hideturtle()
colormode(255)
t.speed('fastest')
angle = 0.0
set_angle = 5

while angle < 360:
    t.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    t.circle(100)
    t.lt(set_angle)
    angle += set_angle

if 360//set_angle != 0:
    for _ in range(0, 3):
        t.undo()

screen.exitonclick()