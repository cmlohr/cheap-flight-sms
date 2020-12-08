from twilio.rest import Client
import smtplib
# TWILIO
SID = "_TWILIO_SID_"
TWILIO_AUTH = "_TWILIO_AUTH_"
TWILIO_PHONE = "_TWILIO_VIRTUAL_PHONE_"
TWILIO_VERIFIED_PHONE = "_VERIFIED_PHONE_"
# EMAIL
GMAIL = "smtp.gmail.com"
PORT = 587 # may not be required
SEND_EMAIL = "_YOUR_SENDING_EMAIL_"
PASSWORD = "_PASSWORD_FOR_SENDING_EMAIL_



class NotificationManager:

    def __init__(self):
        self.client = Client(SID, TWILIO_AUTH)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=TWILIO_VERIFIED_PHONE,
        )
        print(message.sid)

    def send_email(self, user_emails, message, google_link):
        with smtplib.SMTP(GMAIL, port=PORT) as connect:
            connect.starttls()
            connect.login(SEND_EMAIL, PASSWORD)
            for email in user_emails:
                connect.sendmail(
                    from_addr=SEND_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:NEW LOW FLIGHT PRICE!\n\n{message}\n{google_link}".encode('utf-8')
                )