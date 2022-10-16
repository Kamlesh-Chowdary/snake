from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=my_snake.up)
screen.onkey(key='Right', fun=my_snake.right)
screen.onkey(key='Left', fun=my_snake.left)
screen.onkey(key='Down', fun=my_snake.down)
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        scoreboard.reset_score()
        my_snake.reset_snake()

    for turtle in my_snake.turtles[1:]:
        if my_snake.head.distance(turtle) < 10:
            scoreboard.reset_score()
            my_snake.reset_snake()

screen.exitonclick()
