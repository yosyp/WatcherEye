"""
Main module of the server file
"""
# import connexion
import logging
from logging.handlers import RotatingFileHandler
# from flask import render_template, request
import flask

# app = connexion.App(__name__, specification_dir="./")
app = flask.Flask(__name__)

app.add_api("swagger.yml")

@app.route("/")
def home():
    # app.app.logger.warning('%s A warning occurred (%d apples)', request.remote_addr, 42)
    # app.app.logger.error('An error occurred')
    app.app.logger.info('%s: home() index route served', request.remote_addr)
    return render_template("home.html", os = 'Windows')

if __name__ == '__main__':
    handler = RotatingFileHandler('../logs/log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)
    app.app.logger.info('Logging started')

