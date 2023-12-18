# Day 30 - Errors, Exceptions and JSON Data: Improving the Password Manager
## Concepts Practised
* Catching Exceptions: The try catch except finally Pattern
* Raising Exceptions
* IndexError Handling
* KeyError Handling
* Write, read and update JSON data in the Password Manager

## Learning Points
### Exception Handling
* Common errors are:
  * `KeyError`: key does not exist in dictionary
  * `IndexError`: list index out of range
  * `TypeError`: incorrect data type
*
  ```python
  try: # code that that might cause an exception
  except: # code to run when exception occurs
  else: # code to run if there were no exceptions. this will only run if the code in the try block succeeds
  finally: # code to run no matter what happens
  ```
* Good practice is not to have a bare ```except``` and to specify the exception you want to catch
* 
  ```python
  try:
      file = open("a_file.txt")
      a_dictionary = {"key":"value"}
  
  except FileNotFoundError:
      file = open("a_file.txt", "w")
      file.write("Something")
  
  except KeyError as error_message: # save error message
      print(f"The key {error_message} does not exist.")

  else: # the code here is only run if the try block is successful
      content = file.read()
      print(content)

  finally:
      file.close()
      print("File was closed.")
  ```
*
  ```python
  try:
      count = count + 1
  except KeyError:
      pass
  ```
* You can also raise your own exceptions:
  ```python
  raise ValueError("This should not happen.")
  ```
* https://www.programiz.com/python-programming/exception-handling
  
### JSON Data
* JSON files are converted to dictionaries in Python
* **Write:** ```json.dump(new_date, file, indent=4)```
  * ```indent``` will unflatten the ```json``` and make it more readable
* **Read:** ```json.load()```
  * ```python
    data = json.load(data_file)
    print(data)
    ```
* **Update:** ```json.update()```
  * ```python
    with open("data.json", "r") as data_file:
         # Reading old data
         data = json.load(data_file)
         # Update old data with new data
         data.update(new_data)
    
    with open("data.json", "w") as data_file:
         # Saving updated data
         json.dump(data, data_file, indent=4)
    ```
