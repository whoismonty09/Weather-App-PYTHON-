import requests

api_key = "40ba04189209257f3dbd521a1d9012d2"
base_url = "https://api.openweathermap.org/data/2.5/weather"

print("Weather Application developed by Monty")
city = input("Enter city name: ")

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(base_url, params=params)

data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
    print("Wind Speed:", wind, "m/s")

else:
    print("City not found!")
