import os
import time
from flask import Flask

app = Flask(__name__)

APP_VERSION = "Version 2"


@app.route("/")
def home():
    slot = os.environ.get("SLOT_NAME", "not set")
    instance = os.environ.get("WEBSITE_INSTANCE_ID", "local")[:8]
    return (
        f"<h1>{APP_VERSION}</h1>"
        f"<p>Slot setting: {slot}</p>"
        f"<p>Instance: {instance}</p>"
    )


@app.route("/burn")
def burn():
    seconds = 20
    end = time.time() + seconds
    count = 0
    while time.time() < end:
        count += 1
    return f"Burned CPU for {seconds} seconds ({count} loops)"