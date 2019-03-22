from io import BytesIO
from time import sleep
from flask import send_file, request, Response
from flask_restful import Resource
import requests
import cv2
import numpy as np

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
    This is a generator function that reads a USB/laptop camera and yields 1 frame 
    of a multipart jpeg video stream.

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
    This is a generator function that reads a Raspberry Pi camera and yields 1 frame 
    of a multipart jpeg video stream.

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
    This function returns a multipart video stream from Picamera if running on 
    a Raspberry Pi, or a loop from file.

    :return     binary stream, multipart/x-mixed-replace; boundary=frame
    """    
    def get(self):
        return Response(self.camerastream(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
