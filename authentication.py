#
# File: authentication.py
# Project: Healthcare Investment Tool
# Author(s): Alex Patterson,
# Purpose: contain functions for handling usernames/passwords
#
from werkzeug.security import generate_password_hash, check_password_hash
#newtFoot6732 - hotplate
#Blue2butt4 - alex
#qtpie - cbat


def verify_user(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    file = open("image.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for line in data:
        index += 1
        if username in line:
            user_hash = data[index]
            user_hash = user_hash.replace("\n", "")
            is_user = check_password_hash(user_hash, password)
            if is_user:
                return "true"
            else:
                return "Password is not correct", line
    return "Username not associated with an account"


def add_user(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    file = open("image.txt", 'r')
    data = file.read()
    file.close()
    if username in data:
        return "There is already an account with that username"
    else:
        file = open("image.txt", "a")
        file.write(username + "\n")
        hashpw = generate_password_hash(password)
        file.write(hashpw + "\n")
        return "true"

