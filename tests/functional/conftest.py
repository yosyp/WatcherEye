"""

!IMPORTANT This file needs to be named conftest.py instead of __init__.py, and
define your application fixture for tests in conftest.py (This is the default
test configuration file used by pytest).
"""

import os
import tempfile
import pytest
import watchereye

@pytest.fixture
def client():
    """
    Set app mode to testing and startup the test client.
    Pytest runs all tests against this client.

    """

    watchereye.app.config['TESTING'] = True
    client = watchereye.app.test_client()

    yield client