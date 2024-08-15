from turtle import Turtle
import random

blocks_list = []

BLOCK_HEIGHT = 1.5
BLOCK_LENGTH = 3

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

level_1 = []


def check_blocks(ball_x, ball_y):
    for block in blocks_list:
        if ((block.ycor() - (BLOCK_HEIGHT * 18)) < ball_y < (block.ycor() + (BLOCK_HEIGHT * 18))
                and (block.xcor() - (BLOCK_LENGTH * 18)) < ball_x < (block.xcor() + (BLOCK_LENGTH * 18))):
            block.teleport(1000, 1000)
            result = "bottom hit"
            if block.ycor() - (BLOCK_HEIGHT * 11) < ball_y < block.ycor() + (BLOCK_HEIGHT * 11):
                result = "side hit"
            return result
            #TODO make block do something before disappearing? Would require 2 screen updates.


def create_level(level):
    if level == 1:
        colors = ["green", "red", "blue", "yellow", "orange", "purple"]
        blocks_per_row = int(CANVAS_WIDTH / (BLOCK_LENGTH * 20))
        x_cor = - (CANVAS_WIDTH / 2)
        y_cor = CANVAS_WIDTH / 2 - 60
        for color in colors:
            for n in range(blocks_per_row):
                block = Block()
                block.color("black", color)
                block.teleport(x_cor, y_cor)
                x_cor += (BLOCK_LENGTH * 20)
            y_cor -= (BLOCK_HEIGHT * 20)
            x_cor = - (CANVAS_WIDTH / 2)


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=BLOCK_HEIGHT, stretch_len=BLOCK_LENGTH, outline=3)
        self.penup()
        self.setheading(180)
        blocks_list.append(self)
