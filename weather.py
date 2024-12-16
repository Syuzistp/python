# import requests
# import sys

# # Function to fetch weather data for a city
# def get_weather_data(city_name, api_key):
#     # OpenWeatherMap API URL
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

#     # Sending the GET request to OpenWeatherMap
#     response = requests.get(url)
    
#     # Checking if the request was successful
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching data: {response.status_code}")
#         sys.exit(1)

# # Function to display weather information
# def display_weather_info(weather_data, option=None):
#     # Extracting relevant weather data
#     main_data = weather_data['main']
#     weather_description = weather_data['weather'][0]['description']
    
#     # Displaying weather data based on user input or showing all available data
#     print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
#     if option == "temperature":
#         print(f"Temperature: {main_data['temp']}°C")
#     elif option == "humidity":
#         print(f"Humidity: {main_data['humidity']}%")
#     elif option == "pressure":
#         print(f"Pressure: {main_data['pressure']} hPa")
#     elif option == "weather":
#         print(f"Weather: {weather_description.capitalize()}")
#     else:
#         print(f"Temperature: {main_data['temp']}°C")
#         print(f"Humidity: {main_data['humidity']}%")
#         print(f"Pressure: {main_data['pressure']} hPa")
#         print(f"Weather: {weather_description.capitalize()}")

# # Function to show available options
# def show_available_options():
#     print("Available weather options:")
#     print("1. temperature")
#     print("2. humidity")
#     print("3. pressure")
#     print("4. weather description")

# # Main function to drive the program
# def main():
#     # Check if the user has entered the city name
#     if len(sys.argv) < 2:
#         print("Please provide a city name as a required argument.")
#         sys.exit(1)

#     city_name = sys.argv[1]  # Get the city name from the command line arguments

#     # Optionally, get the second argument for specific data (temperature, humidity, etc.)
#     option = None
#     if len(sys.argv) == 3:
#         option = sys.argv[2].lower()
    
#     # Show available options
#     show_available_options()

#     # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
#     api_key = 'your_api_key_here'

#     # Fetch the weather data
#     weather_data = get_weather_data(city_name, api_key)
    
#     # Display the weather data based on the user's option
#     display_weather_info(weather_data, option)

# main()
