from turtle import Turtle


class Bar:
    def __init__(self, x_axis):
        self.segments = []
        self.new_segment((x_axis, 20))
        self.new_segment((x_axis, 0))
        self.new_segment((x_axis, -20))

    def new_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move_up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(30)

    def move_down(self):
        for segment in self.segments:
            segment.setheading(-90)
            segment.forward(30)
