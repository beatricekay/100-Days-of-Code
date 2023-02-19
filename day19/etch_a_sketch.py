from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home() # move the turtle back to origin coordinates (0,0)
    
screen.listen()
# Control turtle movement with the spacebar
screen.onkey(key="w", fun=move_forward) # parentheses not needed as function is in an argument
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()