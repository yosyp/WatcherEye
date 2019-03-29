"""

"""

import json
import pytest

from watchereye import *

def test_api_ping(client):
    """
    GIVEN a HTTP GET ping endpoint
    WHEN the endpoint is hit
    THEN check that JSON string with 'ping' as first element is returned.
    """

    rv = client.get('/api/v1/ping')
    assert json.loads(rv.data)[0] == 'pong'