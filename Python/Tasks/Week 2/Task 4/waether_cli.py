import requests
from datetime import datetime

city = input("Enter the city:").strip()

api_key = "9a82fb08366f3de8b40198e137f35135"

url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    now = datetime.now().strftime("%H:%M:%S")
    weatherInfo = data["weather"][0]["main"]
    print(f"Current Weather Details at time {now}") 
    print(f"Current Weather : {weatherInfo}")
    weatherDesc = data["weather"][0]["description"]
    print(f"Description : {weatherDesc}")
    tempInCelsius = (data["main"]["temp"] - 273.15)
    print(f"Temperature : {round(tempInCelsius,2)}")

else:
    print(f"Failed to retreive data. Error {response.status_code}")

