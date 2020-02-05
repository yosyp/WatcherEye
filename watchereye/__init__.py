"""
Main code entry point used by `flask run` to standup the web service.

This file does 3 things:
 1. Configure logging to relevant files and output streams
 2. Startup Flask() and Api()
 3. Configure routes to the root endpoint and all API endpoints
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from logging.config import dictConfig
from watchereye.api import *

"""
Check if logs/ directory exists, if it does not then create it.
Check if logs/log.log file exists, if it does not then create it.
"""
if not os.path.exists('logs'):
    os.makedirs('logs')

if not os.path.isfile('logs/log.log'):
    file = open('logs/log.log', 'w')

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
                   'formatter': 'f'},
        'file': {'class': 'logging.handlers.RotatingFileHandler',
                 'filename': 'logs/log.log', # Change this filename or make sure logs/ exists!
                 'maxBytes': 1024,
                 'backupCount': 3,
                 'formatter': 'f'},
        },
    root = {
        'handlers': ['stream','file'],
        'level': 'INFO',
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
    app.run()
