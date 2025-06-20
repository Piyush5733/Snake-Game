from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def boundary(self):
        border = Turtle()
        border.penup()
        border.goto(-290, 290)
        border.pendown()
        border.hideturtle()
        border.color("maroon")
        border.pensize(2)
        for _ in range(4):
            border.forward(580)
            border.right(90)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="circle")
        new_segment.penup()
        new_segment.color("dark green")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extent(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[seg_num - 1].xcor()
            y_cor = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_cor, y_cor)
        self.head.fd(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)
