import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

owm_params = {
    "lat": os.environ.get("MY_LAT"),
    "lon": os.environ.get("MY_LON"),
    "appid": os.environ.get("WEATHER_API_KEY"),
    "exclude": "current,minutely,daily"
}

res = (requests.get(f"{OWM_ENDPOINT}", params=owm_params))
res.raise_for_status()
owm_data = res.json()
print((owm_data))
