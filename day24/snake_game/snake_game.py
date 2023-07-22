# main snake function
from turtle import Screen
from snake import Snake # import Snake class 
from food import Food # import Food class
from scoreboard import Scoreboard # import Scoreboard class
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turn tracer off so that one by one animations do not show

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    ## Step 4: Detect collision with food
    # turtle.distance() method returns the distance between 2 turtles
    if snake.head.distance(food) < 15:
        # Food will reappear in a random location
        food.refresh() 

        # Extend itself after eating food
        snake.extend()

        ## Step 5: Create a scoreboard
        # Increase score whenever snake collides with the food
        scoreboard.increase_score()

    ## Step 6: Detect collision with wall
    # Set a boundary that is at around 280 px x 280 px in size
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    ## Step 7: Detect collision with tail
    # If head collides with any segment in the tail, trigger game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()