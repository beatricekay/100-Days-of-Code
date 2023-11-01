# Day 27: Tkinter, *args, **kwargs and Creating GUI Programs
## Concepts
* Creating Windows and Labels with Tkinter
* Setting Default Values for Optional Arguments inside a Function Header
* *args and **kwargs
* Buttons, Entry, and Setting Component Options
* Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more
* Tkinter Layout Managers: pack(), place() and grid()
  
## Learning Points
### Arguments with Default Values
* You can specify the default values when defining the function from the start. To change the values, you just define the value again when caling the function.
``` python
def my_function(a=1, b=2, c=3): 
```
* You can tell a function has default values when the pop up shows that the argument=...

### *args - Unlimited Positional Arguments
* Allows for flexible number of arguments:
``` python
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
```
* You can rename ```args``` to be anything you want, just remember to add the asterisk * at the start.
* The variable args is a tuple and can be accessed by index.

### *kwargs - Keyword Arguments
* Allow for arbitary number of keywords
``` python
def calculate(**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)
```
* ```kwargs``` is a dictionary so you can reference the value assigned to the key words the same way.
