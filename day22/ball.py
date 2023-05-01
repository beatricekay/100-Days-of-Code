from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup() # don't draw across screen when moving
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    ## Step 4: Create the ball and make it move
    def move(self):
        # move in a diagonal where x and y coordinates change, y = mx
        # x and y will change the same amount
        # amount that + will determine speed of the ball
        # ball only moves 1 pixel each time the screen updates
        # alternative is letting the screen sleep for a while between each ball move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    ## Step 5: Detect collision with wall and bounce
    # Bouncing in the y-axis
    def bounce_y(self):
        # y-coordinate has to go in the opposite direction
        self.y_move *= -1

    ## Step 6: Detect collision with paddle
    # Bouncing in the x-axis
    def bounce_x(self):
        # x-coordinate has to go in the opposite direction
        self.x_move *= -1
        # increase ball speed each time it hits the paddle
        # this reduces the sleep time of the screen updating so that it updates faster
        self.move_speed * 0.9

    ## Step 7: Detect when paddle misses
    def reset_position(self):
        self.goto(0,0)
        # reset move speed to original speed
        self.move_speed = 0.1
        # If right paddle player misses, ball resets and goes towards left paddle player and vice versa
        self.bounce_x()


