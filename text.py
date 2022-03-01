import os
from twilio.rest import Client

def sms_all(scraper):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    scraper = str(scraper)
    numbers = ('8475323886','2242411079')
    for i in numbers:
        send = i
        message = client.messages \
                        .create(
                        body= scraper,
                        from_='+16467989631',
                        to= '+1'+ send,
                            )
            
        print(message.sid)