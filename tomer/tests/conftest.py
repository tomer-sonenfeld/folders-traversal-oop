

import builtins
import pytest
from mockito import when, mock



@pytest.fixture
def mocked_open(request):
    testing_file_path = request.param
    file_mock = mock()
    when(builtins).open(testing_file_path, 'r').thenReturn(file_mock)
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__(None, None, None).thenReturn()
    return file_mock
