from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Key Listeners

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_STATE = "PLAY"
score = 0
i = 0

while GAME_STATE == "PLAY":
    screen.update()
    time.sleep(0.06)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.create_food()
        snake.increase()
        scoreboard.increase()

    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        GAME_STATE = "FINISHED"
        scoreboard.game_over()

    # detect collisions with itself
    
    for i in range(1,len(snake.segments) - 1):   
        if snake.head.distance(snake.segments[i]) < 10:
            GAME_STATE = "FINISHED"
            scoreboard.game_over()
     


screen.exitonclick()

