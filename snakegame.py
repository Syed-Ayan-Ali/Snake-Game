from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

GAME_STATE = "PLAY"

starting_position = [(0, 0), (20, 0), (40, 0)]

segment = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    
    segment.append(new_segment)



while GAME_STATE == "PLAY":
    screen.update()
    time.sleep(0.1)
    # To implement the behaviour where the snake can turn with the other segments connected,
    # we need to make sure the segments are linked to one another.

    # One way to do this is to start from the last segment and move it in the place of the second last segment
    # Then, move the second last segment to the third last segment and so on until to you reach the first segment, the head.
    # At this point, the head can turn in any direction and the same process will continue to repeat until the game ends.
    
    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)
        
    
    segment[0].left(90)
        
    segment[0].forward(20)    

screen.exitonclick()

