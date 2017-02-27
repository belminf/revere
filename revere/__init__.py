"""Application bootstrap

Setup the flask application here.
"""

from flask import Flask
from flask_restful import Api
from revere.config import DEBUG
import types

app = Flask(__name__.split('.')[0])
api = Api(app)
app.debug = DEBUG


def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper


api.route = types.MethodType(api_route, api)
