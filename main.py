import requests

API_KEY = "42a90dc3d87d1574334f3e90b05d8c4d"

cities = ["Pecos,US", "Las Vegas,NM,US"]
url = f"https://api.openweathermap.org/data/2.5/weather?q=Las Vegas,NM,US&appid={API_KEY}&units=imperial"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", response.json())

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error fetching data for {city}")
            return None

        weather_main = data["weather"][0]["main"]
        temp = data["main"]["temp"]

        return weather_main, temp

    except Exception as e:
        print(f"Exception occurred: {e}")
        return None


def traffic_light_logic(weather, temp):
    """
    Green = clear/good weather
    Yellow = moderate (clouds, mild rain)
    Red = severe (storm, extreme temp)
    """

    if weather in ["Clear"] and 60 <= temp <= 85:
        return "🟢 GREEN - Great weather!"

    elif weather in ["Clouds", "Drizzle"] or (40 <= temp < 60 or 85 < temp <= 95):
        return "🟡 YELLOW - Be cautious."

    elif weather in ["Rain", "Thunderstorm", "Snow"] or temp < 40 or temp > 95:
        return "🔴 RED - Bad weather conditions!"

    else:
        return "🟡 YELLOW - Uncertain conditions."


def main():
    for city in cities:
        result = get_weather(city)

        if result:
            weather, temp = result
            status = traffic_light_logic(weather, temp)

            print(f"\nCity: {city}")
            print(f"Weather: {weather}")
            print(f"Temperature: {temp}°F")
            print(f"Status: {status}")


if __name__ == "__main__":
    main()
