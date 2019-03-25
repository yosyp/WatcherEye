# WatcherEye
RESTful API with Flask that serves images from Raspberry Pi powered by picamera.

## Setup
This software is tested in the following environment:
1. Raspberry Pi 3 Model B v1.2
2. Picamera vX.Y

## Installation
All dependencies are specified in `requirements.txt`. Install all python packages:

`pip install -r requirements.txt`

## Running
1. If using `virtualenvwrapper`: `workon WatcherEye`
2. Set Flask app environment variable: `export FLASK_APP=watchereye`
3. Set Flask app development variable:`export FLASK_ENV=info`
4. Start the Flask server: `flask run`
5. Point your favorite browser to `localhost:5000`

The API can be accessed via HTTP/S requests, see `watchereye/api.py`for up-to-date API endpoint documentation. Briefly:

| Method | Endpoint | Description | Return Format |
|-|-|-|-|
| `GET` | `/api/v1/ping` | Ping API server | JSON array | 
| `GET` | `/api/v1/stats` | Usage statistics | JSON array |
| `GET` | `/api/v1/image` | Capture and return image | image/jpeg |
| `GET` | `/api/v1/stream` | View video stream | multipart/x-mixed-replace; image/jpeg | 

## Logging
Logging at the `debug` level (recording all incoming requests and IPs) using the default python `logging` facility. Logs are stored in `logs/log.log` and streamed to STDOUT

## Test
Using PyTest:
1. `workon WatcherEye`
2. `python -m pytest -s -v --disable-pytest-warnings tests/`

## References
1. [Installing Raspbian on Raspberry Pi on Mac OS X](https://www.raspberrypi.org/documentation/installation/installing-images/)
2. [Video Streaming with Flask](https://blog.miguelgrinberg.com/post/video-streaming-with-flask)
3. [Flask Video Streaming Revisited](https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited)

## Development Notes
Update `requirements.txt` after installing any new `pip` modules using:
`pip freeze > requirements.txt`
