import requests
from twilio.rest import Client

STOCK = ""
COMPANY_NAME = ""
API_KEY_ALPHA = ""
ALPHA_ENDPOINT = "https://www.alphavantage.co/query?"
API_KEY_NEWS = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_NUM = ""
MY_NUM = ""


def get_news():
    endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": COMPANY_NAME,

    }

    response = requests.get(url=endpoint, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    three_articles = data["articles"][:3]

    list_of_articles = [f"{STOCK}: {up_down} {percentage_difference}%\nHeadline: {article['title']}\nBrief:"
                        f"{article['description']}" for article in three_articles]

    return list_of_articles


def send_sms(list_of_articles):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in list_of_articles:
        message_text = article

        message = client.messages \
            .create(
            body=message_text,
            from_=TWILIO_NUM,
            to=MY_NUM
        )

        print(message.status)


alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_ALPHA,
}

response = requests.get(url=ALPHA_ENDPOINT, params=alpha_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterdays_close = float(data_list[0]["4. close"])
previous_day_close = float(data_list[1]["4. close"])

percentage_difference = round(((yesterdays_close - previous_day_close) / previous_day_close) * 100, 2)

up_down = None

if percentage_difference > 0:
    up_down = "😘"
else:
    up_down = "😰"

print(percentage_difference)

if abs(percentage_difference) > 5:
    send_sms(get_news())


