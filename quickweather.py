#! python3
# quickweather.py - Prints the weather for a location from the command line.

import json, requests, sys, bs4

# figures out location from the command line inputs

if len(sys.argv) < 2:
	print('usage: quickweather.py location')
	sys.exit()

location = ' '.join(sys.argv[1:])

# downloads JSON data from openweather's API. Workaround due to the site requiring an API key. Currently waiting for the site to auth my key...

APPID = ''

url = 'api.openweathermap.org/data/2.5/weather?q=%s'+ location + '&APPID=' + APPID
response = requests.get(url)
response.raise_for_status()

# load jason data into a python variable.
weatherData = json.loads(response.text)

pprint.pprint(weatherData)

# prints weather data

w = weatherData['list']
print('Current weather in %s is: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

