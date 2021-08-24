import os
import smtplib
import datetime as dt
from random import choice
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_EMAIL = "nathanielchang01@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

NOW = dt.datetime.now()
WEEKDAY = NOW.weekday()

def send_quote():
    if WEEKDAY == 1:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="terryszhou@gmail.com",
                msg=f"Subject: Tuesday Motivational Quote\n\n{quote}"
            )

send_quote()
