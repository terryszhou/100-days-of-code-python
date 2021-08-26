import requests
import datetime as dt
import os
import smtplib
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_EMAIL = "nathanielchang01@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

MY_LAT = 30.319920
MY_LNG = -97.655210

def iss_tracker():
    response = requests.get("http://api.open-notify.org/iss-now.json")
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

# sunrise_sunset()

def iss_notifier():
    sun_params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    iss_res = requests.get("http://api.open-notify.org/iss-now.json")
    sun_res = requests.get("https://api.sunrise-sunset.org/json", params=sun_params)

    iss_lat = iss_res.json()["iss_position"]["latitude"]
    iss_lng = iss_res.json()["iss_position"]["longitude"]

    sunrise = sun_res.json()["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = sun_res.json()["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = dt.datetime.now()
    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LNG - 5 < iss_lng < MY_LNG + 5:
        if time_now.hour > sunset:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="terryszhou@gmail.com",
                    msg=f"Subject: The ISS is nearby!\n\nISS is currently at {(iss_lat, iss_lng)}."
                )

iss_notifier()
