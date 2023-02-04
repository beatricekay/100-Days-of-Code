# Turtle Challenge 4: Generate a Random Walk
# Use a list of randomly generated colours

import turtle as t
import random

timmy_the_turtle = t.Turtle()
t.colormode(255) # need to change color mode of the module, t

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for i in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()