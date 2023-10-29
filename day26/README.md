# Day 26: List Comprehension and the Nato Alphabet
## Concepts
* How to Create Lists using List Comprehension
* How to use Dictionary Comprehension
* How to Iterate over a Pandas DataFrame
  
## Learning Points
### List Comprehension
* Help to reduce the number of lines in code by creating the new list directly in the list itself. This concept can be applied to strings as well.
  * ``` python
    new_list = [new_item for item in list]```
 
### Conditional List Comprehension:
* ``` python
  new_list = [new_item for item in list if test]```

### Dictionary Comprehension
* Create a new dictionary based on values in a list:
  * ``` python
    new_dict = {new_key:new_value for item in list if test}```
* Create a new dictionary based on a values in a dictionary:
  * ```python
    new_dict = {new_key:new_value for (key, value) in dict.items() if test}```
 
### Looping through a Pandas DataFrame
* Method 1: 
``` python
for (key, value) in dataframe.items()
    print(key) # this prints out the name of the columns
    print(value) # this prints out the data in each of the columns
```
* Method 2:
``` python
for (index, row) in dataframe.iterrows():
  if row.column == 'Value': # condition to filter rows
      print(index) # this prints out the index of all the rows
      print(row) # this prints out each of the rows, where each row is a Panda Series object
      print(row.column) # this prints out the entire column referenced
```
