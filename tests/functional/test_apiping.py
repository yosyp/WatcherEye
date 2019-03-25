import os
import tempfile
import json
import pytest

from watchereye import *

def test_ping(client):
    """
    GIVEN
    WHEN
    THEN
    """
    rv = client.get('/api/v1/ping')
    assert json.loads(rv.data)[0] == 'pong'