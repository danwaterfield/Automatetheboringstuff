#! python3
# quickweather.py - Prints the weather for a location from the command line.

import json, requests, sys

# figures out location from the command line inputs

if len(sys.argv) < 2:
	print('usage: quickweather.py location')
	sys.exit()

location = ' '.join(sys.argv[1:])

# to do download the json data from openweathermap's API

# load jason data into a python variable.