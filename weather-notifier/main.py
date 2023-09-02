import requests
from twilio.rest import Client

API_KEY = ""
MY_LAT = ""
MY_LONG = ""
CITY = ""
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_NUM = ""
MY_NUM = ""

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(hour_data["weather"])
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
        .create(
        body=f"It will rain today! Don't forget to bring an umbrella with you!",
        from_=TWILIO_NUM,
        to=MY_NUM
    )

    print(message.status)
else:
    print(f"It won't rain today in {CITY}. You're safe.")



