import os
import sqlite3

from flask_mail import Message, Mail
from flask import Flask, render_template, request
from helpers import lookup, addUserToNewsletter
from categories import categories
from countries import countries

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.register_blueprint(categories)
app.register_blueprint(countries)


def checkAndSendNewsletter(freq):
    global days
    conn = sqlite3.connect('newsletter.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ELIST WHERE FREQUENCY = '%s'" % (freq))
    rows = cursor.fetchall()
    for row in rows:
        send_mail_flask(row['email'], 'newsletter', row['name'], row['frequency'])
    conn.commit()
    conn.close()


scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda: checkAndSendNewsletter('daily'), trigger="interval", days=1)
scheduler.add_job(func=lambda: checkAndSendNewsletter('weekly'), trigger="interval", days=7)
scheduler.add_job(func=lambda: checkAndSendNewsletter('monthly'), trigger="interval", days=30)
scheduler.start()


def send_mail_flask(to, subject, name, frequency):
    responses = lookup('country', None, 'us')
    msg = Message(subject=subject, sender='200801223@rajalakshmi.edu.in', recipients=[to])
    details = {
        "name": name,
        "freq": frequency
    }
    msg.html = render_template('mail.html', full_response=responses['articles'], title='Top Headlines',
                               senderDetails=details)
    mail.send(msg)


@app.route('/mail')
def mailList():
    thisdict = {
        "name": "surya",
        "freq": "Weekly"
    }
    responses = lookup('country', None, 'us')
    return render_template('mail.html', full_response=responses['articles'], title='Top Headlines',
                           senderDetails=thisdict)


@app.route('/newsletter', methods=['POST'])
def newsletter():
    email = request.form.get('email')
    freq = request.form['default-radio']
    addUserToNewsletter(email, freq)
    return render_template('index.html')


@app.route('/')
def index():
    checkAndSendNewsletter('weekly')
    responses = lookup('country', None, 'us')
    return render_template('index.html', full_response=responses['articles'], title='Top Headlines')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    responses = lookup('search', query)
    print(responses['articles'])
    if responses['status'] == 'error':
        return render_template('apology.html', message='No Results Found', title='Not Found')
    return render_template('query.html', full_response=responses['articles'], title=query)


if __name__ == '__main__':
    app.run()
