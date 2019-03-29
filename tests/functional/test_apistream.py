"""

"""

import pytest
import imghdr
from os import environ

from watchereye import *

# Skip hardware-based tests if using CI/CD tools
@pytest.mark.skipif("TRAVIS" in environ and environ["TRAVIS"] == "true",
                    reason="Skipping test on Travis, no hardware camera.")

def test_api_stream(client):
    """
    GIVEN
    WHEN
    THEN
    """
    # rv = client.get('/api/v1/stream')

    # assert imghdr.what('', rv.data) == 'jpeg'