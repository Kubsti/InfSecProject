from flask import Flask
from Secure_forum import app

if __name__ == "__main__":
    app.run(debug=True) #, ssl_context='adhoc')