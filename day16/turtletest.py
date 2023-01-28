from turtle import Turtle, Screen # import Turtle and Screen classes

## TURTLE OBJECT
# Constructing an object turtle by assigning it to the Turtle() class
# Now the variable timmy contains a Turtle object from Turtle() class
timmy = Turtle()
# Calling methods associated with the turtle object
timmy.shape("turtle")
timmy.color("cadetblue1")
timmy.forward(100) 

## SCREEN OBJECT
# Creating an object my_screen by assigning it to Screen() class
my_screen = Screen()

# Calling attribute canvheight associated with the screen object
# (object).(attribute)
my_screen.canvheight # prints out canvas height
print(my_screen.canvheight) 

# Assessing method exitonclick() method from Screen() class
my_screen.exitonclick() 


