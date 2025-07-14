from turtle import Turtle

AlIGN = 'center'
FONT = ('Courier', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color('red')
        self.penup()
        self.goto(0, 380)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Lives: {self.lives}", align=AlIGN, font=FONT)

    def live_score(self):
        self.lives -= 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Player Loss!",align="center",font=FONT)

    def game_won(self):
        self.goto(0,0)
        self.write("Player won!",align="center",font=FONT)