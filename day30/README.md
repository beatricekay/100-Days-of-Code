# Day 30 - Errors, Exceptions and JSON Data: Improving the Password Manager
## Concepts Practised
* Catching Exceptions: The try catch except finally Pattern
* Raising Exceptions
* IndexError Handling
* KeyError Handling
* Write, read and update JSON data in the Password Manager

## Learning Points
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
* https://www.programiz.com/python-programming/exception-handling
