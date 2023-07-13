from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.exitonclick()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.setheading(tim.heading() - 10)


def rotate_counterclockwise():
    tim.setheading(tim.heading() + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def main():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=rotate_counterclockwise)
    screen.onkey(key="d", fun=rotate_clockwise)
    screen.onkey(key="c", fun=clear_screen)


if __name__ == "__main__":
    main()
