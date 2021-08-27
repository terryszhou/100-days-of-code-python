import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

API_KEY = os.environ.get("WEATHER_API_KEY")
CITY_NAME = "Austin"

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}")
print(res.json())