# Keep track of the score level
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250) # position level at the top left hand corner
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() # clear the level if not next level will overwrite over one another
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Do not clear the text as we want to keep the Level text in the top left corner
        # To show what Level the player ended when it is GAME OVER
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

