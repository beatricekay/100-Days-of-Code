import requests
from datetime import datetime
import smtplib
import time

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

MY_LAT = 1.352083
MY_LONG = 103.819839
MY_EMAIL = "terryacorn2024@gmail.com"
MY_PASSWORD = "fkie wyba higc gqrs"

## Check position of ISS
def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status
    data = response_iss.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Allow for position to be within +5 or -5 degrees of the ISS position
    if abs(MY_LAT - iss_latitude) == 5 or abs(MY_LONG - iss_longitude) == 5:
        print(f"ISS is close to your position. It is currently at {iss_latitude}, {iss_longitude}.")
        return True
    else:
        print(f"ISS is not close to your position. It is currently at {iss_latitude}, {iss_longitude}.")
        return False

## Check if it is night time
def is_night():
    url = "https://api.sunrise-sunset.org/json"
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # time format
        "tzid": "Asia/Singapore" # timezone
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()

    # time is in this format 2024-06-08T06:56:48+08:00
    # we want to split the time at the "T" and take the hour, e.g. 06
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour
    
    if hour_now >= sunset or hour_now <= sunrise:
        print(f"It is currently night time. The time now is {hour_now}.")
        return True
    else:
        print(f"It is currently day time. The time now is {hour_now}.")
        return False

while True:
    time.sleep(60) # run the code every 60 seconds
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # secure the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg="Subject: Look Up\n\nThe ISS is above you in the sky. Look up!"
        )