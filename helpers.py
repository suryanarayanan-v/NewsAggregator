import requests
import os
import datetime


def lookup(query_type=None, query=None, country=None):
    api_key = os.environ.get('API_KEY')
    if query_type == 'country':
        url = (f'http://newsapi.org/v2/top-headlines?'
               f'country={country}&'
               f'apiKey={api_key}')
        response = requests.get(url)
        responseJson = response.json()
    elif query_type == 'category':
        url = (f'http://newsapi.org/v2/top-headlines?'
               f'country={country}&'
               f'category={query}&'
               f'apiKey={api_key}')
        response = requests.get(url)
        responseJson = response.json()
    elif query_type == 'search':
        url = (f'http://newsapi.org/v2/everything?'
               f'q={query}&'
               f'from{datetime.date.today() - datetime.timedelta(days=1)}&'
               f'apiKey={api_key}')
        response = requests.get(url)
        responseJson = response.json()
    if responseJson['status'] == 'error':
        return responseJson
    for article in responseJson['articles']:
        if article['content'] is None:
            article['content'] = ''

    return responseJson
