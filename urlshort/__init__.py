# This file will be called automatically by flask to setup our app
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "jh34jh3j4h3jh43j4h9edj23u28khd389hdjsn"

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app