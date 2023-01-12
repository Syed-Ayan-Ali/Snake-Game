from turtle import Turtle

high_scores = []

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.y = 250

    def show_score_board(self):
        with open('high_scores.txt', 'r') as f:
            for line in f:    
                self.goto(-280, self.y)
                self.y -= 20 
                self.color("white")
                self.write(f"Score: {line}", align="center", font = ("Courier", 15, "normal"))
                self.hideturtle()