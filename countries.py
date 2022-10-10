from flask import Blueprint, render_template
from helpers import lookup

countries = Blueprint('countries', __name__)


@countries.route('/australia')
def australia():
    responses = lookup('country', None, 'au')
    return render_template('index.html', full_response=responses['articles'], title='Australia')


@countries.route('/canada')
def canada():
    responses = lookup('country', None, 'ca')
    return render_template('index.html', full_response=responses['articles'], title='Canada')


@countries.route('/germany')
def germany():
    responses = lookup('country', None, 'de')
    return render_template('index.html', full_response=responses['articles'], title='Germany')


@countries.route('/india')
def india():
    responses = lookup('country', None, 'in')
    return render_template('index.html', full_response=responses['articles'], title='India')


@countries.route('/southkorea')
def southkorea():
    responses = lookup('country', None, 'kr')
    return render_template('index.html', full_response=responses['articles'], title='South Korea')


@countries.route('/uk')
def uk():
    responses = lookup('country', None, 'gb')
    return render_template('index.html', full_response=responses['articles'], title='United Kingdom')


@countries.route('/us')
def us():
    responses = lookup('country', None, 'us')
    return render_template('index.html', full_response=responses['articles'], title='United States')
