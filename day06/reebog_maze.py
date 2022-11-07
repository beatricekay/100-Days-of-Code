def turn_right():
    turn_left()
    turn_left()
    turn_left()

# handles scenario of infinite loop where there is no right wall for the robot from the start
# we make the robot move till he faces a wall, and have him turn left/right 
while front_is_clear() == True:
    move()
turn_left()

while at_goal() == False:
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
