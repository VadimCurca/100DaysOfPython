from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Courier", 40, "bold"))

    def increment(self):
        self.score += 1
        self.write_score()
