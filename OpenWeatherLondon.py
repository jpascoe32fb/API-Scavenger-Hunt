import requests

api_key = ''

city_name = "London,UK"

url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': city_name,
    'appid': api_key,
    'units': 'imperial'  
}

response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response to JSON
    data = response.json()
    
    # Extract the desired information
    temp = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Display the output
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Weather Condition: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error:", response.status_code, response.text)
