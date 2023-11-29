import requests
from send_email import send_email

topic = "tesla"

api_key = "43f86ffc46984db794b257b903c78bf1"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "apiKey=43f86ffc46984db794b257b903c78bf1&"
       "language=en")

# Make a request with newsapi
request = requests.get(url)

# Get a dictionary in JSON format
content = request.json()

# Send an email with news titles, descriptions and url
raw_message = f"""\
Subject: Today's news

"""
for article in content['articles'][:10]:
    if article['title'] is not None:
        raw_message += article['title'] + "\n"
        if article['description'] is not None:
            raw_message += article['description'] + "\n"
        raw_message += article['url'] + "\n\n"

send_email(raw_message.encode('utf-8'))
