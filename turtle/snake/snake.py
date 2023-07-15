from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    segments = []

    def __init__(self, start_segments_num=3):
        for i in range(start_segments_num):
            self.new_segment((-20 * i, 0))
        self.head = self.segments[0]

    def move_forward(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x, new_y = self.segments[i-1].pos()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)

    def new_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        self.new_segment(self.segments[-1].pos())

    def detect_collision_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.pos() == segment.pos():
                return True
        return False

    def set_heading(self, x):
        if (x + 180) % 360 != self.head.heading():
            self.head.setheading(x)

    def head_up(self):
        self.set_heading(UP)

    def head_down(self):
        self.set_heading(DOWN)

    def head_left(self):
        self.set_heading(LEFT)

    def head_right(self):
        self.set_heading(RIGHT)
