from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="make a bet", prompt="which turtle gonna win the race? type the color: ")
color = ["red", "green", "blue", "yellow", "purple", "orange"]
y_positions = [-100, -70, -40, -10, 20, 50]
participants = []

for turtle_indexes in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_indexes])
    new_turtle.goto(x=-230, y=y_positions[turtle_indexes])
    participants.append(new_turtle)

if user_input:
    race_start = True


while race_start:

    for turtle in participants:
        if turtle.xcor() > 230:
            race_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"you've won,{winning_color} is the winner of this race")
            else:
                print(f"you've lost,{winning_color} is the winner of this race")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
