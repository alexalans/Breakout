from turtle import Turtle

START = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.color("white")
        self.penup()
        self.teleport(0, -280)

    def move_left(self):
        if self.xcor() > - 320:
            self.setheading(180)
            self.fd(15)

    def move_right(self):
        if self.xcor() < 320:
            self.setheading(0)
            self.fd(20)


