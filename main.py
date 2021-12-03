import random
from turtle import Turtle, Screen

new_turtle = Turtle()
new_turtle.hideturtle()
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the"
                                                              " race? Enter a color")
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y = -100
is_race_on = False
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"First place is taken by {winner} turtle. You won!")
            else:
                print(f"You lost. The winner is {winner} turtle")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()