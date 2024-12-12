from dataclasses import asdict
from random import random

import requests, json, geopy

from db_connection import cursor
API_KEY = "6459ac502e2f09a73b6900f8878b340f"


paikkakunnan_nimi = input("Paikkakunnan nimi: ")

sql = f"SELECT latitude_deg, longitude_deg from airport where municipality = '{paikkakunnan_nimi}' limit 1"
cursor.execute(sql)
try:
    result =  cursor.fetchall()[0]
except Exception as e:
    print(e)
    quit()
URL = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunnan_nimi}&units=metric&appid={API_KEY}"
test = requests.get(url=URL).json()
main = test["main"]
print(f"Säätila: {test['weather'][0]['description']} \nLämpötila: {main['temp']}")
