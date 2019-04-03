"""
...
"""

import pytest
import imghdr
from os import environ

from watchereye import *

# Skip hardware-based tests if using CI/CD tools
@pytest.mark.skipif("TRAVIS" in environ and environ["TRAVIS"] == "true",
                    reason="Skipping test on Travis, no hardware camera.")

def test_api_image(client):
    """
    GIVEN a HTTP GET endpoint that serves an image
    WHEN the endpoint is hit
    THEN check that the returned binary is a jpeg.
    """

    rv = client.get('/api/v1/image')

    assert imghdr.what('', rv.data) == 'jpeg'