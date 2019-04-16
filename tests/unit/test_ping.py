"""
This file contains unit tests for the Ping class get() method of the ping API endpoint.

"""
import watchereye

def test_ping():
    """
    GIVEN ping GET endpoint method
    WHEN the ping() method is triggered
    THEN check that JSON string with 'pong' as first element is returned.
    """
    ping = watchereye.Ping()

    assert ping.get()[0] == 'pong'
