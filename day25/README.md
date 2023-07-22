# Day 25: Working with CSV Data and the Pandas Library
## Concepts
* Reading CSV Data in Python
* DataFrames & Series
* Working with Rows & Columns
* Data Analysis with Pandas
  
## Learning Points
* To read CSV data without the `pandas` library, we can use the `csv` library:
  ```
  import csv

  with open("weather_data.csv") as data_file:
      data = csv.reader(data_file)
      temperatures = []
      for row in data:
          if row[1] != "temp":
              temperature = int(row[1])
              temperatures.append(temperature)
          
  print(temperatures)
  ```
* `pandas` library is more convenient to read CSV files
  * `to_dict()`: converts a DataFrame to a dictionary
  * `to_list()`: converts a Series (single DataFrame column) to a list
  * DataFrame(): converts a dictionary to a DataFrame
 
* Reference a column: `df["column"]` or `df.column`
* Reference a row: `df[df["column"] == condition]`
