from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230.0, y=(index * 30) - 30)
    turtles.append(new_turtle)

while not is_race_on:
    for turtle in turtles:
        distance = randint(1, 10)
        turtle.forward(distance)
        position_x, position_y = turtle.position()

        if int(position_x) >= 230:
            winner = turtle.pencolor()
            print(f'el ganador es {winner}')
            is_race_on = True

            if user_bet == winner:
                print(f'Ganaste!!')
            else:
                print(f'Perdiste!!')

screen.exitonclick()
