from turtle import Turtle
import random


class Play_box(Turtle):

        def __init__(self):
            super().__init__()
            self.penup()
            self.color('white')
            self.shape('square')
            self.shapesize(stretch_len=4)
            self.goto(x=0, y=-300)

        def move_left(self):
            if self.xcor() > -420:
                new_x = self.xcor() - 10
                self.goto(new_x, self.ycor())

        def move_right(self):
            if self.xcor() < 420:
                new_x = self.xcor() + 10
                self.goto(new_x, self.ycor())