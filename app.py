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
            elif status[0] == "Password is not correct":
                pw_error = status[0]
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
    else:
        ready_to_make_new_user = False
        email_error = ""
        title_error = ""
        name1_error = ""
        name2_error = ""
        org_error = ""
        type_error = ""
        p1_error = ""
        p2_error = ""

        if 'email' in request.form:
            if not request.form['email']:
                email_error = "Must enter an email"
            else:
                if "@" not in request.form['email']:
                    email_error = "Please enter a valid email"
                else:
                    exists = authentication.verify_user(request.form['email'], "")
                    if exists[0] == "Password is not correct":
                        if exists[1] == request.form['email'] + "\n":
                            email_error = "User already exists"

        if 'title' in request.form:
            if request.form['title'] == "0":
                title_error = "Must select a title"
        if '1name' in request.form:
            if not request.form['1name']:
                name1_error = "Must enter your first name"
        if '2name' in request.form:
            if not request.form['2name']:
                name2_error = "Must enter your last name"
        if 'org' in request.form:
            if not request.form['org']:
                org_error = "Must enter the name of your organization"
        if 'u-type' in request.form:
            if request.form['u-type'] == "0":
                type_error = "Must select a user type"
        if 'password' in request.form:
            if not request.form['password']:
                p1_error = "Must enter a password"
        if 'password_check' in request.form:
            if request.form['password'] != request.form['password_check']:
                p2_error = "Passwords do not match"
            if not request.form['password_check']:
                p2_error = "Must confirm password"

        if email_error == "" and title_error == "" and name1_error == "" and name2_error == "" and org_error == "" and \
                type_error == "" and p1_error == "" and p2_error == "":
            ready_to_make_new_user = True

        if not ready_to_make_new_user:
            return render_template('sign.html', Err0=email_error, Err1=title_error,
                                   Err2=name1_error, Err3=name2_error, Err4=org_error, Err5=type_error,
                                   Err6=p1_error, Err7=p2_error)
        else:
            session['logged_in'] = True
            return redirect('/main')
