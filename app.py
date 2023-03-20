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
        #To view profile or index page, change 'log' to 'profile' or 'index'
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

#The table on index won't show it's values unless 'values' table is added under the first 'if' statement (at line 30)
@app.route('/')
def index():
    values = [
        {'month': 'January', 'growth': 100, 'percent': 10, 'etc': 0},
        {'month': 'February', 'growth': 200, 'percent': 15, 'etc': 0},
        {'month': 'March', 'growth': 300, 'percent': 20, 'etc': 0},
        {'month': 'April', 'growth': 400, 'percent': 25, 'etc': 0},
        {'month': 'May', 'growth': 500, 'percent': 30, 'etc': 0},
        {'month': 'June', 'growth': 600, 'percent': 35, 'etc': 0},
        {'month': 'July', 'growth': 700, 'percent': 40, 'etc': 0},
        {'month': 'August', 'growth': 800, 'percent': 45, 'etc': 0},
        {'month': 'September', 'growth': 900, 'percent': 50, 'etc': 0},
        {'month': 'October', 'growth': 1000, 'percent': 55, 'etc': 0},
        {'month': 'November', 'growth': 1100, 'percent': 60, 'etc': 0},
        {'month': 'December', 'growth': 1200, 'percent': 65, 'etc': 0},
    ]
    return render_template('index.html', values=values)

#Uncomment if you want to run without using terminal
#if __name__ == '__main__':
#    app.run(debug=True)



