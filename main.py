from turtle import Turtle, Screen

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

# tim = Turtle(shape='turtle')
#
# tim.goto(x=-230.0, y=0)

screen.exitonclick()
