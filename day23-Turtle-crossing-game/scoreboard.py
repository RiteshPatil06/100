from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(250, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}', align='left', font=('Arial', 16, 'bold'))
    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.write(f'GAME OVER', align='center', font=('Arial', 16, 'bold'))
