import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600) # x and y can range from -300 to 300
screen.tracer(0) # turn off turtle animation

player = Player() # create a player object from the Player class
car_manager = CarManager()
scoreboard = Scoreboard()

## Step 1: Move the turtle with the keypress
screen.listen() # listen for keyboard strokes
screen.onkey(player.goup, "Up") # move the turtle with the Up key
# when calling functions within a function, you can exclude the parentheses ()

game_is_on = True
while game_is_on:
    time.sleep(0.1) # screen refreshed every 0.1 second
    screen.update()

    ## Step 2: Create and move the cars
    car_manager.create_car() # create a new car every 0.1 second
    car_manager.move_cars() # move all cars by 5 spaces

    ## Step 3: Detect collision with car
    # Check distance between turtle player and each car
    for car in car_manager.all_cars:
        if car.distance(player) < 20: # distance is measured from centre of each turtle
            game_is_on = False
            scoreboard.game_over()

    ## Step 4: Detect when turtle reaches the other side and increase its speed
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

    ## Step 5: Create a scoreboard (Level Up, Game Over)
    # Update scoreboard each time level increases
        scoreboard.increase_level()

screen.exitonclick()