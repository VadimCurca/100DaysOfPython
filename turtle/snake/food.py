from turtle import Turtle
import random


class Food(Turtle):
    x, y = 0, 0

    def __init__(self):
        super().__init__(shape="square")
        super().penup()
        self.color("red")
        self.refresh()

    def refresh(self):
        self.x = random.randint(-(300-40)//20, (300-40)//20) * 20
        self.y = random.randint(-(300-40)//20, (300-40)//20) * 20
        self.goto(self.x, self.y)

