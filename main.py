from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

GAME_STATE = "PLAY"
while GAME_STATE == "PLAY":
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()
