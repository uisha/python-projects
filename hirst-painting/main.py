# import colorgram as cg
#
# colors = cg.extract('image.jpg', 10)
#
# rgb_colors = []
#
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# screen size = 400 x 300
from turtle import Turtle, Screen, colormode
import random as r

# import setup
t = Turtle()
screen = Screen()

# color and dot setup
t.hideturtle()
t.penup()
t.speed(10)
t.setpos(-225, -225)
color_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211), (114, 83, 59)]
colormode(255)

# turtle movement
for y in range (10):
    for _ in range(10):
        t.dot(20, r.choice(color_list))
        t.fd(50)
    t.setpos(-225, t.ycor() + 50)


screen.exitonclick()