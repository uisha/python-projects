from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

t.showturtle()
cnt = 0


def move_forward():
    t.fd(10)


def move_backward():
    t.backward(10)


def turn_right():
    t.rt(5)


def turn_left():
    t.lt(5)


def clear():
    t.reset()


def hide_cursor():
    global cnt
    if cnt == 0:
        t.hideturtle()
        cnt += 1
    else:
        t.showturtle()
        cnt -= 1


screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backward, key='Down')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkeypress(fun=clear, key='c')
screen.onkeypress(fun=hide_cursor, key='space')
screen.listen()
screen.exitonclick()