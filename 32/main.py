import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

my_email = "nathanielchang01@gmail.com"
password = os.environ.get("PASSWORD")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="terryszhou@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
