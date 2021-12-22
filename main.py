from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="make a bet", prompt="which turtle gonna win the race? type the color: ")
color = ["red", "green", "blue", "yellow", "purple", "orange"]

tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x=-230, y=-100)

tom = Turtle(shape="turtle")
tom.penup()
tom.color("green")
tom.goto(x=-230, y=-70)

jim = Turtle(shape="turtle")
jim.penup()
jim.color("blue")
jim.goto(x=-230, y=-40)

jam = Turtle(shape="turtle")
jam.penup()
jam.color("yellow")
jam.goto(x=-230, y=-10)


tad = Turtle(shape="turtle")
tad.penup()
tad.color("purple")
tad.goto(x=-230, y=20)

tad = Turtle(shape="turtle")
tad.penup()
tad.color("orange")
tad.goto(x=-230, y=50)

screen.exitonclick()
