#
# File: app.py
# Project: Healthcare Investment Tool
# Author(s): Alex Patterson, Micheal Martinez, Kaylo Leon, Govinda Ramrattan
# Purpose: contain page navigation and session information
#

# first time, in terminal: pip install flask
# to run website, in terminal (windows):  flask --app app --debug run
# flask is sensitive to file structure and names

from flask import Flask, render_template, request, url_for, flash, redirect, session
import random
import math
import authentication
from PythonToJson import row
from data_processing import age_data, insurance_data, city_data
import pymysql

app = Flask(__name__)

key = math.floor(random.random() * 23456)
app.config['SECRET_KEY'] = f'{key}'

# Connect to Database


mydb = pymysql.connect(
    host='hcitDB.cmswaq8q4kav.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='POnMQIgR6AB3FbyYJ5DZ',
    db='sys'
)


def user_info(username):
    """
    Grabs user info from database
    """
    cursor = mydb.cursor()
    query = "SELECT * FROM sys."
    cursor.execute(query)
    myresult = cursor.fetchall()


def add_user(info_list):
    """
    Inserts a user's info into database
    """
    cursor = mydb.cursor()
    query = "SELECT * FROM sys."
    cursor.execute(query)


@app.route('/', methods=['GET', 'POST'])
def log():
    """
    Start up website -> first page is log in: can enter credentials or navigate to sign up page
    """
    if request.method == "GET":
        # To view profile or index page, change 'log' to 'profile' or 'index'
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
                return redirect(url_for("index"))
            elif status == "Password is not correct":
                pw_error = status
            elif status == "Username not associated with an account":
                user_error = status + ". Do you need to sign up?"

        return render_template('log.html', ErrU=user_error, ErrP=pw_error)


@app.route('/signup', methods=['GET', 'POST'])
def sign():
    """
    Sign up page, allows you to enter new credentials or navigate back to log in page
    """
    if request.method == "GET":
        return render_template('sign.html')


# The table on index won't show it's values unless 'values' table is added under the first 'if' statement (at line 30)
@app.route('/dashboard')
def index():
    """
    Dashboard loads after log in or sign up, displays data, navigation to profile page, contains a log out button
    """
    test = row  # What displays after inspect index
    ages = age_data
    insurance = insurance_data
    city = city_data
    values = [
        {'city': 'Jacksonville', 'percent': 14.84, 'future': 967200, 'predicted': 143532},
        {'city': 'Miami', 'percent': 14.07, 'future': 433900, 'predicted': 61049},
        {'city': 'Orlando', 'percent': 14.22, 'future': 313900, 'predicted': 44636},
        {'city': 'Tampa', 'percent': 15.61, 'future': 396400, 'predicted': 61878},
        {'city': 'Fort Myers', 'percent': 14.24, 'future': 112400, 'predicted': 16005},
    ]
    return render_template('dashboard.html', values=values, ages=ages, test=test, insurance=insurance, city=city)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        name = f"{first_name} {last_name}"

        organization = request.form['organization']
        title_position = request.form['title_position']
        work_number = request.form['work_number']
        mobile_number = request.form['mobile_number']
        email_address = request.form['email_address']
        email = f"{email_address}"

        return render_template("profile.html", name=name, email=email, first_name=first_name, last_name=last_name,
                               organization=organization, title_position=title_position, work_number=work_number,
                               mobile_number=mobile_number, email_address=email_address)
    else:
        return render_template("profile.html", name=name, email=email, first_name=first_name, last_name=last_name,
                               organization=organization, title_position=title_position, work_number=work_number,
                               mobile_number=mobile_number, email_address=email_address)

# Uncomment if you want to run without using terminal
# if __name__ == '__main__':
# app.run(debug=True)
