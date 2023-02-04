# Extract a list of RGB tuples from the image
import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg',20)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# We delete the first 3 colours because they are very close to the colour white 
colour_list = [(200, 167, 110), (237, 241, 246), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46)]

# Create a painting with 10 x 10 dots which are size 20 and spaced apart by 50
t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()

for i in range(1, 11):

    for j in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)
        
    timmy.setx(0)
    timmy.sety(50*i)

screen = t.Screen()
screen.exitonclick()

