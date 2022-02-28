import os
from twilio.rest import Client

def sms_all(scraper):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    scraper = str(scraper)
    message = client.messages \
                    .create(
                    body= scraper,
                    from_='+16467989631',
                    to= ['+18475323886','+12242411079'],
                        )
        
    print(message.sid)