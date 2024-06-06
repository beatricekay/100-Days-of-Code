import smtplib
import datetime as dt
import random as rd

MY_EMAIL = "terryacorn2024@gmail.com"
MY_PASSWORD = "fkie wyba higc gqrs"
    
now = dt.datetime.now()
weekday = now.weekday()

path = "/Users/beatricekay/Downloads/Birthday Wisher (Day 32) start/quotes.txt"

if weekday == 3: # index 0 starts from Monday
    # pick random quote from list of quotes
    with open(path) as quote_file:
        all_quotes = quote_file.readlines() # returns a list of all quotes
        quote = rd.choice(all_quotes)
    
    print(quote)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # secure the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )