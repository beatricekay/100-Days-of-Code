from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400) # keyword arguments
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

# 6 turtles in purple, blue, green, yellow, orange and red
# Turtle to go to the starting line, e.g. left side of the screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-150, -100, -50, 0, 50, 100]

for i in range (0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_coordinate[i]) 



screen.exitonclick()