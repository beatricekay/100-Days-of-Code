from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # keyword arguments
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

# 6 turtles in purple, blue, green, yellow, orange and red
# Turtle to go to the starting line, e.g. left side of the screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for i in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i]) 
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_coordinate[i]) 
    all_turtles.append(new_turtle)

# Only start the race once the user has made their bet
# If user_bet is true - if it has a value
if user_bet: 
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance) 

print(all_turtles)
screen.exitonclick()