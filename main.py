import requests

api_key = '5803574c55b04535837cc22cefbcc1ce'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-11-07&\
    sortBy=publishedAt&apiKey=5803574c55b04535837cc22cefbcc1ce'

request = requests.get(url)
content = request.text



print(content)