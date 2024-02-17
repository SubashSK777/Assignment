import requests

def get_weather(city):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=Metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()
        desc = weather['weather'][0]['main']
        temp = round(weather['main']['temp'])
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        print("\n")
        print(f"--------The weather in '{city}' is--------------")
        print(f"Weather: {desc}")
        print(f"Temperature: {temp}ºC")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed}km/h")

api_key = 'cb0fe32b4004b702eb49ba7111ccb9b5'

while True:
    print("\nChoose an option:")
    print("1. Get weather forecast")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        city = input("Enter city: ")
        if not city:
            print("Error: City name must be filled out.")
        else:
            get_weather(city)
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose again.")