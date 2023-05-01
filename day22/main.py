from turtle import Screen, Turtle
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time

## Step 1: Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0) # turn off animation when relocating paddle to starting position 

## Step 2: Create and move a paddle
## Step 3: Create another paddle (for a 2 player game)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

## Step 4: Create the ball and make it move
ball = Ball()

## Step 8: Keep score with a scoreboard
scoreboard = Scoreboard()

## Control paddles
screen.listen() # listen for keyboard strokes

# Control right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Control left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() # ball will keep moving while game is True

    ## Step 5: Detect collision with wall and bounce downwards
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    ## Step 6: Detect collision with paddle
    # Distance is measured from centre of ball and paddle, but we want to consider if the ball touches 
    # the paddle of the edge/corners as well
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 or ball.xcor() < -320:
        ball.bounce_x()

    ## Step 7: Detect when paddle misses
    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle miss
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
