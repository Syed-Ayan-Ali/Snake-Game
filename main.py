from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# Key Listeners

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_STATE = "PLAY"
while GAME_STATE == "PLAY":
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()

