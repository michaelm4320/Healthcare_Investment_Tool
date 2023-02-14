#
# File: app.py
# Project: Healthcare Investment Tool
# Author(s): Alex Patterson,
# Purpose: contain page navigation and session information
#

# first time, in terminal: pip install flask
# to run website, in terminal (windows and pycharm):  flask --app app --debug run
# flask is sensitive to file structure and names

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')