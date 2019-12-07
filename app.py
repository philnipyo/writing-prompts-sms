import os
from twilio.rest import Client

# Get values from environment variables to use
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
personal_num = os.environ.get('PERSONAL_NUM')
twilio_num = os.environ.get('TWILIO_NUM')

client = Client(account_sid, auth_token)

# Creates and sends a text message; include mediaurl field to send things like images and gifs
client.messages.create(
                     from_=twilio_num,
                     to=personal_num,
                     body="This is a test!",
                 )