# Day 32 - Send Email (smtplib) & Manage Dates (datetime)
## Concepts Practised
* How to Send Emails with Python using SMTP
* Working with the `datetime` Module

## Learning Points
### Simple Mail Transfer Process (SMTP)
* To connect to a Gmail server, a connection has to be created.
* To ensure the connection is secure, we can use Transport Layer Security (TSL) to encrypt the email.
* An App Password can be used in place of the actual password for an extra layer of protection. 2-Step Verification has to be enabled first.

```python
my_email = "enter sender email here"
password = "enter app password here"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="enter sendee email here", 
    msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()
```
<img width="610" alt="image" src="https://github.com/beatricekay/100-Days-of-Code/assets/59497250/2da81e52-161b-4028-b607-0dbd3e5a29e5">

### Running Python Code in the Cloud
* We can host our code on https://www.pythonanywhere.com/
    * Upload all relevant files
    * Create a new Bash console
    * In the console, write `python3 main.py` to run the Python file
    * If Google attempts to block the connection, click on the support link to enable the connection
    * If the script successfully runs without any errors, the $ sign will reappear again
      <img width="778" alt="image" src="https://github.com/beatricekay/100-Days-of-Code/assets/59497250/1b73596b-363f-4292-bceb-769f5100ab79">
    * We can also schedule the task to run daily
      <img width="973" alt="image" src="https://github.com/beatricekay/100-Days-of-Code/assets/59497250/c882b865-499c-483a-a88a-fefa9b0f48dd">
      <img width="967" alt="image" src="https://github.com/beatricekay/100-Days-of-Code/assets/59497250/3c751866-788b-4c64-92aa-96573529ef44">
