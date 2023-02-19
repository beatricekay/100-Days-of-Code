from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
# Control turtle movement with the spacebar
screen.onkey(key="space", fun=move_forward) # parentheses not needed as function is in an argument
screen.exitonclick()