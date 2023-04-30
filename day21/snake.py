# All things snake related is inside this Snake class
from turtle import Turtle

# Global Variable
# Makes it easier to change the variables
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() # calls create_snake() method everytime an object is created
        self.head = self.segments[0] # since we will reference the snake head multiple times

    # Step 1: Create a snake body
    ## By default each turtle has a size of 20 px by 20 px
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the snake when it eats food
        # Get the last segment by calling the -1 index
        # Add the new segment to the last segment's position
        self.add_segment(self.segments[-1].position())
    
    ## Step 2: Move the snake
    def move(self):
        # For turns, we make the segments go to where the previous segments are
        # Segment 3 goes to where Segment 2 was
        # Segment 2 goes to where Segment 1 was
        # Segment 1 is free to move as it decides the direction

        # Reference Segment 3 (2), Segment 2 (1) and Segment 1 (0) from their tuple coordinates in segments list
        # range(start, stop, step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        # Move first segment forward by 20 so that other segments can follow 
        self.head.forward(MOVE_DISTANCE)

    ## Step 3: Control the snake with keyboard
    def up(self):
        # Control the head - Segment 1
        # Disallow snake to move back up if it is already going down
        if self.head.heading() != DOWN:
            self.head.setheading(UP) # turn to 90 degree direction

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)