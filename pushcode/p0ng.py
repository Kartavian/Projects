# Attempt at Pong
# by Loren Stevenson

import turtle
import winsound

pn = turtle.Screen()
pn.title("P0NG by Kartavian")
pn.bgcolor("black")
pn.setup(width=800, height=600)
pn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = -.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="Center", font=("Courier", 24, "normal"))


# Functions

# paddle_a functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
pn.listen()
pn.onkeypress(paddle_a_up, "w")
pn.onkeypress(paddle_a_down, "s")
pn.onkeypress(paddle_b_up, "Up")
pn.onkeypress(paddle_b_down, "Down")


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
        
    # Left Border
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
        
    
    # bounce off paddle_b
    if (ball.xcor () > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    # bounce off paddle_a
    if (ball.xcor () < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
pn.mainloop()