import os
from revere import app
from revere.resources import tags

#  Workaround for the werkzeug reloader removing the current directory from the
#  path. It's nasty, but it works! Inspired by:
#  https://github.com/mitsuhiko/flask/issues/1246
os.environ['PYTHONPATH'] = os.getcwd()

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
