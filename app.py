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

#Running the command would not work for me so I uncommented
#this to just run the program without using terminal

#if __name__ == '__main__':
#    app.run(debug=True)