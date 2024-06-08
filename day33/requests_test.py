import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# This will raise an exception if the response was not successful
# We do not need to manually define all the different exceptions for each status code
response.raise_for_status() 

print(response.status_code)
print(response.text)