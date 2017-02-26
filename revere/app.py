"""Application bootstrap

Setup the flask application here.
"""

from flask import Flask
from flask_restful import Api
from config import DEBUG

app = Flask(__name__.split('.')[0])
api = Api(Flask)
app.debug = DEBUG
