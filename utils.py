import requests

API_KEY = '8e7264e53808149f2c50e6ffb77f5c1c'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def fetch_weather_data(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"  # Fetching in Celsius
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None


def process_weather_data(weather_data):
    # Extract relevant data
    location = weather_data['name']
    avg_temp = weather_data['main']['temp']
    max_temp = weather_data['main']['temp_max']
    min_temp = weather_data['main']['temp_min']
    condition = weather_data['weather'][0]['description']

    return {
        'location': location,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'condition': condition
    }
