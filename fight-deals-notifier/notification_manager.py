from twilio.rest import Client
import smtplib

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_VIRTUAL_NUMBER = ""
TWILIO_VERIFIED_NUMBER = ""
GMAIL_EMAIL = ""
PASSWORD_GMAIL = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=GMAIL_EMAIL, password=PASSWORD_GMAIL)
            connection.sendmail(
                from_addr=GMAIL_EMAIL,
                to_addrs=GMAIL_EMAIL,
                msg=message.encode("utf-8")
            )

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
