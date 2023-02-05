# Day 19: Instances, State and Higher Order Functions
## Concepts
* Python Higher Order Functions & Event Listeners
* Object State and Instances
* The Turtle Coordinate System

## Learning Points
* Turtle Event Listeners: https://docs.python.org/3/library/turtle.html#turtle.listen

### Higher Order Functions
* When a function is used as an argument, we do not need to put the parentheses. For example:
```
def function_a(something):
    # Do this with something
    
def function_b():
    # Do this action

# Call function_a() using function_b as an input but we pass the name without the parentheses
function_a(function_b) 
```
* Another example:
```
def add(n1, n2):
    return n1 + n2

def calculator(n1, n2, func): # calculator() is the Higher Order Function
    return func(n1, n2)

result = calculator(2, 3, add)
```
