import flask
from flask import Flask, request
import json


app = Flask(__name__)


@app.route("/api/check-pair")
def check():
    if not (request.args.get("name") and request.args.get("email")):
        return "error"

    name = request.args.get("name")
    email = request.args.get("email")
    
    if name not in data:
        return "unknown"
    
    if email in data[name]:
        return "valid"
        
    return "invalid"


if __name__ == "__main__":
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    app.run(debug=True, port=5001, host="0.0.0.0")
