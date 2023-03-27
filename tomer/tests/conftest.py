

import pytest
from mockito import unstub, verifyStubbedInvocationsAreUsed


@pytest.fixture
def teardown():
    yield
    try:
        verifyStubbedInvocationsAreUsed()
    finally:
        unstub()
