##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random as rd
import smtplib

MY_EMAIL = "terryacorn2024@gmail.com"
MY_PASSWORD = "fkie wyba higc gqrs"

### Step 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes

### Step 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# read birthdays.csv
data = pd.read_csv("birthdays.csv")

# create a dictionary using dictionary comprehension
# birthdays_dict = {(birthday_month, birthday_day): data_row}
# birthdays_dict = {(12, 24): Angela,angela@email.com,1995,12,24}
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

### Step 3. If there is a match, pick a random letter from letter templates.
# compare and see if today's month/day tuple matches one of the keys in birthday_dict
if today_tuple in birthdays_dict: # check if tuple matches dictionary key tuple
    birthday_person = birthdays_dict[today_tuple]
    
    # if there is a match, pick a random letter
    random_number = rd.randint(1,3)
    file_path = f"letter_templates/letter_{random_number}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

### Step 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # secure the connection
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=birthday_person["email"], 
        msg=f"Subject:Happy Birthday\n\n{contents}"
    )