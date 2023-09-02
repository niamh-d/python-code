import requests
from datetime import datetime
import smtplib
import time

MY_LAT = ""
MY_LONG = ""
UTC_LOCAL_OFFSET = ""

MY_EMAIL_GMAIL = ""
MY_PASSWORD_EMAIL = ""
RECIPIENT = ""


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_utc_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_utc_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    sunrise_local_hour = sunrise_utc_hour + UTC_LOCAL_OFFSET
    sunset_local_hour = sunset_utc_hour + UTC_LOCAL_OFFSET

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now >= sunset_local_hour or hour_now <= sunrise_local_hour:
        return True


def email_sender():

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL_GMAIL, password=MY_PASSWORD_EMAIL)
        connection.sendmail(
            from_addr=MY_EMAIL_GMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject: Look up!\n\nThe ISS is overhead! Happy viewing!"
        )


while True:

    time.sleep(60)

    if is_iss_overhead() and is_dark():

        email_sender()
