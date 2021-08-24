##################### Extra Hard Starting Project ######################
import os
import smtplib
import pandas
import datetime as dt
from random import choice
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_EMAIL = "nathanielchang01@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

NOW = dt.datetime.now()
MONTH = NOW.month
DAY = NOW.day

birthday_data = pandas.read_csv("birthdays.csv")
birthday_list = birthday_data.to_dict(orient="records")

def birthday_mailer():
    for person in birthday_list:
        if person["month"] == MONTH and person["day"] == DAY:
            with open(choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"])) as letter:
                contents = letter.read()
                new_contents = contents.replace("[NAME]", person["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=person["email"],
                    msg=f"Subject: Happy Birthday {person['name']}!\n\n{new_contents}"
                )

birthday_mailer()