import pytest
from mockito import unstub, verifyStubbedInvocationsAreUsed


@pytest.fixture
def verify_mocks_were_stubbed():
    yield
    try:
        verifyStubbedInvocationsAreUsed()
    finally:
        unstub()
