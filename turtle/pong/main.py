from turtle import Turtle, Screen
from bar import Bar
from ball import Ball
import settings
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=settings.SCREEN_WIDTH, height=settings.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


def main():
    left_bar = Bar(-370)
    right_bar = Bar(360)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(right_bar.move_up, "Up")
    screen.onkey(right_bar.move_up, "Left")
    screen.onkey(right_bar.move_down, "Down")
    screen.onkey(right_bar.move_down, "Right")

    screen.onkey(left_bar.move_up, "w")
    screen.onkey(left_bar.move_up, "a")
    screen.onkey(left_bar.move_down, "s")
    screen.onkey(left_bar.move_down, "d")

    game_running = True
    while game_running:
        ball.move(left_bar, right_bar)

        if ball.left_collision():
            scoreboard.increment_right()
            time.sleep(2)
            ball.reset()

        if ball.right_collision():
            scoreboard.increment_left()
            time.sleep(2)
            ball.reset()

        screen.update()
        # time.sleep(0.01)

    screen.exitonclick()


if __name__ == "__main__":
    main()
