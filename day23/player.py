# Control turtle to move across the screen

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10 # how much the turtle moves each time
FINISH_LINE_Y = 280 # finishing line position

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup() # turtle remains a shape and does not draw when moving
        self.go_to_start() # reference the function created in later lines to go back to starting position
        self.setheading(90) # turtle faces North in the beginning

    def goup(self):
        self.forward(MOVE_DISTANCE) 

    # Player to go back to starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Detect if player has passed the finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False