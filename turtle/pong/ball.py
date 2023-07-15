from turtle import Turtle
import random
from settings import *


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.penup()

        self.x, self.y = 0, 0
        self.acc_x, self.acc_y = 0, 0
        self.reset()

    def reset(self):
        self.x, self.y = 0, 0
        self.acc_x = -1
        self.acc_y = random.uniform(1.2, 1.4)

    def bar_collision(self, bar):
        for segment in bar.segments:
            if self.distance(segment) <= 20:
                return True
        return False

    def move(self, left_bar, right_bar):
        self.x += self.acc_x
        self.y += self.acc_y
        self.goto(self.x, self.y)

        if self.y > SCREEN_MAX_Y or self.y < SCREEN_MIN_Y:
            self.acc_y *= -1
            self.y += self.acc_y
            self.goto(self.x, self.y)

        if (self.bar_collision(left_bar) and self.acc_x < 0) or (self.bar_collision(right_bar) and self.acc_x > 0):
            self.acc_x *= -1
            self.x += self.acc_x * 1.2
            self.goto(self.x, self.y)

    def left_collision(self):
        if self.x < SCREEN_MIN_X:
            return True
        return False

    def right_collision(self):
        if self.x > SCREEN_MAX_X:
            return True
        return False
