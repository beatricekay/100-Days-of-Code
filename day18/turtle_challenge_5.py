# Turtle Challenge 5: Draw a Spirograph

import turtle as t
import random

timmy_the_turtle = t.Turtle()
t.colormode(255) # need to change color mode of the module, t

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy_the_turtle.speed("fastest")

def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(50)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()