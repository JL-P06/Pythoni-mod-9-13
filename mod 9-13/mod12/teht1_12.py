import requests
import json


REQUEST_URL = "https://api.chucknorris.io/jokes/random"

vitsi = requests.get(REQUEST_URL).json()

print(vitsi["value"])