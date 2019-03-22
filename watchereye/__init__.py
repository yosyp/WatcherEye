import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from logging.config import dictConfig
from watchereye.api import *

"""
Logging config sets up logging to both STDOUT stream and log file.
"""
logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'stream': {'class': 'logging.StreamHandler',
                   'formatter': 'f',
                   'level': logging.DEBUG},                 
        'file': {'class': 'logging.handlers.RotatingFileHandler',
                 'filename': 'logs/log.log', # Change this filename or make sure logs/ exists!
                 'maxBytes': 1024,
                 'backupCount': 3,
                 'formatter': 'f',
                 'level': logging.DEBUG},
        },                 
    root = {
        'handlers': ['stream','file'],
        'level': logging.DEBUG,
        },
)

dictConfig(logging_config)
logger = logging.getLogger()


app = Flask(__name__)
api = Api(app)


"""
Display landing page 
@TODO API decription on landing page similar to what swagger provides.
"""
@app.route("/")
def home():
    return render_template("home.html", os = 'Windows')


"""
API endpoints route to classes with those names, with methods for get(), post(), etc.

See each class separately for further documentation, inputs and ouputs. 
"""
api.add_resource(Ping,   '/api/v1/ping')
api.add_resource(Stats,  '/api/v1/stats')
api.add_resource(Image,  '/api/v1/image')
api.add_resource(Stream, '/api/v1/stream')

if __name__ == '__main__':
    app.run(debug=True)
