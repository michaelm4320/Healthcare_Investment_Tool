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
import authentication

app = Flask(__name__)

key = math.floor(random.random() * 23456)
app.config['SECRET_KEY'] = f'{key}'

test_variable1 = "Healthcare Investment Tool"
test_variable2 = 6725432


@app.route('/', methods=['GET', 'POST'])
def log():
    session['logged_in'] = False
    if request.method == "GET":
        return render_template('log.html')
    else:
        user_error = ""
        pw_error = ""
        if 'username' in request.form:
            session['user'] = request.form['username']
            if not request.form['username']:
                user_error = "Must enter a username"

        if 'password' in request.form:
            session['pass'] = request.form['password']
            if not request.form['password']:
                pw_error = " Must enter a password"

        if session['pass'] and session['user']:
            status = authentication.verify_user(session['user'], session['pass'])
            if status == "true":
                session['logged_in'] = True
                return render_template('index.html', Radiant=status)
            elif status == "Password is not correct":
                pw_error = status
            elif status == "Username not associated with an account":
                user_error = status + ". Do you need to sign up?"

        return render_template('log.html', ErrU=user_error, ErrP=pw_error)


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        if not session['logged_in']:
            return redirect('/')
        else:
            return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign():
    if request.method == "GET":
        return render_template('sign.html')






