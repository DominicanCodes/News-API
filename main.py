import requests

api_key = '5803574c55b04535837cc22cefbcc1ce'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-11-07&\
    sortBy=publishedAt&apiKey=5803574c55b04535837cc22cefbcc1ce'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])