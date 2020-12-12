from turtle import Turtle, Screen
import os

field_width = 1000
field_height = 600

pad_width = 80
pad_length = 20

ball_dia = 30

border_step = 50

score_player_1 = 0
score_player_2 = 0

FONT = ("Arial", 24, "bold")

window = Screen()
window.title("Fun_Pong")
window.bgcolor("#2F4F4F")
window.setup(width=field_width, height=field_height)
window.tracer(0)


player_1 = Turtle("square")
player_1.speed(0)
player_1.turtlesize(stretch_wid=4, stretch_len=1)
player_1.color("#FF4500")
player_1.penup()
player_1.goto((border_step - field_width/2), 0)


player_2 = Turtle("square")
player_2.speed(0)
player_2.turtlesize(stretch_wid=4, stretch_len=1)
player_2.color("#FF4500")
player_2.penup()
player_2.goto((field_width/2 - border_step), 0)


ball = Turtle("circle")
ball.speed(0)
ball.turtlesize(1.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4


score_1 = Turtle()
score_1.speed(0)
score_1.color("white")
score_1.penup()
score_1.hideturtle()
score_1.goto(-250, 250)
score_1.write("PLAYER 1: 0", align="center", font=FONT)


score_2 = Turtle()
score_2.speed(0)
score_2.color("white")
score_2.penup()
score_2.hideturtle()
score_2.goto(220, 250)
score_2.write("PLAYER 2: 0", align="center", font=FONT)


border = Turtle()
border.speed(0)
border.color("white")


def draw_border():
    border.pensize(4)
    border.penup()
    border.setposition(0, -field_height/2)
    border.setheading(90)
    border.pendown()

    for _ in range(field_height // 50):
        border.forward(50 / 2 + 1)
        border.penup()
        border.forward(50 / 2 + 1)
        border.pendown()


def player_1_up():
    y = player_1.ycor()
    if y < (field_height/2 - pad_width/2):
        y += 20
        player_1.sety(y)


def player_1_down():
    y = player_1.ycor()
    if y > (pad_width/2 - field_height/2):
        y -= 20
        player_1.sety(y)


def player_2_up():
    y = player_2.ycor()
    if y < (field_height/2 - pad_width/2):
        y += 20
        player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    if y > (pad_width/2 - field_height/2):
        y -= 20
        player_2.sety(y)


if __name__ == '__main__':

    window.listen()
    window.onkey(player_1_up, 's')
    window.onkey(player_1_down, 'z')
    window.onkey(player_2_up, 'Up')
    window.onkey(player_2_down, 'Down')

    draw_border()

    while True:
        window.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > field_height/2 - ball_dia/2:
            ball.sety(285)
            ball.dy *= -1
            os.system('afplay bounce.wav&')

        if ball.ycor() < ball_dia/2 - field_height/2:
            ball.sety(-285)
            ball.dy *= -1
            os.system('afplay bounce.wav&')

        if ball.xcor() > field_width/2 - ball_dia/2:
            ball.goto(0, 0)
            ball.dx *= -1
            score_player_1 += 1
            score_1.clear()
            score_1.write(f'PLAYER 1: {score_player_1}',
                          align='center', font=FONT)

        if ball.xcor() < ball_dia/2 - field_width/2:
            ball.goto(0, 0)
            ball.dx *= -1
            score_player_2 += 1
            score_2.clear()
            score_2.write(f'PLAYER 2: {score_player_2}',
                          align='center', font=FONT)

        if ball.xcor() < (pad_length/2 + border_step + ball_dia/2) - field_width/2 and ball.ycor() < (player_1.ycor() + pad_width/2) and ball.ycor() > (player_1.ycor() - pad_width/2):
            ball.setx(-425)
            ball.dx *= -1
            os.system('afplay bounce.wav&')

        if ball.xcor() > field_width/2 - (pad_length/2 + border_step + ball_dia/2) and ball.ycor() < (player_2.ycor() + pad_width/2) and ball.ycor() > (player_2.ycor() - pad_width/2):
            ball.setx(425)
            ball.dx *= -1
            os.system('afplay bounce.wav&')
