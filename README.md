# WatcherEye
RESTful API with Flask that serves images from Raspberry Pi powered by picamera.

## Setup
This software is tested in the following environment:
1. Raspberry Pi 3 Model B v1.2
2. Picamera vX.Y

## Installation
Install all python packages:

`pip install -r requirements.txt`

## Running
1. Run `python watcheye.py` 
2. Point your favorite browser to `localhost:5000`

The API can be accessed via HTTP/S requests, see `swagger.yml` for up-to-date API endpoints:


- /api/v1/ping
  description: "Ping API server"
- name: "stats"
  description: "Usage statistics"
- name: "image"
  description: "Capture and return image"
- name: "stream"
  description: "View video streama"  

## References
1. [Installing Raspbian on Raspberry Pi on Mac OS X](https://www.raspberrypi.org/documentation/installation/installing-images/)
