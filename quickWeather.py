#! python
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys,pprint

# Compute location from command line argument.
if len(sys.argv) < 2:
    print ('Usage: quickWeather.py location')
    sys.exit()
location = ','.join(sys.argv[1:])
# Download the json data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=0e5bedf3f10cad5f44a339ded8ebc9aa' %(location)
proxies={
'http': 'http://127.0.0.1:7890',
'https': 'http://127.0.0.1:7890'} # https -> http
response = requests.get(url,proxies)
response.raise_for_status()
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.

print('Current weather in %s:' %(location))
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])
