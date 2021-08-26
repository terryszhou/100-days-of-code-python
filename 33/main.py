import requests
from datetime import datetime

MY_LAT = 30.319920
MY_LNG = -97.655210

def iss_tracker():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    print(longitude, latitude)

# iss_tracker()

def sunrise_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now()
    print(sunrise)
    print(sunset)
    print(time_now.hour)

sunrise_sunset()