import os, praw, random
from twilio.rest import Client

# ============================================================
# This is section is for the API and tool usage initialization


# Get values from environment variables to use
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
personal_num = os.environ.get('PERSONAL_NUM')
twilio_num = os.environ.get('TWILIO_NUM')
reddit_user = os.environ.get('REDDIT_USER')
reddit_pass = os.environ.get('REDDIT_PASSWORD')
sms_reddit_client_id = os.environ.get('SMS_REDDIT_CLIENT_ID')
sms_reddit_client_secret = os.environ.get('SMS_REDDIT_CLIENT_SECRET')


# Reddit client
reddit = praw.Reddit(client_id=sms_reddit_client_id,
                     client_secret=sms_reddit_client_secret,
                     password=reddit_pass,
                     user_agent='writing-prompt-sms by /u/{}'.format(reddit_user),
                     username=reddit_user)


# Twilio client
client = Client(account_sid, auth_token)


# End initialization section
# ============================================================


# Select the WritingPrompts subreddit
wp = reddit.subreddit('WritingPrompts')


# One-liner where the titles of the top 10 posts are added into a dictionary and if they are not stickied posts
# For r/WritingPrompts, there are 2 stickied posts by default so 12 is used to account for that
prompts = [prompt.title for prompt in wp.hot(limit=12) if not prompt.stickied]


# Randomly generate a number to retrieve the corresponding title from the prompts list
randomTitleNumber = random.randint(0, 9)


# Creates and sends a text message containg the writing prompt via Twilio client.
try:
    client.messages.create(
                     from_=twilio_num,
                     to=personal_num,
                     body="{}".format(prompts[randomTitleNumber]),
                 )
# Acknowledge that the prompt was successfully sent by pressing any key to exit.
finally:
    input('Prompt successfully sent. Press any key to exit!')
