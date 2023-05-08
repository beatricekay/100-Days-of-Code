# Random cars passing across the screen
# Each car is a turtle itself, and measures 20 x 40 px

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] # colours of the cars
STARTING_MOVE_DISTANCE = 5 # starting move distance of the car at Level 1
MOVE_INCREMENT = 10 # how much the cars move each time


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Creates a new car instance
    def create_car(self):
        random_chance = random.randint(1,6) 

        if random_chance == 1: # generate a 1/6th chance to create a car
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2) # only need to stretch width from 20 to 40 px
            new_car.penup() # does not draw when car is moving along the screen
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250) # generate car at a random position but not in the top/bottom 50 px of the screen
            new_car.goto(300, random_y) # car starts from extreme right of the screen
            self.all_cars.append(new_car)

    # Moves the cars
    def move_cars(self):
        for car in self.all_cars:
            # backwards is used because turtles move from left to right
            car.backward(self.car_speed)

    # Increases car speed so that cars move faster
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
