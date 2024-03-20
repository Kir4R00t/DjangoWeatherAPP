import os
from dotenv import load_dotenv
import requests


def get_weather_data(city_name):
    load_dotenv('.env')
    API_KEY = os.getenv('TOKEN')
    URL = "https://api.openweathermap.org/data/2.5/weather?"
    request_url = URL + f"q={city_name}&units=metric&appid={API_KEY}"

    print("Request URL:", request_url)  # debugging
    response = requests.get(request_url)

    print("Response Status Code:", response.status_code)  # debugging

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        # Check if 'wind' data is available in the response
        if 'wind' in data:
            wind_speed = data['wind']['speed']
        else:
            wind_speed = None

        return {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
        }
    else:
        return None
