# Day 24: Files, Directories and Paths
## Concepts
* How to Open, Read, and Write to Files using the "with" Keyword
* Relative and Absolute File Paths
* Add a High Score to the Snake Game

## Learning Points
### Reading and Writing to Files
* To read a file, there are 2 methods 
#### Method 1
```python
# Save the opened file to a variable
file = open("my_file.txt")

# Save the file contents into a variable
contents = file.read()
print(contents)

# Close file manually once done
file.close()
```

#### Method 2
```python
# Combine both open and saving steps to a variable in one line of code
# the with open() step helps to manage the closing of the file
with open("my_file.txt") as file:
  print(contents)
```

* `open()` also accepts another parameter called `mode`
  * Default `mode` parameter is set to "r" which is read only
  * "w" is for writing but this deletes/overrides everything in the text file
    *  If the file doesn't exist, running this code will help to create the file
  * "a" stands for append

```python
with open("my_file.txt", mode="a") as file:
  file.write("\nNew text inserted")
```

#### File Paths and Directories
* Relative File Path: working directory file path
* Absolute File Path: relative to the root, e.g. Mactintosh HD

* To look in the current folder: `./talk.ppt`
* To look for a file in the path file above the current path: `../report.doc`
* Each `../` goes up one level. If you want to go up 2 levels, it will be `../../Desktop/my_file.txt`
* For Mac OS, the path folder starts from `/Users/beatricekay/Desktop/file.txt`
* For Windows, each path is separated by the back slash instead \ but in code forward slash / works as well
