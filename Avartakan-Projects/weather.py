import requests

def fetch_weather_data(city, api_key):
    """Fetch weather data for the given city from OpenWeatherMap API."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return None

def process_weather_response(response, city):
    """Process the API response and display weather information."""
    if response and response.status_code == 200:
        try:
            data = response.json()
            if 'main' not in data or 'weather' not in data:
                print("Error: Weather data is missing from the response.")
                return None

            temperature = data['main'].get('temp', 'N/A')
            feels_like = data['main'].get('feels_like', 'N/A')
            humidity = data['main'].get('humidity', 'N/A')
            weather_description = data['weather'][0].get('description', 'N/A').capitalize()

            print(f"Weather in {city}:")
            print(f"  Temperature: {temperature}°C")
            print(f"  Feels like: {feels_like}°C")
            print(f"  Humidity: {humidity}%")
            print(f"  Description: {weather_description}")

            return {
                "temperature": temperature,
                "feels_like": feels_like,
                "humidity": humidity,
                "description": weather_description
            }
        except (KeyError, ValueError) as parse_err:
            print(f"Error parsing the response: {parse_err}")
            return None
    elif response and response.status_code == 404:
        print(f"Error: City '{city}' not found. Please check the city name and try again.")
        return None
    elif response and response.status_code == 401:
        print("Error: Invalid API key. Please check your API key and try again.")
        return None
    else:
        print("Failed to retrieve weather data. Please try again.")
        return None

def main():
    """Main function to get user input and fetch weather information."""
    api_key = 'b10e2b972de04df00fab932ba98bcb11'
    city = input("Enter the name of city: ")
    if not city.strip():
        print("Error: City name cannot be empty.")
        return

    response = fetch_weather_data(city, api_key)
    process_weather_response(response, city)

if __name__ == "__main__":
    main()

