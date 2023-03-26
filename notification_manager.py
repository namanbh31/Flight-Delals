from twilio.rest import Client

TWILIO_SID = "add your sid"
TWILIO_AUTH_TOKEN = "add your auth token"
TWILIO_VIRTUAL_NUMBER = 'add your twillio number'
TWILIO_VERIFIED_NUMBER = 'number to senf messeges'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
