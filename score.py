from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.borders()
        self.score = 0

    def borders(self):
        self.pensize(2)
        self.teleport(0, 300)
        self.setheading(0)
        self.forward(450)
        self.setheading(270)
        self.forward(600)
        self.setheading(180)
        self.forward(900)
        self.setheading(90)
        self.forward(600)
        self.setheading(0)
        self.forward(450)

    def score_keeping(self):
        self.teleport(-250, 270)
        self.clear()
        self.write(f"Score: {self.score}",
                   move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.teleport(0, -100)
        self.clear()
        self.write("GAME OVER!",
                   move=False, align='center', font=('Arial', 80, 'bold'))
