import requests
import json
while True:
    try:
        user = input("Username(press e to exit) : ")
        url =  f"https://api.github.com/users/{user}"
        res= requests.get(url)
        data=res.json()
        print ("User: " ,data["login"])
        print ("Repos: " ,data["public_repos"])
        print ("Followers" .data["followers"])
        if user=="e":
            break
    except requests.exceptions.RequestException:
        print("Network error")
    except KeyError:
        print("User not found")
    except Exception as e :
        print("Error: ",e)
    