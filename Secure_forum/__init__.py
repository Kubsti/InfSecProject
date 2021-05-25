from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.secret_key = os.urandom(24)
from Secure_forum import routes

