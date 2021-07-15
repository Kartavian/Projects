# I am attempting to make Pongclone in pycharm without the video aid
import turtle
import winsound

pn = turtle.Screen()
pn.title("Pongclone by Kartavian")
pn.bgcolor("purple")
pn.setup(width=800, height=600)
pn.tracer(0)

# Score
score_a = 0
score_b = 0

# Create the Paddles
# Left paddle
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("lavender")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)

# right paddle
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("lavender")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("violet")
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = .05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("royal blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="Center", font=("Arial", 24, "normal"))


# Functions

# paddle_a functions

def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)


def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)


def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)


def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)


# Keyboard binding
pn.listen()
pn.onkeypress(p1_up, "w")
pn.onkeypress(p1_down, "s")
pn.onkeypress(p2_up, "Up")
pn.onkeypress(p2_down, "Down")

# Main Game loop

while True:
    pn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    # Top Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("Courier", 24, "normal"))

    # Left Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("Courier", 24, "normal"))

    # bounce off p2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 40) and (
            ball.ycor() > p2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # bounce off paddle_a
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < p1.ycor() + 40) and (
            ball.ycor() > p1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if score_a > 2:
        pen.write("Player 1 Wins")
        False
    if score_b > 2:
        pen.write("Player 2 Wins")
        False
main.mainloop()
