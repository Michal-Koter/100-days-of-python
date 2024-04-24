import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypass"
MY_LAT = 54.352024
MY_LONG = 18.646639

def is_iss_overhad():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return -5 <= iss_latitude - MY_LAT <= 5 and -5 <= iss_longitude - MY_LONG <= 5

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return sunset <= time_now or time_now <= sunrise

while True:
    if is_iss_overhad() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
    time.sleep(600)
