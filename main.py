from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=400, width=500)
screen.exitonclick()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


is_race_on = False
all_turtles = []


def create_turtles():
    distance = 0
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.speed(1)
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(-230, -100 + distance)
        distance += 40
        all_turtles.append(new_turtle)


create_turtles()
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

