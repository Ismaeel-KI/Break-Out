from turtle import *
import time
from ball_logic import Ball
from playbox_logic import Play_box
from Score import Score


def brick_logic():
    bricks = []
    brick_y = [i for i in range(360, 60, -30)]
    brick_x_row1 = [i for i in range(-400, 400, 130)]
    brick_x_row2 = [i for i in range(-400, 400, 90)]
    brick_x_row3 = [i for i in range(-400, 400, 50)]

    for i, y in enumerate(brick_y):
        if i % 3 == 0:
            stretch_len = 6
            brick_x = brick_x_row1
            color = 'red'
        elif i % 2 == 1:
            stretch_len = 4
            brick_x = brick_x_row2
            color = 'blue'
        else:
            stretch_len = 2
            brick_x = brick_x_row3
            color = 'yellow'
        for x in brick_x:
            brick = Turtle()
            brick.color(color)
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=stretch_len)
            brick.penup()
            brick.goto(x=x, y=y)
            bricks.append(brick)
    return bricks


window = Screen()
window.bgcolor('black')
window.tracer(0)

# Brick placing
bricks = brick_logic()

# Paddle
play_box = Play_box()

window.listen()
window.onkeypress(play_box.move_left, "Left")
window.onkeypress(play_box.move_right, "Right")

# Ball
ball = Ball()

# Score
score = Score()

Game_on = True
while Game_on:

    window.update()
    score.update()
    ball.move()
    if (abs(ball.xcor() - play_box.xcor()) < 50  # half of paddle width
            and abs(ball.ycor() - play_box.ycor()) < 20):  # vertical range for collision
        ball.bounce_vertically()

    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_horizontally()

    if not bricks:
        score.game_won()
        Game_on = False

    for brick in bricks:
        if (abs(ball.xcor() - brick.xcor()) < 60 and
                abs(ball.ycor() - brick.ycor()) < 20):
            ball.bounce_vertically()
            brick.hideturtle()
            bricks.remove(brick)
            break

    if ball.ycor() < -360:
        if score.lives > 1:
            score.live_score()
            ball.reset_ball()
        else:
            score.game_over()
            Game_on = False
            time.sleep(1)

window.exitonclick()
