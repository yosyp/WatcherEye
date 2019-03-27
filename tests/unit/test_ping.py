"""
This file contains unit tests for the ping() GEt function of the ping API endpoint.

"""
import watchereye

def test_ping():
    """
    GIVEN ping GET endpoint function
    WHEN the ping() function is triggered
    THEN check that is returns a JSON with 'pong' as first element.
    """
    ping = watchereye.Ping()

    assert ping.get()[0] == 'pong'
