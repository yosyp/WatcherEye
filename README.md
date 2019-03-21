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
1. If using `virtualenvwrapper`: `workon WatcherEye`
2. `export FLASK_APP=watchereye`
3. `export FLASK_ENV=development`
4. `flask run`
5. Point your favorite browser to `localhost:5000`

The API can be accessed via HTTP/S requests, see `swagger.yml` for up-to-date API endpoints:

| Method | Endpoint | Description |
|-|-|-|
| `GET` | `/api/v1/ping` | Ping API server |
| `GET` | `/api/v1/stats` | Usage statistics |
| `GET` | `/api/v1/image` | Capture and return image |
| `GET` | `/api/v1/stream` | View video stream |

## Logging
Logging is done by default at the `info` level (recording all incoming requests and IPs) using the default python `logging` facility. Logs are stored in `logs/log.log`

## References
1. [Installing Raspbian on Raspberry Pi on Mac OS X](https://www.raspberrypi.org/documentation/installation/installing-images/)
2. [Video Streaming with Flask](https://blog.miguelgrinberg.com/post/video-streaming-with-flask)