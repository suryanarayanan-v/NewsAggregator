import re

import requests
import os
import datetime
import sqlite3


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


def addUserToNewsletter(emailID, frequency):
    conn = sqlite3.connect('newsletter.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS ELIST (email TEXT UNIQUE, name TEXT, LASTSENT TEXT, FREQUENCY TEXT);''')
    name = emailID.split("@")[0]
    lastSent = datetime.date.today()
    try:
        conn.execute("INSERT INTO ELIST (email, name, lastsent, frequency) VALUES (?,?,?,?)",
                     (emailID, name, lastSent, frequency))
    except:
        print('failed')

    conn.row_factory = sqlite3.Row  # add this row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ELIST")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row['email']}, {row['lastsent']}, {row['frequency']}.")

    conn.commit()
    conn.close()



