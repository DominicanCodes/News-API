from send_email import send_email
import requests

topic = 'tesla'
api_key = '5803574c55b04535837cc22cefbcc1ce'
url = f'https://newsapi.org/v2/everything?q={topic}&from=2022-11-07&\
        sortBy=publishedAt&apiKey=5803574c55b04535837cc22cefbcc1ce&\
        language=en'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = 'Subject: News for you!\n'

# Access the article titles and description
for article in content['articles'][:20]:
    if article['title'] is not None:
        message += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"
        # message = message.replace("\u2026", " ")
        # print(message)

# Encode message
message = message.encode("utf-8")

# Send email
send_email(message)