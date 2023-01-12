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
    def sort_score_board(self):
        scores = []
        with open('high_scores.txt', 'r') as f:
            for line in f:  
                score = line[7::1] # To get the score from the text
                print(score)
                scores.append(int(score))
                scores = sorted(scores)
                scores = scores[::-1]
                print("sorted array: ", sorted(scores))

        with open('high_scores.txt', 'w') as f:
            for score in scores:
                print("score", score)  
                f.write(f"Score: {score}")
                f.write("\n")