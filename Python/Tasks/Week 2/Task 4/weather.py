import requests

url = "https://api.openweathermap.org/geo/1.0/direct?q=Jaipur&limit=5&appid=411ee0a03513118dea40797c022da439"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    lat = data[0]["lat"]
    lon = data[0]["lon"]

url1 = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=411ee0a03513118dea40797c022da439")

response1 = requests.get(url1)

if response1.status_code == 200:
    data1 = response1.json()
    print(f"Detail - {data1["weather"][0]["main"]}")
    print(f"Description - {data1["weather"][0]["description"]}")
    celsius = data1["main"]["temp"]-273.15
    print(f"Temperature {celsius}")

