import time
from turtle import Screen
from player import Player
from cards import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = Car_Manager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

    if player.ycor() > 290:
        scoreboard.increase_score()
        player.reset()
        car_manager.speed_increase()






screen.exitonclick()