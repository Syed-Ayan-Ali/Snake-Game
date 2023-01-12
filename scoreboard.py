from turtle import Turtle

high_scores = []

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def show_score_board(self):
        for score in high_scores:
            self.write(f"Score: {score}", align="center", font = ("Arial", 24, "normal"))
            self.hideturtle()