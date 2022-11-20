# Day 8: Function Parameters & Caesar Cipher
## Content
* Functions with Inputs
* Positional vs. Keyword Arguments

## Learning Points
* def function(parameter): v.s. function(argument).
* Paremeter is used when defining the function, while argument is used when calling the function. 
* Keyword arguments allow the repositioning of arguments. The order of the positional arguments does not matter, e.g. function(c=1, b=2, a=3) 
* np.ceil() and math.ceil() rounds up all numbers to its nearest integer. np.ceil() keeps the number as floating (will need int() if it needs to be converted to an integer), while math.ceil() converts it to an integer. 
* A prime number can only be divided by 1 and the number itself. 
* Note that range(2,2) returns no numbers at all while range(2,3) returns just the number 2.
* There are 2 ways to approach the Caeser Cipher project. 1) Include 2 sets of the alphabet in the alphabet list, 2) Have only 1 set of the alphabet and account for the numbers > 25 or < 1 by using the %.
