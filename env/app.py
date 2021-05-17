from flask import Flask, render_template
from databasemanagement import getposts
from jinja2 import Environment, select_autoescape

app = Flask(__name__)
@app.route("/")
def home():
    qrows = getposts()
    return render_template('index.html', rows = qrows, status=True)
