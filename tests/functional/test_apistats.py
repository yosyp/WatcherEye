"""
...
"""

from watchereye import *

def test_api_stats(client):
    """
    GIVEN a HTTP GET stats endpoint
    WHEN the endpoint is hit
    THEN
    """

    rv = client.get('/api/v1/stats')

    # temporary placeholder until response is finalized:
    assert rv.data == b'"stats!"\n'

    # finalized response validation goes here:
    # assert json.loads(rv.data)[0] == 'pong'
