import requests
import json
import time
from datetime import datetime

# Add your OpenWeatherMap API key here
API_KEY = "6912921bb1ac6aef4a257a2225866410"

# List of cities for which to fetch weather data
cities = ["Delhi", "Mumbai", "Chennai", "Bengaluru", "Kolkata", "Hyderabad"]

# Temperature threshold for alerts
temp_threshold = float(input("Enter temperature threshold for alerts (in °C, default 35°C): ") or 35)

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API for a given city."""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        print(f"Fetching data for {city}: {response.status_code}")
        if response.status_code == 200:
            print(f"Response data for {city}: {response.json()}")
            return response.json()
        else:
            print(f"Failed to fetch data for {city}. Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception occurred while fetching data for {city}: {e}")
        return None

def process_weather_data(weather_data):
    """Process and print weather data."""
    if not weather_data:
        return "No data available."

    try:
        city_name = weather_data['name']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        weather_desc = weather_data['weather'][0]['main']
        weather_report = (f"Weather Report for {city_name} at {datetime.now()}:\n"
                          f"  - Temperature: {temp}°C\n"
                          f"  - Feels Like: {feels_like}°C\n"
                          f"  - Weather: {weather_desc}")
        if temp >= temp_threshold:
            weather_report += f"\n  [Alert] Temperature exceeds {temp_threshold}°C!"
        print(weather_report)
        return weather_report
    except KeyError as e:
        print(f"KeyError: Missing key in weather data: {e}")
        return "Invalid data."

def monitor_weather():
    """Monitor weather and log data periodically."""
    all_weather_data = {}
    while True:
        daily_summaries = {}
        for city in cities:
            weather_data = fetch_weather_data(city)
            report = process_weather_data(weather_data)
            all_weather_data[city] = weather_data if weather_data else {}
            
            if weather_data:
                temp = weather_data['main']['temp']
                daily_summaries[city] = {
                    "Average Temperature": temp,
                    "Max Temperature": weather_data['main'].get('temp_max', temp),
                    "Min Temperature": weather_data['main'].get('temp_min', temp),
                    "Dominant Weather Condition": weather_data['weather'][0]['main']
                }
            else:
                daily_summaries[city] = "No data available."

        # Print daily summaries
        for city, summary in daily_summaries.items():
            if isinstance(summary, dict):
                print(f"\nDaily Weather Summary for {city}:")
                print(f"  - Average Temperature: {summary['Average Temperature']}°C")
                print(f"  - Max Temperature: {summary['Max Temperature']}°C")
                print(f"  - Min Temperature: {summary['Min Temperature']}°C")
                print(f"  - Dominant Weather Condition: {summary['Dominant Weather Condition']}")
            else:
                print(f"No data available for {city}.")

        # Save data to a JSON file
        with open('weather_data.json', 'w') as f:
            json.dump(all_weather_data, f, indent=4)
        print("Weather data saved to weather_data.json")

        # Wait for 5 minutes before fetching data again
        print("Waiting for 5 minutes before the next update...")
        time.sleep(5 * 60)

if __name__ == "__main__":
    monitor_weather()
