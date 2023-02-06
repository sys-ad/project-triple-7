import os
import json
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title='Team Portfolio', url=os.getenv("URL"), users=data["users"])

def user_route(username):
    def user_func():
        return render_template(f'{username}.html', title=username, url=os.getenv("URL"))
    return user_func

with open("app/data.json") as file:
    data = json.load(file)
    for user in data["users"]:
        first_name = user["firstName"].lower()
        app.add_url_rule(f'/{first_name}', first_name, user_route(first_name))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404', url=os.getenv("URL")), 404

if __name__ == "__main__":
    app.debug = True
    app.run()
