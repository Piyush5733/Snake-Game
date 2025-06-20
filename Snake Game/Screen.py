from turtle import Screen
from snake_class import Snake
from score_board import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("medium sea green")
screen.title("WELCOME TO SNAKE GAME")


snake = Snake()
score = ScoreBoard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.boundary()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # score.game_over()
        score.reset_score()
        snake.reset_snake()

    # Detect collision with own body

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset_score()
            snake.reset_snake()
            pass


screen.exitonclick()
