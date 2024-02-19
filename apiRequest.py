import requests

def apiRequest():

    API_KEY = "a41271a97939d058f9d80607b05b55a8"
    apiResponse = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=" + API_KEY


    response = requests.get(apiResponse).json()
    print(response)  # Print the response for inspection

    return response
