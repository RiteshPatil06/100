from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} HighScore: {self.high_score}', align='center', font=('Arial', 16, 'bold'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 16, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update()
