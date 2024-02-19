from apiRequest import apiRequest


def main():
    response = apiRequest()
    print_weather_data(response)
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def print_weather_data(response):
    # Extracting specific data from the response
    temperature_kelvin = response['main']['temp']
    weather_description = response['weather'][0]['description']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = kelvin_to_celsius(temperature_kelvin)

    print(f"The temperature in Zurich is {temperature_celsius:.2f} degrees Celsius.")
    print(f"Current weather description: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")

