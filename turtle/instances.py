from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def main():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    turtles = []

    for idx in range(len(colors)):
        turtle = Turtle(shape="turtle")
        turtles.append(turtle)
        turtle.fillcolor(colors[idx])
        turtle.penup()
        turtle.goto(x=-200, y=-150+60*idx)
        turtle.pendown()

    run = True
    while run:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.position()[0] >= 500//2 - 30:
                run = False
                break

    screen.exitonclick()


if __name__ == "__main__":
    main()
