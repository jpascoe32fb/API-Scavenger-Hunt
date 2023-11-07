import requests

url = 'https://restcountries.com/v3.1/name/brazil'

response = requests.get(url)

# If the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    brazil_data = response.json()[0]

    # Extract population, area, and official language information
    population = brazil_data['population']
    area = brazil_data['area']
    languages = brazil_data['languages'].values()

    print(f"Country: Brazil")
    print(f"Population: {population}")
    print(f"Area: {area} sq. km")
    print(f"Official Languages: {', '.join(languages)}")
else:
    print(f"Error: {response.status_code}")
