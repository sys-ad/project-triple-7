import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title='Team portfolio', url=os.getenv("URL"), users=data["users"])

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/traveling')
def travel():
    return render_template('hobbies.html', title="Traveling", url=os.getenv("URL"))