#########
# Authors: Kyle Nielsen John DrakeTODO add your name if you edit this file
# For: CIS 433 at UOregon
# Date of creation: February 6, 2019
# Last update: February 6, 2019  TODO keep updated
# Language: Python 3
# Credit:  TODO credit outside sources if applicable
# Program state: Basic check for name-email combo. Only 1 combo in database
#########



import flask
from flask import Flask, request
import json


app = Flask(__name__)


with open("/home/Scopt97/cis433proj/data.json", "r") as data_file:
    data = json.load(data_file)  # load the file with name-email combos


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


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
