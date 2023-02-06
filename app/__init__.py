import os
import json
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='templates')

with open("app/data.json") as file:
    data = json.load(file)

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html', title='Team Portfolio', url=os.getenv("URL"))
=======
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
>>>>>>> 39ce3e5b6b7259218ca7212d955f008c89f50005

def user_route(username):
    def user_func():
        return render_template(f'{username}.html', title=username, experiences=data[username]["workExperiences"], hobbies=data[username]["hobbies"], url=os.getenv("URL"))
    return user_func

<<<<<<< HEAD
with open("app/data.json") as file:
    data = json.load(file)
    for user in data:
        first_name = user.lower()
        app.add_url_rule(f'/{first_name}', first_name, user_route(first_name))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404', url=os.getenv("URL")), 404

if __name__ == "__main__":
    app.debug = True
    app.run()
=======
@app.route('/traveling')
def travel():
    return render_template('travels.html', title="Traveling", url=os.getenv("URL"))
>>>>>>> 39ce3e5b6b7259218ca7212d955f008c89f50005
