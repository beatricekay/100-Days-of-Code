# Create a random location for snake food to appear
# Reappear in a random location once it is eaten by the snake

from turtle import Turtle # food will be a Turtle object
import random


class Food(Turtle): # inherit from Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()

        # By default each turtle has a size of 20 px by 20 px
        # Stretch by 0.5 to be a 10 px by 10 px circle
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # Set positions where food can appear to be not too close to the edge of the screen
        # If not this will be hard for the snake to eat the food
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
