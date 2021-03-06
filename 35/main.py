import os
from dotenv import load_dotenv, find_dotenv
import requests
from twilio.rest import Client

load_dotenv(find_dotenv())

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_PARAMS = {
    "lat": os.environ.get("MY_LAT"),
    "lon": os.environ.get("MY_LON"),
    "appid": os.environ.get("WEATHER_API_KEY"),
    "exclude": "current,minutely,daily"
}
ACCT_SID = os.environ.get("TWILIO_ACCT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_ACCT_TOKEN")
PHONE_NUM = "+15406251609"

def owm_tracker():
    res = (requests.get(f"{OWM_ENDPOINT}", params=OWM_PARAMS))
    res.raise_for_status()
    rainy = False
    for hour in res.json()["hourly"][:12]:
        if hour["weather"][0]["id"] < 700:
            rainy = True
    if rainy:
        client = Client(ACCT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an ⛱!",
                from_=PHONE_NUM,
                to='+19253843787'
            )
        print(message.status)

owm_tracker()
