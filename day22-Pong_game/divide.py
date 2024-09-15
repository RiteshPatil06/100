from turtle import Turtle

class Divide_the_page(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, -200)
        self.goto(0, 200)
