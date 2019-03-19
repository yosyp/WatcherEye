"""
API module responds to all api requests defined in swagger.yml
"""
import platform
from io import BytesIO
from time import sleep
from datetime import datetime
from flask import make_response, abort, send_file

"""
BEGIN: Imports used for debugginig
"""
import requests
"""
END: Imports used for debugginig
"""

runningOnPi = False

if platform.system() == 'Linux':
    from picamera import PiCamera
    runningonPi = True


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def ping():
    """
    This function responds to a request for /api/v1/ping
    with timestamp and pong

    :return:        JSON array
    """
    app.app.logger.info('%s: ping()', request.remote_addr)
    return ['pong', get_timestamp()]

def stats():
    """
    This function responds to a request for /api/v1/stats
    with API usage statistics

    :return:        JSON array
    """
    app.app.logger.info('%s: stats()', request.remote_addr)    
    return 'stats go here'

def image():
    """
    This function responds to a request for /api/v1/image
    with API usage statistics

    :return:        JSON array
    """
    my_stream = BytesIO()
    if runningOnPi == True:
        # Create an in-memory stream
        camera = PiCamera()
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture(my_stream, 'jpeg')
        app.app.logger.info('%s: image() from Pi', request.remote_addr)
    else:
        my_stream = requests.get('https://cdn-images-1.medium.com/max/2400/0*KR0lpn7XYPGo1KBo.jpg').content
        app.app.logger.info('%s: image() from non-Pi', request.remote_addr)

    return send_file(BytesIO(my_stream), mimetype="image/jpeg")

def stream():
    """
    This function responds to a request for /api/v1/stream
    with API usage statistics

    :return:        JSON array
    """
        app.app.logger.info('%s: stream() returned', request.remote_addr)
    # return send_file('img.png', mimetype='image/png')
    return 'hello'   