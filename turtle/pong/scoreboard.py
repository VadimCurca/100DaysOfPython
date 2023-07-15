from turtle import Turtle
from settings import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, SCREEN_MAX_Y - 70)
        self.score_left = 0
        self.score_right = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", False, align="center", font=("Courier", 60, "bold"))

    def increment_left(self):
        self.score_left += 1
        self.write_score()

    def increment_right(self):
        self.score_right += 1
        self.write_score()
