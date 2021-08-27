import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_PARAMS = {
    "lat": os.environ.get("MY_LAT"),
    "lon": os.environ.get("MY_LON"),
    "appid": os.environ.get("WEATHER_API_KEY"),
    "exclude": "current,minutely,daily"
}

def owm_tracker():
    res = (requests.get(f"{OWM_ENDPOINT}", params=OWM_PARAMS))
    res.raise_for_status()
    owm_data = res.json()
    rainy = False
    for hour in owm_data["hourly"]:
        if owm_data["hourly"].index(hour) in range(0,12):
            if hour["weather"][0]["id"] < 700:
                rainy = True
    if rainy == True:
        print("Bring an umbrella.")


owm_tracker()
