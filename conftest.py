import pytest
from mockito import unstub


@pytest.fixture(autouse=True)
def unstub_all():
    yield
    unstub()
