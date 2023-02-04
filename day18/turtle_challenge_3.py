# Turtle Challenge 3: Drawing Different Shapes
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

colours = ["crimson","tomato","gold","medium sea green","medium slate blue","light sky blue"]

for n in range(3, 11):
    angle = ((n-2)*180)/n
    timmy_the_turtle.color(random.choice(colours))
    for sides in range(0, n):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(180-angle)

screen = Screen()
screen.exitonclick()
