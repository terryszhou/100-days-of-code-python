import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

my_email = "nathanielchang01@gmail.com"
password = os.environ.get("PASSWORD")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="terryszhou@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1993, month=12, day=22, hour=23, minute=30)
