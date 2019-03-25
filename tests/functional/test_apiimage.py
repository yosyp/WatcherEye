import pytest
import imghdr

from watchereye import *

def test_api_image(client):
    """
    GIVEN
    WHEN
    THEN
    """
    rv = client.get('/api/v1/image')

    assert imghdr.what('', rv.data) == 'jpeg'