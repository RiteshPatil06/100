from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)

