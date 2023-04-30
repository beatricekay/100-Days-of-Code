# Day 21: Build the Snake Game Part 2: Inheritance & List Slicing
## Content
* Class Inheritance 
* How to Slice Lists & Tuples in Python

## Learning Points:
### Class Inheritance
* Inheriting behaviour (methods) and appearance (attributes) of an existing class
```
# Fish class is inheriting from Animal class
class Fish(Animal): 
  def __init__(self):
  
  # Command to for Fish class inherit from "super" Animal class
    super().__init__() 
```

* If we want to inherit a method and add on to it
```
class Animal:
  def __init__(self):
    self.num_eyes = 2
  
  def breathe(self):
    print("Inhale, exhale.")
    
# Fish class to inherit from Animal class
class Fish(Animal):
  def __init__(self):
    # Inherit all attributes
    super().__init__()
  
  def breathe(self):
    super().breathe()
    # Adding to the breathe() method
    print("doing this underwater.") 
```
