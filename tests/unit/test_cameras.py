"""
This file 

"""
from io import BytesIO
from os import uname
import watchereye
import imghdr

def test_camera_image():
    """
    GIVEN a camera resource
    WHEN capturing an image
    THEN check that it can be converted to binary data
    """
    imgapi = watchereye.Image()

    if uname().sysname == 'Darwin':
        buf = imgapi.cameracapture() 
    else:
        buf = imgapi.picameracapture() 

    assert imghdr.what('', buf) == 'jpeg'

# def test_camera_stream():
#     """

#     """
#     streamapi = watchereye.Stream()

#     if uname().sysname == 'Darwin':
#         buf = imgapi.camerastream() 
#     else:
#         buf = imgapi.picamerastream()     

#     assert
