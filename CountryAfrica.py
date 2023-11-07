import requests

url = 'https://restcountries.com/v3.1/region/africa'

response = requests.get(url)

if response.status_code == 200:
    # Parse the response as JSON
    countries_data = response.json()  # This returns a list of countries in Africa

    # Create a list to hold the names of all countries
    country_names = [country['name']['common'] for country in countries_data]

    print(f"Countries in Africa: {', '.join(country_names)}")
else:
    print(f"Error: {response.status_code}")
