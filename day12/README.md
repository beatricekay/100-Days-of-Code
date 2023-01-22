# Day 12: Scope & Number Guessing Game
## Content
* How to Modify a Global Variable
* Python Constants and Global Scope

## Learning Points
* Global scope: variable accessible anywhere outside a function
* Local scope: variable only accessible inside a function
* Python does not have block scope
* If you define a variable within a function, then it is only available within the function's local scope. Calling a variable outside of its local scope will result in a NameError.
* If you define a variable outside of a function, but within an if/for/while loop, then it does not count as creating a separate local scope and still exists within the global scope.
* To modify a global scope inside a function:
```
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
```
* You should generally avoid modifying global scope inside a local scope.
* You assign values that are constant/fixed to a global variable, e.g. pi
* You differentiate fixed variables from variables that might change by keeping them in UPPERCASE
