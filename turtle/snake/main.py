from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorebord import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def main():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.head_up, "Up")
    screen.onkey(snake.head_down, "Down")
    screen.onkey(snake.head_left, "Left")
    screen.onkey(snake.head_right, "Right")

    game_running = True
    while game_running:
        screen.update()
        time.sleep(0.1)
        snake.move_forward()

        if snake.head.distance(food) < 15:
            scoreboard.increment()
            snake.grow()
            food.refresh()

        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -290 \
                or snake.detect_collision_with_tail():
            scoreboard.game_over()
            game_running = False

    screen.exitonclick()


if __name__ == "__main__":
    main()

