from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

# Key Listeners

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_STATE = "PLAY"
while GAME_STATE == "PLAY":
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.create_food()
        

screen.exitonclick()

