# Turtle Challenge 1: Draw a Square

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

for i in range (0,4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
