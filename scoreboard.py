from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", False, 'center', FONT)

    def score_increase(self):
        self.score += 1
        self.update_score()

    def end_game(self):
        self.goto(0, 0)
        self.write(f"THE END", False, 'center', FONT)