#
# File: app.py
# Project: Healthcare Investment Tool
# Author(s): Alex Patterson,
# Purpose: contain page navigation and session information
#

# first time, in terminal: pip install flask
# to run website, in terminal (windows):  flask --app app --debug run
# flask is sensitive to file structure and names

from flask import Flask, render_template, request, url_for, flash, redirect, session
import random
import math

app = Flask(__name__)

key = math.floor(random.random() * 23456)
app.config['SECRET_KEY'] = f'{key}'

test_variable1 = "Healthcare Investment Tool"
test_variable2 = 6725432


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', Radiant=test_variable1, Awesome=test_variable2)


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template('dashboard.html')


@app.route('/log_in', methods=['GET', 'POST'])
def log():
    if request.method == "GET":
        return render_template('log.html')
    else:
        if 'username' in request.form:
            session['user'] = request.form['username']

        if 'password' in request.form:
            session['pass'] = request.form['password']

        return render_template('index.html', Radiant=session['user'], Awesome=session['pass'])



