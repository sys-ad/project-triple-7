import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    projects = [
        {
            "name": "Personal Library",
            "link": "https://github.com/rachelxiao907/congenial-broccolis",
            "description": "A web application that serves as an online library for users to store a selection of books and movies they search for."
        },
        {
            "name": "Space Invaders",
            "link": "https://github.com/rachelxiao907/APCSFinalProject",
            "description": "This project is a version of the game Space Invaders done in Processing. It is an interactive game where the player controls the shooter by moving it left and right with the arrow keys and pressing the spacebar to shoot a bullet upwards that harms the aliens."
        }
    ]
    return render_template('index.html', title="Rachel Xiao", projects=projects, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/traveling')
def travel():
    return render_template('travels.html', title="Traveling", url=os.getenv("URL"))