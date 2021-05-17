from flask import Flask, render_template
from databasemanagement import getposts
from jinja2 import Environment, select_autoescape

app = Flask(__name__)
#should never be done and is only there to show that if autoescape is distabled then the application is open for XSS attacks
env =Environment(autoescape=select_autoescape(
    disabled_extensions=('html')
))
@app.route("/")
def home():
    qrows = getposts()
    return render_template('index.html', rows = qrows, status=True)
