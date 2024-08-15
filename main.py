import turtle
import time
from turtle import Screen

import blocks
from player import Player
from ball import Ball
from score import Score

LIVES = 3

def check_break():
    ball_y = ball.ycor()
    ball_x = ball.xcor()
    direction = blocks.check_blocks(ball_x, ball_y)
    if direction == "bottom hit":
        ball.change_direction_y()
        return True
    elif direction == "side hit":
        ball.change_direction_x()
        return True
    else:
        return False

def check_bat():
    if (player.ycor() - 20) < ball.ycor() < (player.ycor() + 20):
        if (player.xcor() - 50) < ball.xcor() < (player.xcor() + 50):
            ball.change_direction_y()
    #TODO if i'm going to change the bat size, i have to make check_bat dependent on the bat size.


screen = Screen()
screen.screensize(600, 400)
screen.bgcolor("black")
screen.colormode(255)
screen.title("BREAKOUT")
screen.listen()
screen.tracer(0)

player = Player()
ball = Ball()
scorekeeper = Score()

game_on = True
game_speed = 0.02
level = 1
nr_lives = 3
lives = []
lives_x_cor = 260

for n in range(LIVES):
    y_cor = 280
    life = Ball()
    life.teleport(lives_x_cor, y_cor)
    lives_x_cor -= 35
    lives.append(life)
    print(lives)


screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=player.move_right, key="Right")

blocks.create_level(level)
scorekeeper.score_keeping()

while game_on:
    time.sleep(game_speed)
    ball.move()
    if check_break():
        scorekeeper.score += 1
        scorekeeper.score_keeping()
    check_bat()
    if ball.check_bottom():
        nr_lives -= 1
        lives[-1].teleport(1000, 1000)
        lives.pop()
        print(lives)
    if nr_lives < 1:
        scorekeeper.game_over()
        ball.teleport(1000, 1000)
        screen.update()
        game_on = False
    screen.update()

"""
- work with 3 lives? can get extra by hitting special brick or completing level
- things randomly dropping from the sky that can make the bat longer or shorter

"""
screen.exitonclick()
