import requests
city =input("Enter the city: ")
url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()
    current= data["current_condition"][0]
    temp = current["temp_C"]
    humidity = current["humidity"]
    desc = current["weatherDesc"][0]["value"]

    print(city ," city\n"
          ,"temp :" ,temp,"C\n"
          "humidity :", humidity ,"%\n"
          "desc :", desc)
    
except requests.exceptions.RequestException:
    print("Network error")
except KeyError:
    print("City not found")
except Exception as e:
    print("Error: " ,e)