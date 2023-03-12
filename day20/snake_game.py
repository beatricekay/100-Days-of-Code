from turtle import Screen, Turtle
from snake import Snake # import Snake class 
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turn tracer off so that one by one animations do not show

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up) # 90 degrees
screen.onkey(key="Down", fun=snake.down) # 270 degrees
screen.onkey(key="Left", fun=snake.left) # 180 degrees
screen.onkey(key="Right", fun=snake.right) # 0 degrees

game_is_on = True
while game_is_on: # keeps moving snake forward

    # This allows the snake to move forward in one piece
    screen.update() # shows all animations drawn before
    time.sleep(0.1) # adds 0.1 second delay before the animation and screen is refreshed
    snake.move()

screen.exitonclick()