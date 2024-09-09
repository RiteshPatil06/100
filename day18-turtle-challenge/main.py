import turtle
import random
from turtle import *
import colorgram


timmy = Turtle()
timmy.shape('turtle')
timmy.speed(10)
turtle.colormode(255)
rgb_colors = [(252, 249, 241), (253, 245, 251), (241, 252, 246), (243, 247, 252), (241, 228, 58), (220, 150, 79), (186, 67, 30), (234, 46, 112), (192, 12, 35), (40, 206, 88), (18, 19, 48), (40, 93, 171), (36, 34, 151), (233, 225, 5), (94, 186, 216), (66, 13, 43), (195, 39, 76), (200, 13, 7), (234, 61, 37), (51, 24, 13), (220, 161, 12), (217, 135, 180), (87, 209, 147), (25, 145, 35), (97, 235, 176), (13, 198, 217), (242, 159, 194), (94, 75, 12), (81, 85, 209), (13, 37, 30)]
count = 0
timmy.penup()
timmy.setx(-300)
timmy.sety(-300)
while count < 10:
    for _ in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)

    for _ in range(1):
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.left(180)

    count += 1




screen = turtle.Screen()
screen.exitonclick()