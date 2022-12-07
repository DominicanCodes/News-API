from send_email import send_email
import requests

api_key = '5803574c55b04535837cc22cefbcc1ce'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-11-07&\
    sortBy=publishedAt&apiKey=5803574c55b04535837cc22cefbcc1ce'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = 'Subject: News for you!\n'

# Access the article titles and description
for article in content['articles']:
    if article['title'] is not None:
        message += f"""
                    {article['title']}
                    {article['description']}
                    """
        # message = message.replace("\u2026", " ")
        # print(message)

# Encode message
message = message.encode("utf-8")

# Send email
send_email(message)