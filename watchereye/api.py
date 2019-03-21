from io import BytesIO
from time import sleep
import requests
from flask import send_file, request
from flask_restful import Resource

class Ping(Resource):
    """
    This function

    :return     JSON array
    """
    def get(self):
        return "hello!"

class Stats(Resource):
    """
    This function

    :return     JSON array
    """    
    def get(self):
        return "stats!"

class Image(Resource):
    """
    This function

    :return     JSON array
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
    This function

    :return     JSON array
    """    
    def get(self):
        return "stream!" 

