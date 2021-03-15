from flask import Flask

# To integrate the database
from config import Config
from flask_mongoengine import MongoEngine

# Special variable name to get that the current application is being rendered by flask
app = Flask(__name__)
# load the configuration deyails from config.py about database 
app.config.from_object(Config)

db=MongoEngine()
db.init_app(app)

from application import routes
