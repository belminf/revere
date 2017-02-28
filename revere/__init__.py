"""Application bootstrap

Setup the flask application here.
"""

from flask import Flask
from flask_restful import Api
import types

app = Flask(__name__.split('.')[0])
api = Api(app)

# Load configuration
app.config.from_object('revere.config')

# Override config if environment variable exists
try:
    app.config.from_envvar('REVERE_CONFIG_FILE')
except RuntimeError:
    pass


def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper


api.route = types.MethodType(api_route, api)
