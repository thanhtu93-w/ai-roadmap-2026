import requests
import json

url =  "https://api.github.com/users/thanhtu93-w"
response = requests.get(url)
data = response.json()
status=response.status_code
print(status)
if status==200:
    print("Successfully")
    print(data)
elif status==404:
    print("Can not find")
elif status==401:
    print("Unauthorized")
else:
    print("Error")
