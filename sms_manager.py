from twilio.rest import Client

SID = "_TWILIO_SID_"
TWILIO_AUTH = "_TWILIO_AUTH_"
TWILIO_PHONE = "_TWILIO_VIRTUAL_PHONE_"
TWILIO_VERIFIED_PHONE = "_VERIFIED_PHONE_"

# Twilio MSG
# def blah_blah_blah():



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