import turtle
import random


is_game_on = False
screen = turtle.Screen()
screen .setup(width=800, height=600)
user_bet = screen.textinput(title="Whats your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-360, y=y_position[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in turtles:
        if turtle.xcor() > 360:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} won the race!")
            else:
                print(f"You've lose! {winning_color} won the race!")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)





screen.exitonclick()