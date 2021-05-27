from flask import Flask
import os

app = Flask(__name__)
from Secure_forum import routes
app.secret_key = os.urandom(24)


