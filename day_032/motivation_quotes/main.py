import smtplib
import datetime
import random

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypass"

now = datetime.datetime.now()
if now.weekday() != 1:
    exit()

with open("quotes.txt", "r") as file:
    quotes = file.read().splitlines()

today_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com", port=25) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Motivation quote\n\n{today_quote}"
                        )