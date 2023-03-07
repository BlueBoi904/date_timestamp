
from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route("/")
def date_timestamp():
    return {"unix": "", "utc": ""}
