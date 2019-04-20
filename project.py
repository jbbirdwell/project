import turtle

# build window
win = turtle.Screen()

# window title/color/size
win.title("csc2280 Project")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# p1 paddle
paddle_p1 = turtle.Turtle()
paddle_p1.speed(0)
# p1 paddle build
paddle_p1.shape('square')
paddle_p1.color('white')
paddle_p1.shapesize(stretch_wid=5, stretch_len=1)
# p1 paddle position
paddle_p1.penup()
paddle_p1.goto(-350, 0)

# p2 paddle
paddle_p2 = turtle.Turtle()
paddle_p2.speed(0)
# p2 paddle build
paddle_p2.shape('square')
paddle_p2.color('white')
paddle_p2.shapesize(stretch_wid=5, stretch_len=1)
# p2 paddle position
paddle_p2.penup()
paddle_p2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
# ball shape
ball.shape('circle')
ball.color('white')
# ball position
ball.penup()
ball.goto(0, 0)
# ball movement
ball.dx = 100
ball.dy = 100

# Pen
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Calibri", 24, "normal"))

# Keeping Score
score_p1 = 0
score_p2 = 0

# move paddle_p1 up and down
# paddle_p1 up
def paddle_pl_up():
    y = paddle_p1.ycor()
    y += 20
    paddle_p1.sety(y)

# paddle_p1 down
def paddle_pl_down():
    y = paddle_p1.ycor()
    y -= 20
    paddle_p1.sety(y)

# paddle_p2 up
def paddle_p2_up():
    y = paddle_p2.ycor()
    y += 20
    paddle_p2.sety(y)

# paddle_p2 down
def paddle_p2_down():
    y = paddle_p2.ycor()
    y -= 20
    paddle_p2.sety(y)

# actually moving the paddle
win.listen()
win.onkeypress(paddle_pl_up, "a")
win.onkeypress(paddle_pl_down, "s")
win.onkeypress(paddle_p2_up, "Up")
win.onkeypress(paddle_p2_down, "Down")

# game loop
while True:
    win.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # create border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        
        # updating score
        score_p1 += 1    
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align = "center", font = ("Calibri", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

        # updating score
        score_p2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align = "center", font = ("Calibri", 24, "normal"))

    
    # paddle/ball interaction
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_p2.ycor() + 40 and ball.ycor() > paddle_p2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_p1.ycor() + 40 and ball.ycor() > paddle_p1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


