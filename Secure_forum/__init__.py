from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
from flask_login import LoginManager 
from Secure_forum import routes

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = os.urandom(24)


