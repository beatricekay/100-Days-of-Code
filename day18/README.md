# Day 18: Turtle & the Graphical User Interface (GUI)
## Concepts
* Understanding Turtle Graphics and How to use the Documentation
* Importing Modules, Installing Packages, and Working with Aliases
* Python Tuples and How to Generate Random RGB Colours

# Learning Points
* Ways to import modules:
```
# Method 1
# Use this method if you're using multiple methods once or twice
import turtle
tim = turtle.Turtle()

# Method 2: don't have to put turtle. infront of everything
# Use this method if you're using the method multiple times
from turtle import Turtle
tim = Turtle()

# Method 3: 
# This method doesn't allow us to know which module the method is coming from
# Avoid using this import method
from turtle import *
```