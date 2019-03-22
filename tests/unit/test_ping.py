"""
This file 
"""
import watchereye

def test_ping():
    """
    GIVEN
    WHEN
    THEN
    """
    ping = watchereye.Ping()

    assert ping.get()[0] == 'pong'
