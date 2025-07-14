from turtle import Turtle
import random

start = [1, -1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.75)
        self.penup()
        self.x_move = random.choice(start)
        self.y_move = random.choice(start)
        self.moving_speed = 1.5  # initial speed

    def move(self):
        new_x = self.xcor() + self.x_move * self.moving_speed
        new_y = self.ycor() + self.y_move * self.moving_speed
        self.goto(new_x, new_y)

    def bounce_vertically(self):
        self.y_move *= -1
        if self.moving_speed < 15:
            self.moving_speed += 0.2

    def bounce_horizontally(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = random.choice(start)
        self.y_move = random.choice(start)
        self.moving_speed = 1.5
