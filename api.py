"""
API module responds to all api requests defined in swagger.yml
"""
from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def ping():
    """
    This function responds to a request for /api/v1/ping
    with timestamp and pong

    :return:        JSON array
    """
    return ['pong', get_timestamp()]

def stats():
    """
    This function responds to a request for /api/v1/stats
    with API usage statistics

    :return:        JSON array
    """
    return 'stats go here'

def image():
        