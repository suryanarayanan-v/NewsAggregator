from flask import Blueprint, render_template
from helpers import lookup

categories = Blueprint('categories', __name__)


@categories.route('/business')
def business():
    responses = lookup('category', 'business', 'us')
    return render_template('query.html', full_response=responses['articles'], title='Business')


@categories.route('/entertainment')
def entertainment():
    responses = lookup('category', 'entertainment', 'us')
    return render_template('query.html', full_response=responses['articles'], title='Entertainment')


@categories.route('/general')
def general():
    responses = lookup('category', 'general', 'us')
    return render_template('query.html', full_response=responses['articles'], title='General')


@categories.route('/health')
def health():
    responses = lookup('category', 'health', 'us')
    return render_template('query.html', full_response=responses['articles'], title='Health')


@categories.route('/science')
def science():
    responses = lookup('category', 'science', 'us')
    return render_template('query.html', full_response=responses['articles'], title='Science')


@categories.route('/sports')
def sports():
    responses = lookup('category', 'sports', 'us')
    return render_template('query.html', full_response=responses['articles'], title='Sports')


@categories.route('/technology')
def technology():
    responses = lookup('category', 'technology', 'us')
    return render_template('query.html', full_response=responses['articles'], title="Technology")
