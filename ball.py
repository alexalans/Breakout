from turtle import Turtle
import random

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.2, 1.2, 1.2)
        self.penup()
        self.start_angle()
    def move(self):
        self.fd(5)
        x = self.xcor()
        if x > 300:
            self.change_direction_x()
        if x < -300:
            self.change_direction_x()
        y = self.ycor()
        if y > 280:
            self.change_direction_y()

    def change_direction_y(self):
        self.setheading(360 - (self.heading()))

    def change_direction_x(self):
        self.setheading(180 - (self.heading()))

    def new_ball(self):
        self.home()
        self.start_angle()

    def check_bottom(self):
        if self.ycor() < - 300:
            self.new_ball()
            return True

    def start_angle(self):
        angle = random.randint(0, 360)
        if 75 < angle < 105:
            self.start_angle()
        elif 255 < angle < 285:
            self.start_angle()
        else:
            self.setheading(angle)
