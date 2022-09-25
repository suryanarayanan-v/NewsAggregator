from flask import Flask, render_template, request
from helpers import lookup
from categories import categories
from countries import countries

app = Flask(__name__)

app.register_blueprint(categories)
app.register_blueprint(countries)


@app.route('/')
def index():
    responses = lookup('country', None, 'us')
    return render_template('index.html', full_response=responses['articles'], title='Top Headlines')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    responses = lookup('search', query)
    if responses['status'] == 'error':
        return render_template('apology.html', message='No Results Found', title='Not Found')
    return render_template('query.html', full_response=responses['articles'], title=query)


if __name__ == '__main__':
    app.run()
