from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
step = 2


def move_forwards():
    tim.forward(step)


def move_backwards():
    tim.backward(step)


def rotate_counter_clockwise():
    tim.left(step)


def rotate_clockwise():
    tim.right(step)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key='e', fun=move_forwards)
screen.onkeypress(key='d', fun=move_backwards)
screen.onkeypress(key='s', fun=rotate_counter_clockwise)
screen.onkeypress(key='f', fun=rotate_clockwise)
screen.onkeypress(key='c', fun=clear_drawing)

screen.exitonclick()
