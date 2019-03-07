#########
# Authors: Kyle Nielsen John Drake TODO add your name if you edit this file
# For: CIS 433 at UOregon
# Date of creation: February 6, 2019
# Last update: March 7, 2019  TODO keep updated
# Language: Python 3
# Credit:  TODO credit outside sources if applicable
# Program state: Basic check for name-email combo. Functions for adding and deleting name-email pairs. Can check if an email is in a list of confirmed phishers, as well as add and delete entries from the list. Only a few combos in database
# Hypothetical future improvement: Accounts, and either: each account has seperate datafiles, or only confirmed accounts can modify the datafiles
#########



import flask
from flask import Flask, request
import json


app = Flask(__name__)


with open("data.json", "r") as data_file:
    data = json.load(data_file)  # load the file with name-email combos

with open("phishers.json", "r") as phishers_file:
    phishers = json.load(phishers_file)  # load the file with confirmed phishing emails


@app.route("/api/check-pair")
def check():
    if not (request.args.get("name") and request.args.get("email")):
        return "error"  # return error if not all args were provided

    name = request.args.get("name")
    email = request.args.get("email")

    if name not in data:
        return "unknown"  # return unknown if name not in database

    if email in data[name]:
        return "valid"  # return valid if the pair matches

    return "invalid"  # otherwise, the pair didn't match. Invalid


@app.route("/api/add-pair")
def add():
    if not (request.args.get("name") and request.args.get("email")):
        return "error"

    name = request.args.get("name")
    email = request.args.get("email")

    if name in data:  # If the name is already in the data, append it to the existing list
        data[name].append(email)
    else:  # otherwise, create a key
        data[name] = [email]

    update_data_file()

    return "success"


@app.route("/api/del-pair")
def delete():
    if not (request.args.get("name") and request.args.get("email")):
        return "error"

    name = request.args.get("name")
    email = request.args.get("email")

    if name in data:  # no need to remove the email if the name doesn't exist
        while email in data[name]:  # remove duplicates, or don't try to remove if it isn't there
            data[name].remove(email)

    update_data_file()

    return "success"


@app.route("/api/check-phish")
def check_phish():
    if not request.args.get("email"):
        return "error"

    email = request.args.get("email")

    if email in phishers["phishers"]:
        return "confirmed"
    return "unconfirmed"


@app.route("/api/add-phish")
def add_phish():
    if not request.args.get("email"):
        return "error"

    email = request.args.get("email")

    phishers["phishers"].append(email)
    update_phishers_file()
    return "success"


@app.route("/api/del-phish")
def del_phish():
    if not request.args.get("email"):
        return "error"

    email = request.args.get("email")

    while email in phishers["phishers"]:
        phishers["phishers"].remove(email)
    update_phishers_file()
    return "success"


def update_data_file():
    with open("data.json", "w") as df:  # open data file with write permission
        json.dump(data, df)  # write json data to file


def update_phishers_file():
    with open("phishers.json", "w") as pf:
        json.dump(phishers, pf)


if __name__ == "__main__":  # passes if running on personal machine, but not on python anywhere
    app.run(debug=False, port=5001, host="0.0.0.0")
