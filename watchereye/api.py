"""
All API endpoints are defined here along with some helper methods.

The Api() module adds resources in the form of classes, so each endpoint here is encapsulated
in its own class. Within each glass the HTTP Method is named get(), post(), etc. In this way can
separate the HTTP response logic with any helper methods.
"""

from io import BytesIO
from time import sleep
from flask import send_file, request, Response
from flask_restful import Resource
from datetime import datetime
from os import uname
import numpy as np
import requests
import cv2
import time

def get_timestamp():
    """
    This function returns current date prettyprinted in %Y-%m-%d %H:%M:%S format.

    :return     string
    """
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

class Ping(Resource):
    """
    This method returns a ping response, current time, and server uptime. 

    :return     JSON array
    """
    def get(self):
        return ['pong', get_timestamp()]

class Stats(Resource):
    """
    This method returns server statistics by analyzing the log file, including
    the number of images taken and served.

    :return     JSON array
    """    
    def get(self):
        return "stats!"

class Image(Resource):
    """
    This method that reads a USB/laptop camera and returns 1 frame

    :return binary image/jpeg
    """
    def cameracapture(self):
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        _, img = camera.read()
        return (cv2.imencode('.jpg', img)[1].tobytes())

    """
    This method reads a Raspberry Pi camera and returns 1 frame 

    :return binary image/jpeg
    """
    def picameracapture(self):
        stream = BytesIO()
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')
        return (cv2.imencode('.jpg', stream)[1].tobytes())

    """
    This method returns a static image from a camera 

    :return     binary file, image/jpeg
    """    
    def get(self):
        if uname().sysname == 'Darwin':
            return Response(self.cameracapture(),   mimetype='image/jpeg')          
        else:
            return Response(self.picameracapture(), mimetype='image/jpeg')          

class Stream(Resource):
    """
    This is a generator function/method that reads a USB/laptop camera and yields 1 frame 
    of a multipart jpeg video stream.

    @TODO: Implement pytest with generator functions.

    :return binary stream, image/jpeg frame
    """
    def camerastream(self):
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # return current frame            
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', img)[1].tobytes() + b'\r\n')                    

    """
    This is a generator function/method that reads a Raspberry Pi camera and yields 1 frame 
    of a multipart jpeg video stream. 

    @TODO: Implement pytest with generator functions.

    :return binary stream, image/jpeg frame
    """
    def picamerastream(self):
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

    """
    This method returns a multipart video stream from a camera.

    :return     binary stream, multipart/x-mixed-replace; boundary=frame
    """    
    def get(self):
        if uname().sysname == 'Darwin':
            return Response(self.camerastream(),   mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return Response(self.picamerastream(), mimetype='multipart/x-mixed-replace; boundary=frame')

