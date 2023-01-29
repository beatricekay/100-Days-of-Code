# Day 17: The Quiz Project & The Benefits of OOP
## Concepts
* How to create a Class in Python
* Working with Attributes, Class Constructors and the init() Function
* Adding Methods to a Class

## Learning Points
* A ```class``` is a blueprint for creating an ```object```.
* Key benefits of OOP is that it allows for code modularity - code which is separated into independent modules. This makes it easier to test and refactor/modify code independently without drastically affecting one another. 

#### Constructors ```__init__```
* Constructors help us to specify what should happen when our object is being constructed
* This is also known as initializing an object - set variables or counters to their starting values
* We use an ```__init__``` function() to initialize the values. This function is called everytime we create an object from the class

#### Attributes
* Attributes can either be:
  1) Created inside the ```___init___``` function. This will require a parameter to be specified inside the function and when creating the object
  2) Specified outside the class by assigning the attribute to the object
  
#### Methods
* A method will always need to have a ```self``` parameter as the first parameter
* When a method is called, it will always have to reference the object that called it
* Self is used to tell the class to refer to the object that is calling it
