# Attempt at brick breaker
import random
import turtle

# Main Window
import winsound

bb = turtle.Screen()
bb.title("BrickBreakClone")
bb.bgcolor("black")
bb.setup(width=800, height=600)
bb.tracer(0)

# Player Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.penup()
pen.hideturtle()
pen.goto(0, -260)
pen.write("Brick Break Pinecones Score: 0", align="Center", font=("Courier", 24, "normal"))

colors = ['red', 'blue', 'green', 'cyan', 'lavender', 'violet', 'purple']
score = 0
# Functions Section
# Paddle Functions
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)
# Check the Border
def b_check():
    if ball.ycor()>280:
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def p_check():
    if ball.ycor() - 10 <= paddle.ycor() + 10 and ball.dy < 0:
        if ball.xcor() - 10 <= paddle.xcor() + 50 and ball.xcor() + 10 >= paddle.xcor() - 50:
            ball.dy *= -1


def f_block():
    for i in block_list:
        if i.state == 'falling':
            i.shape('circle')

            i.l = i.xcor() - 10
            i.r = i.xcor() + 10
            i.shapesize(1, 1)
            i.goto(i.xcor(), i.ycor() + i.dy)

# Keyboard Bindings
bb.listen()
bb.onkeypress(paddle_left, "Left")
bb.onkeypress(paddle_right, "Right")

# list for blocks
x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205, 180]
block_list = []

for i in y_list:
    for j in x_list:
        block = turtle.Turtle()
        block.shape('square')
        block.shapesize(stretch_len=5, stretch_wid=1)
        block.c = (random.choice(colors))
        block.color(block.c)
        block.up()
        block.goto(j, i)
        block.state = 'ready'
        block.l = block.xcor() - 50
        block.r = block.xcor() + 50
        block_list.append(block)

# Number of blocks to make
block_count = len(block_list)

# Gameplay Loop
while block_count > 0:

    bb.update()

    # Move the Ball
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
    b_check()
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    p_check()
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    f_block()
    winsound.PlaySound("break.wav", winsound.SND_ASYNC)

    # Border Checking

    # Bottom Border
    if ball.ycor() <= -300:
        ball.goto(0, 0)
        if score > 0:
            score -= 1
        pen.clear()
        pen.write(f'Brick Break Pinecones Score: {score}', align='center', font=('Courier', 24, 'normal'))

    # Block collisions
    for i in block_list:

        if (i.l <=ball.xcor() <= i.r) and (i.ycor()-10 <= ball.ycor() <= i.ycor()+10) and i.state == 'ready':
            ball.dy *= -1
            i.state = 'falling'
            i.dy = -2
            score += 1
            pen.clear()
            pen.write(f'Brick Break Pinecones Score: {score}', align='center', font=('Arial', 24, 'normal'))

        if (paddle.xcor() - 50 < i.xcor() < paddle.xcor() + 50) and (paddle.ycor() - 10 < i.ycor() <= paddle.ycor() + 10) and i.dy < 0:
            i.dy *= -1
        if i.ycor() < -320 or i.ycor()>320:
            block_list.remove(i)
            block_count = len(block_list)

pen.clear()
pen.goto(0, 0)
pen.write(f'Game Over\nScore: {score}', align='center', font=('Arial', 40, 'normal'))
bb.mainloop()