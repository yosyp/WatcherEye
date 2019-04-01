"""
This file contains unit tests for accessing and reading the camera modules.

"""
from io import BytesIO
from os import uname, environ
import watchereye
import imghdr
import pytest

# Skip hardware-based tests if using CI/CD tools:
@pytest.mark.skipif("TRAVIS" in environ and environ["TRAVIS"] == "true",
                    reason="Skipping test on Travis, no hardware camera.")

def test_camera_image():
    """
    GIVEN a camera resource
    WHEN an image is captured using the approriate module
    THEN check that the binary data is a jpeg
    """
    imgapi = watchereye.Image()

    if uname().sysname == 'Darwin':
        buf = imgapi.cameracapture()
    else:
        buf = imgapi.picameracapture()

    assert imghdr.what('', buf) == 'jpeg'