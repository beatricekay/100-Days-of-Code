# Turtle Challenge 4: Generate a Random Walk
# Use a list of defined colours

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

colours = ["crimson","tomato","gold","medium sea green","medium slate blue","light sky blue"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for i in range(200):
    timmy_the_turtle.color(random.choice(colours))

    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
