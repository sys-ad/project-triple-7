import os
import json
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title='Team Portfolio', url=os.getenv("URL"), users=data["users"])

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/travels')
def travels():
    return render_template('travels.html', title="Travels", url=os.getenv("URL"))

@app.route('/rachel')
def rachel():
    return render_template('rachel.html', title="Rachel", url=os.getenv("URL"))

@app.route('/eliza')
def eliza():
    return render_template('eliza.html', title="Eliza", url=os.getenv("URL"))

@app.route('/helen')
def helen():
    return render_template('helen.html', title="Helen", url=os.getenv("URL"))

@app.route('/mauricio')
def mauricio():
    return render_template('mauricio.html', title="Mauricio", url=os.getenv("URL"))

@app.route('/line', methods =["GET"])
def line_chart():
  """
  Doing a bunch of python
  Using a small example data set.
  """
  data = json.dumps( [1.0,2.0,3.0] )
  labels=json.dumps( ["12-31-18", "01-01-19", "01-02-19"] )
  return render_template("profile_template.html", data = data,
                        labels=labels)