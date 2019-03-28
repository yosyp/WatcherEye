# WatcherEye

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/yosyp/WatcherEye.svg?branch=master)](https://travis-ci.com/yosyp/WatcherEye)
[![codecov](https://codecov.io/gh/yosyp/WatcherEye/branch/master/graph/badge.svg)](https://codecov.io/gh/yosyp/WatcherEye)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1e43cd5b04be47a0af71281d10ee5932)](https://app.codacy.com/app/yosyp/WatcherEye?utm_source=github.com&utm_medium=referral&utm_content=yosyp/WatcherEye&utm_campaign=Badge_Grade_Dashboard)

RESTful API with Flask that serves images from Raspberry Pi powered by picamera.

## Setup
This software is intended to run in the following environment:
1. Raspberry Pi 3 Model B v1.2
2. Picamera v2

The testing environment for this software is a Macbook, the built-ion camera is used.

## Installation
All dependencies are specified in `requirements.txt`. Install all python packages:

`pip install -r requirements.txt`

## Running
1. If using `virtualenvwrapper`: `workon WatcherEye`
2. Set Flask app environment variable: `export FLASK_APP=watchereye`
3. Set Flask app development variable:`export FLASK_ENV=info`
4. Start the Flask server: `flask run`
5. Point your favorite browser to `localhost:5000`

Note that flask in debug mode only exposes the web service locally on the host. To have the web service accessible from external IPs (i.e. using the public IP of the server), you may need to run flask with the `--host=0.0.0.0` flag.

## API Reference
The API can be accessed via HTTP/S requests, see `watchereye/api.py`for up-to-date API endpoint documentation. Briefly:

| Method | Endpoint         | Description              | Return Format                         |
|--------|------------------|--------------------------|---------------------------------------|
| `GET`  | `/api/v1/ping`   | Ping API server          | JSON array                            | 
| `GET`  | `/api/v1/stats`  | Usage statistics         | JSON array                            |
| `GET`  | `/api/v1/image`  | Capture and return image | image/jpeg                            |
| `GET`  | `/api/v1/stream` | View video stream        | multipart/x-mixed-replace; image/jpeg | 

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
