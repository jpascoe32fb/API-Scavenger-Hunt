import requests
from datetime import datetime

api_key = ''

city_name = "Tokyo"

url = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'  
}

response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response to JSON
    forecast_data = response.json()
    
    # Loop through the forecast data
    print(f"5 Day Weather Forecast for {city_name} at 3-hour intervals:\n")
    for forecast in forecast_data['list']:
        # Convert the timestamp to a datetime object
        timestamp = forecast['dt']
        forecast_time = datetime.fromtimestamp(timestamp)

        # Extract the desired information
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        humidity = forecast['main']['humidity']
        wind_speed = forecast['wind']['speed']

        # Print the forecast data
        print(f"{forecast_time} => Temperature: {temp}°C, Weather: {description}, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
else:
    print("Error:", response.status_code, response.text)
