from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="make a bet", prompt="which turtle gonna win the race? type the color: ")
color = ["red", "green", "blue", "yellow", "purple", "orange"]
y_positions = [-100, -70, -40, -10, 20, 50]

for turtle_indexes in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[turtle_indexes])
    tim.goto(x=-230, y=y_positions[turtle_indexes])


screen.exitonclick()
