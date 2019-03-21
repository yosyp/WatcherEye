from io import BytesIO
from time import sleep
import requests
from flask import send_file, request
from flask_restful import Resource

class Ping(Resource):
    """
    This function returns a ping response, current time, and server uptime. 

    :return     JSON array
    """
    def get(self):
        return "hello!"

class Stats(Resource):
    """
    This function returns server statistics by analyzing the log file, including
    the number of images taken and served.

    :return     JSON array
    """    
    def get(self):
        return "stats!"

class Image(Resource):
    """
    This function returns a static image or picture from Picamera if running on 
    a Raspberry Pi. 

    :return     binary file, image/jpeg
    """    
    def get(self):
        my_stream = BytesIO()
        runningOnPi = False
        if runningOnPi == True:
            # Create an in-memory stream
            camera = PiCamera()
            camera.start_preview()
            # Camera warm-up time
            sleep(2)
            camera.capture(my_stream, 'jpeg')
        else:
            my_stream = requests.get('https://cdn-images-1.medium.com/max/2400/0*KR0lpn7XYPGo1KBo.jpg').content

        return send_file(BytesIO(my_stream), mimetype="image/jpeg")        


class Stream(Resource):
    """
    This function returns a multipart video stream from Picamera if running on 
    a Raspberry Pi, or a loop from file.

    :return     binary stream, multipart/x-mixed-replace; boundary=frame
    """    
    def get(self):
        return "stream!" 

