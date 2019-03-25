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
    rv = client.get('/api/v1/stats')

    # temporary placeholder until response is finalized:
    assert rv.data == b'"stats!"\n'

    # finalized response validation goes here:
    # assert json.loads(rv.data)[0] == 'pong'